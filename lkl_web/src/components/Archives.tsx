import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getTrades } from "../api";

export default function Archives() {
  const nav = useNavigate();
  const [trades, setTrades] = useState<any[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getTrades();
        setTrades(data.data || data || []);
      } catch (e) {
        console.error("Archives fetch error", e);
      }
    };
    fetchData();
  }, []);

  return (
    <div style={{ padding: 30, fontFamily: "'Segoe UI', sans-serif", maxWidth: 1200, margin: "auto" }}>
      <button onClick={() => nav("/")} style={{ marginBottom: 20, padding: "10px 20px", background: "#6c757d", color: "white", border: "none", borderRadius: 8 }}>
        ← Retour
      </button>
      <h1 style={{ textAlign: "center", color: "#1a1a1a" }}>ARCHIVES DES TRADES</h1>
      {trades.length ? (
        <table style={{ width: "100%", borderCollapse: "collapse", background: "white", borderRadius: 12, overflow: "hidden", boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}>
          <thead style={{ background: "#007bff", color: "white" }}>
            <tr>
              <th style={{ padding: 15 }}>Symbole</th>
              <th style={{ padding: 15 }}>Type</th>
              <th style={{ padding: 15 }}>Profit</th>
              <th style={{ padding: 15 }}>Date</th>
            </tr>
          </thead>
          <tbody>
            {trades.map(t => (
              <tr key={t.id} style={{ borderBottom: "1px solid #eee" }}>
                <td style={{ padding: 12, textAlign: "center" }}>{t.symbol}</td>
                <td style={{ padding: 12, textAlign: "center" }}>{(t.type || '').toUpperCase()}</td>
                <td style={{ padding: 12, textAlign: "center", color: parseFloat(t.pnl) > 0 ? "#28a745" : "#dc3545" }}>
                  {parseFloat(t.pnl) > 0 ? "+" : ""}{t.pnl}$
                </td>
                <td style={{ padding: 12, textAlign: "center" }}>{new Date(t.created_at).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : <p style={{ textAlign: "center", color: "#888" }}>Aucun trade fermé.</p>}
    </div>
  );
}