// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::{Manager, AppHandle};
use tauri::api::process::{Command as TauriCommand};
use rusqlite::Connection;
use std::path::PathBuf;
use serde::{Serialize, Deserialize};

// --- DATA STRUCTURES ---

#[derive(Serialize)]
struct Analysis {
    id: i32,
    symbol: String,
    action: String,
    trend: String,
    fibo_zone: String,
    price: f64,
    created_at: String
}

#[derive(Serialize)]
struct Trade {
    id: i32,
    ticket: i32,
    symbol: String,
    action: String,
    price: f64,
    sl: f64,
    tp: f64,
    lot: f64,
    profit: f64,
    status: String,
    created_at: String
}

#[derive(Serialize)]
struct ChatMessage {
    id: i32,
    user_id: i32,
    sender: String,
    message: String,
    msg_type: String,
    media_url: Option<String>,
    created_at: String
}

#[derive(Serialize)]
struct BotState {
    active: bool,
    status: String
}

// --- SQLITE COMMANDS (FAST READ) ---

fn get_db_path(app: &AppHandle) -> PathBuf {
    PathBuf::from("../../LKL_Trading_AI/data/knowledge.db")
}

#[tauri::command]
fn get_analyses(app: AppHandle) -> Result<Vec<Analysis>, String> {
    let db_path = get_db_path(&app);
    let conn = Connection::open(db_path).map_err(|e| e.to_string())?;
    let mut stmt = conn.prepare("SELECT id, symbol, action, trend, fibo_zone, price, created_at FROM analyses ORDER BY created_at DESC LIMIT 50").map_err(|e| e.to_string())?;
    let rows = stmt.query_map([], |row| {
        Ok(Analysis {
            id: row.get(0)?,
            symbol: row.get(1)?,
            action: row.get(2)?,
            trend: row.get(3)?,
            fibo_zone: row.get(4)?,
            price: row.get(5)?,
            created_at: row.get(6)?,
        })
    }).map_err(|e| e.to_string())?;
    let mut vec = Vec::new();
    for r in rows { if let Ok(x) = r { vec.push(x); } }
    Ok(vec)
}

#[tauri::command]
fn get_trades(app: AppHandle) -> Result<Vec<Trade>, String> {
    let db_path = get_db_path(&app);
    let conn = Connection::open(db_path).map_err(|e| e.to_string())?;
    let mut stmt = conn.prepare("SELECT id, ticket, symbol, type, price, sl, tp, lot, profit, status, created_at FROM trades ORDER BY created_at DESC LIMIT 50").map_err(|e| e.to_string())?;
    let rows = stmt.query_map([], |row| {
        Ok(Trade {
            id: row.get(0)?,
            ticket: row.get(1)?,
            symbol: row.get(2)?,
            action: row.get(3)?,
            price: row.get(4)?,
            sl: row.get(5)?,
            tp: row.get(6)?,
            lot: row.get(7)?,
            profit: row.get(8)?,
            status: row.get(9)?,
            created_at: row.get(10)?,
        })
    }).map_err(|e| e.to_string())?;
    let mut vec = Vec::new();
    for r in rows { if let Ok(x) = r { vec.push(x); } }
    Ok(vec)
}

#[tauri::command]
fn get_settings() -> Result<serde_json::Value, String> {
    Ok(serde_json::json!({
        "bot_running": "0",
        "risk_lot_size": 0.01,
        "mt5_login": "123456",
        "mt5_name": "Demo Account"
    }))
}

#[tauri::command]
fn update_settings(settings: serde_json::Value) -> Result<(), String> {
    println!("Updating settings: {:?}", settings);
    Ok(())
}

#[tauri::command]
async fn send_chat_message(message: String, user_id: i32) -> Result<String, String> {
    send_ipc_command("SEND_CHAT", &format!("{}|{}", user_id, message)).await
}

#[tauri::command]
fn get_chat_history(app: AppHandle, user_id: i32) -> Result<Vec<ChatMessage>, String> {
    let db_path = get_db_path(&app);
    let conn = Connection::open(db_path).map_err(|e| e.to_string())?;
    let mut stmt = conn.prepare("SELECT id, user_id, sender, message, type, media_url, created_at FROM chat_history WHERE user_id = ? ORDER BY created_at ASC").map_err(|e| e.to_string())?;
    let rows = stmt.query_map([user_id], |row| {
        Ok(ChatMessage {
            id: row.get(0)?,
            user_id: row.get(1)?,
            sender: row.get(2)?,
            message: row.get(3)?,
            msg_type: row.get(4)?,
            media_url: row.get(5)?,
            created_at: row.get(6)?,
        })
    }).map_err(|e| e.to_string())?;
    let mut vec = Vec::new();
    for r in rows { if let Ok(x) = r { vec.push(x); } }
    Ok(vec)
}

// --- PYTHON IPC COMMANDS (CONTROL) ---

async fn send_ipc_command(cmd: &str, payload: &str) -> Result<String, String> {
    use tokio::io::{AsyncWriteExt, AsyncReadExt};
    use tokio::net::TcpStream;
    let mut stream = TcpStream::connect("127.0.0.1:5555").await.map_err(|e| format!("Bot hors ligne ({})", e))?;
    let msg = format!("{}|{}", cmd, payload);
    stream.write_all(msg.as_bytes()).await.map_err(|e| e.to_string())?;
    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer).await.map_err(|e| e.to_string())?;
    Ok(String::from_utf8_lossy(&buffer[..n]).to_string())
}

#[tauri::command]
async fn set_bot_state(active: bool) -> Result<String, String> {
    let cmd = if active { "START" } else { "STOP" };
    send_ipc_command("SET_STATE", cmd).await
}

#[tauri::command]
async fn get_bot_state() -> Result<BotState, String> {
    let response = send_ipc_command("GET_STATE", "").await?;
    let parts: Vec<&str> = response.split('|').collect();
    Ok(BotState {
        active: parts.get(0).unwrap_or(&"OFF") == &"ACTIVE",
        status: parts.get(1).unwrap_or(&"Unknown").to_string()
    })
}

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let _window = app.get_window("main").unwrap();
            #[cfg(not(debug_assertions))]
            TauriCommand::new_sidecar("lkl_engine")
                 .expect("failed to setup sidecar")
                 .spawn()
                 .expect("failed to spawn sidecar");
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            get_analyses,
            get_trades,
            get_settings,
            update_settings,
            send_chat_message,
            get_chat_history,
            set_bot_state,
            get_bot_state
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
