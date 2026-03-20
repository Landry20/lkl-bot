import { useEffect, useState } from "react";
import { getTrades, getPositions, getAnnouncements } from "../api";
import { useNavigate } from "react-router-dom";
import { TrendingUp, Activity, ShieldCheck, Zap } from "lucide-react";

export default function Today() {
  const [trades, setTrades] = useState<any[]>([]);
  const [positions, setPositions] = useState<any[]>([]);
  const [ann, setAnn] = useState<any[]>([]);
  const nav = useNavigate();

  useEffect(() => {
    Promise.all([getTrades(), getPositions(), getAnnouncements()])
      .then(([t, p, a]) => {
        const tradeList = t.data || t || [];
        const posList = p.data || p || [];
        setTrades(tradeList.filter((x: any) => new Date(x.created_at).toDateString() === new Date().toDateString()));
        setPositions(posList.filter((x: any) => new Date(x.datetime || x.created_at).toDateString() === new Date().toDateString()));
        setAnn(a.data || a || []);
      })
      .catch(e => console.error("Today fetch error", e));
  }, []);

  const getPLColor = (v: number) => v >= 0 ? "#10b981" : "#ef4444";

  return (
    <div style={{ padding: "40px 20px", maxWidth: 1200, margin: "auto" }}>
      <button
        onClick={() => nav("/")}
        className="glass-button"
        style={{ marginBottom: 30, padding: "10px 20px", background: 'rgba(255,255,255,0.05)', color: '#fff', border: '1px solid var(--glass-border)', borderRadius: '8px', cursor: 'pointer' }}
      >
        ← Dashboard
      </button>

      <header style={{ marginBottom: '3rem', textAlign: 'center' }}>
        <h1 className="premium-gradient-text" style={{ fontSize: '3rem', margin: 0 }}>AUJOURD'HUI</h1>
        <p style={{ color: '#94a3b8', fontSize: '1.2rem' }}>Performance et Biais du Jour</p>
      </header>

      {/* KPI Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1.5rem', marginBottom: '3rem' }}>
        <div className="glass-card" style={{ textAlign: 'center' }}>
          <div style={{ opacity: 0.6, fontSize: '0.8rem', marginBottom: '10px' }}>PROFIT JOUR</div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: getPLColor(trades.reduce((acc, t) => acc + parseFloat(t.pnl), 0)) }}>
            ${trades.reduce((acc, t) => acc + parseFloat(t.pnl), 0).toFixed(2)}
          </div>
        </div>
        <div className="glass-card" style={{ textAlign: 'center' }}>
          <div style={{ opacity: 0.6, fontSize: '0.8rem', marginBottom: '10px' }}>POSITIONS ACTIVES</div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--accent-blue)' }}>{positions.length}</div>
        </div>
        <div className="glass-card" style={{ textAlign: 'center' }}>
          <div style={{ opacity: 0.6, fontSize: '0.8rem', marginBottom: '10px' }}>ANNONCES À VENIR</div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#f59e0b' }}>{ann.length}</div>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        {/* Main Content */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
          <section className="glass-card">
            <h3 style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
              <Activity size={20} color="var(--accent-blue)" /> Positions Ouvertes
            </h3>
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead>
                <tr style={{ background: "rgba(255,255,255,0.03)", textAlign: 'left' }}>
                  <th style={{ padding: 12 }}>Symbole</th>
                  <th style={{ padding: 12 }}>Type</th>
                  <th style={{ padding: 12 }}>Lot</th>
                  <th style={{ padding: 12 }}>Motif Reasoning</th>
                </tr>
              </thead>
              <tbody>
                {positions.length ? positions.map((x: any) => (
                  <tr key={x.id} style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                    <td style={{ padding: 15, fontWeight: 700 }}>{x.symbol}</td>
                    <td style={{ padding: 15, color: x.type === 'buy' ? '#10b981' : '#ef4444' }}>{x.type.toUpperCase()}</td>
                    <td style={{ padding: 15 }}>{x.lot}</td>
                    <td style={{ padding: 15, fontSize: '0.85rem', opacity: 0.8 }}>{x.reason}</td>
                  </tr>
                )) : <tr><td colSpan={4} style={{ padding: 30, textAlign: 'center', opacity: 0.5 }}>Aucune position en cours.</td></tr>}
              </tbody>
            </table>
          </section>

          <section className="glass-card">
            <h3 style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
              <ShieldCheck size={20} color="#10b981" /> Dernières Closes (Aujourd'hui)
            </h3>
            <div style={{ display: 'grid', gap: '10px' }}>
              {trades.map((x: any) => (
                <div key={x.id} style={{ background: 'rgba(255,255,255,0.03)', padding: '12px 20px', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <span style={{ fontWeight: 700, marginRight: '15px' }}>{x.symbol}</span>
                    <span style={{ opacity: 0.6, fontSize: '0.8rem' }}>{x.type.toUpperCase()}</span>
                  </div>
                  <div style={{ fontWeight: 800, color: getPLColor(x.pnl) }}>
                    {x.pnl >= 0 ? "+" : ""}${parseFloat(x.pnl || 0).toFixed(2)}
                  </div>
                </div>
              ))}
            </div>
          </section>
        </div>

        {/* Sidebar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <section className="glass-card">
            <h3 style={{ fontSize: '1.1rem', marginBottom: '1.2rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Zap size={18} color="#f59e0b" /> Alertes Pulse
            </h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              {ann.length ? ann.slice(0, 5).map(x => (
                <div key={x.id} style={{ fontSize: '0.85rem', borderLeft: `3px solid ${x.impact === 'high' ? '#ef4444' : '#f59e0b'}`, paddingLeft: '10px', marginBottom: '5px' }}>
                  <div style={{ opacity: 0.5, fontSize: '0.7rem' }}>{x.time || 'Aujourd\'hui'}</div>
                  <div><strong>{x.currency}</strong> - {x.event}</div>
                </div>
              )) : <div style={{ opacity: 0.5 }}>Pas d'alertes majeures.</div>}
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}