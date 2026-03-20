import { invoke } from '@tauri-apps/api/tauri';
import { listen } from '@tauri-apps/api/event';

// Wrapper pour gérer les erreurs IPC
async function callCommand(command: string, args: any = {}) {
  try {
    const response = await invoke(command, args);
    return response;
  } catch (error) {
    console.error(`Tauri Command Error [${command}]:`, error);
    window.dispatchEvent(new CustomEvent('add-toast', {
      detail: { message: `Erreur System: ${error}`, type: 'error' }
    }));
    throw error;
  }
}

// ============================================
// CORE DATA (Connecté au StateManager Python)
// ============================================

export const getAnalyses = () => callCommand('get_analyses');
export const getTrades = () => callCommand('get_trades');
export const getLiveData = () => callCommand('get_uiview_state');
export const getCurrentUser = () => callCommand('get_settings'); // On desktop, user = settings

// ============================================
// ACTIONS UTILISATEUR
// ============================================

export const sendChatMessage = (message: string, userId: number) => callCommand('send_chat_message', { message, userId });
export const getChatHistory = (userId: number) => callCommand('get_chat_history', { userId });

export const toggleBot = (active: boolean) => callCommand('set_bot_state', { active });
export const getBotState = () => callCommand('get_bot_state');

// ============================================
// SETTINGS (SQLite Local)
// ============================================

export const getSettings = () => callCommand('get_settings');
export const updateSettings = (settings: any) => callCommand('update_settings', { settings });
export const updateTradingSettings = (settings: any) => callCommand('update_settings', { settings });
export const saveLicense = (key: string) => callCommand('save_license', { key });

// ============================================
// EVENTS (Remplaçant WebSockets / Pusher)
// ============================================

export { listen } from '@tauri-apps/api/event';
