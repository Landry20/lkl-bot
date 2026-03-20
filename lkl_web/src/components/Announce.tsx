import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getAnnouncements } from "../api";
import { Calendar, Clock, ExternalLink, AlertTriangle, AlertCircle, Info, BrainCircuit } from "lucide-react";

const API = "http://localhost:8000/api";

export default function Announce() {
  const nav = useNavigate();
  const [news, setNews] = useState<any[]>([]);
  const [botPredictions, setBotPredictions] = useState<any[]>([]);
  const [activeTab, setActiveTab] = useState<'macro' | 'geo' | '3t' | 'special'>('macro');

  const fetchData = async () => {
    try {
      const res = await getAnnouncements();
      setNews(res.data || []);

      const token = localStorage.getItem('token');
      const predRes = await fetch(`${API}/fundamental-analyses?category=macro`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const predData = await predRes.json();
      setBotPredictions(predData.data?.data || []);
    } catch (e) {
      console.error("Announce fetch error", e);
    }
  };

  useEffect(() => {
    fetchData();
    const i = setInterval(fetchData, 60000);
    return () => clearInterval(i);
  }, []);

  const getImpactDetails = (impact: string) => {
    switch (impact?.toUpperCase()) {
      case 'HIGH': return { color: "#ef4444", icon: <AlertCircle size={18} />, label: "Impact Élevé" };
      case 'MEDIUM': return { color: "#f59e0b", icon: <AlertTriangle size={18} />, label: "Impact Modéré" };
      default: return { color: "#3b82f6", icon: <Info size={18} />, label: "Impact Faible" };
    }
  };

  return (
    <div style={{ padding: "40px 20px", maxWidth: 1000, margin: "auto" }}>
      <button
        onClick={() => nav("/")}
        className="glass-button"
        style={{ marginBottom: 30, padding: "10px 20px", background: 'rgba(255,255,255,0.05)', color: '#fff', border: '1px solid var(--glass-border)', borderRadius: '8px', cursor: 'pointer' }}
      >
        ← Dashboard
      </button>

      <div style={{ display: 'flex', gap: '10px', marginBottom: '30px', overflowX: 'auto', paddingBottom: '10px' }}>
        {['macro', 'geo', '3t', 'special'].map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab as any)}
            className={activeTab === tab ? "active-nav-item" : ""}
            style={{
              padding: '10px 20px', borderRadius: '12px', border: '1px solid var(--glass-border)',
              background: activeTab === tab ? 'var(--accent-blue)' : 'rgba(255,255,255,0.05)',
              color: '#fff', cursor: 'pointer', transition: 'all 0.3s', textTransform: 'uppercase', fontSize: '0.8rem', fontWeight: 700
            }}
          >
            {tab === 'macro' ? '📉 Macro' : tab === 'geo' ? '🌍 Géo' : tab === '3t' ? '🔥 3T Impact' : '🌟 Spécial'}
          </button>
        ))}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
        {/* News Feed */}
        <div style={{ display: "grid", gap: 20 }}>
          <h2 style={{ fontSize: '1.2rem', opacity: 0.7, marginBottom: '10px' }}>
            {activeTab === 'macro' ? 'Calendrier Macro' : activeTab === 'geo' ? 'Actualité Géo' : activeTab === '3t' ? 'Impact 3T' : 'Événements Spéciaux'}
          </h2>
          {news.filter(n => {
            if (activeTab === 'macro') return n.currency === 'USD' || n.currency === 'EUR';
            if (activeTab === 'geo') return n.impact === 'HIGH' || n.status === 'HIGH';
            return true;
          }).length ? news.filter(n => {
            if (activeTab === 'macro') return n.currency === 'USD' || n.currency === 'EUR';
            if (activeTab === 'geo') return n.impact === 'HIGH' || n.status === 'HIGH';
            return true;
          }).map(n => {
            const details = getImpactDetails(n.status || n.impact);
            return (
              <div key={n.id} className="glass-card" style={{
                padding: 25, borderRadius: 16, borderLeft: `6px solid ${details.color}`
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 15 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 10, color: details.color, fontWeight: 700 }}>
                    {details.icon}
                    <span>{details.label}</span>
                  </div>
                  <div style={{ display: "flex", alignItems: "center", gap: 15, fontSize: "0.85rem", color: "#94a3b8" }}>
                    <Clock size={14} /> {n.time || n.datetime || (n.date ? new Date(n.date).toLocaleDateString('fr-FR', { weekday: 'short', day: 'numeric', month: 'short' }) : 'TBD')}
                  </div>
                </div>
                <h3 style={{ fontSize: "1.1rem", fontWeight: 600, color: "#f8fafc" }}>
                  <span style={{ color: 'var(--accent-blue)', marginRight: 10 }}>[{n.currency}]</span>
                  {n.event || n.title}
                </h3>
              </div>
            );
          }) : <div className="glass-card" style={{ padding: 20, opacity: 0.5 }}>Chargement du calendrier...</div>}
        </div>

        {/* Bot Predictions */}
        <div>
          <h2 style={{ fontSize: '1.2rem', opacity: 0.7, marginBottom: '10px', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <BrainCircuit size={20} color="var(--accent-blue)" /> Prédictions LKL
          </h2>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {botPredictions.length ? botPredictions.map(p => (
              <div key={p.id} className="glass-card" style={{ padding: '15px', fontSize: '0.9rem', border: '1px solid rgba(0,124,240,0.2)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                  <span style={{ fontWeight: 800, color: p.bias === 'bullish' ? '#10b981' : '#ef4444' }}>{p.bias.toUpperCase()}</span>
                  <span style={{ opacity: 0.5 }}>{new Date(p.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                </div>
                <p style={{ margin: 0, opacity: 0.9 }}>{p.content}</p>
                <div style={{ marginTop: '10px', fontSize: '0.75rem', color: 'var(--accent-blue)' }}>Confiance: {p.confidence}%</div>
              </div>
            )) : <div className="glass-card" style={{ padding: 20, opacity: 0.5 }}>Le bot prépare ses prévisions...</div>}
          </div>
        </div>
      </div>
    </div>
  );
}
