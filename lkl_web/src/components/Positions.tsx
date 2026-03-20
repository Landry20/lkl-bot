// src/components/Positions.tsx
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getLiveData } from "../api";

export default function Positions() {
  const nav = useNavigate();
  const [positions, setPositions] = useState<any[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getLiveData();
        // Laravel paginate renvoie les données dans 'data'
        setPositions(data.data || data.positions || []);
      } catch (e) {
        console.error("Failed to fetch positions", e);
      }
    };
    fetchData();
    const i = setInterval(fetchData, 5000);
    return () => clearInterval(i);
  }, []);

  const getType = (r: string) => {
    if (r.includes("SCALP")) return { text: "SCALPING", color: "#ff6b6b" };
    if (r.includes("SWING")) return { text: "SWING", color: "#4ecdc4" };
    if (r.includes("DAY")) return { text: "DAY TRADING", color: "#f7b731" };
    return { text: "UNKNOWN", color: "#95a5a6" };
  };

  return (
    <div style={{ padding: 30, fontFamily: "'Segoe UI', sans-serif", maxWidth: 1200, margin: "auto" }}>
      <button onClick={() => nav("/")} style={{ marginBottom: 20, padding: "10px 20px", background: "#6c757d", color: "white", border: "none", borderRadius: 8 }}>
        ← Retour
      </button>
      <h1 style={{ textAlign: "center", color: "#1a1a1a" }}>POSITIONS OUVERTES</h1>
      {positions.length ? (
        <div style={{ display: "grid", gap: 15 }}>
          {positions.map(p => {
            const type = getType(p.reason);
            return (
              <div key={p.id} style={{
                background: "white", padding: 20, borderRadius: 14,
                boxShadow: "0 4px 12px rgba(0,0,0,0.1)", borderLeft: `5px solid ${type.color}`
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <div>
                    <strong style={{ fontSize: "1.3em" }}>{p.symbol}</strong>
                    <span style={{ marginLeft: 10, background: type.color, color: "white", padding: "4px 10px", borderRadius: 20, fontSize: "0.8em" }}>
                      {type.text}
                    </span>
                  </div>
                  <div style={{ textAlign: "right" }}>
                    <div><strong>Entry:</strong> {p.entry_price}</div>
                    <div><strong>SL:</strong> {p.sl} | <strong>TP:</strong> {p.tp}</div>
                  </div>
                </div>
                <div style={{ marginTop: 10, fontSize: "0.9em", color: "#555" }}>
                  {p.reason} | {new Date(p.created_at).toLocaleString()}
                </div>
              </div>
            );
          })}
        </div>
      ) : <p style={{ textAlign: "center", color: "#888", fontStyle: "italic" }}>Aucune position ouverte.</p>}
    </div>
  );
}