import { useEffect, useState } from "react";
import { getAnalyses } from "../api";
import echo from "../echo";
import TradingViewChart from "./TradingViewChart";
import RobotGuard from "./RobotGuard";

export default function Fonda() {
  const [analyses, setAnalyses] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const res = await getAnalyses();
      setAnalyses(res.data || []);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();

    // Temps réel
    echo.channel('analyses')
      .listen('.AnalysisCreated', (e: any) => {
        setAnalyses(prev => {
          const exists = prev.find(a => a.id === e.analysis.id);
          if (exists) return prev.map(a => a.id === e.analysis.id ? e.analysis : a);
          return [e.analysis, ...prev];
        });
      });

    return () => {
      echo.leaveChannel('analyses');
    };
  }, []);

  if (loading) return <div style={{ padding: 50, textAlign: 'center', color: 'var(--text-secondary)' }}>Chargement des analyses...</div>;

  return (
    <RobotGuard>
      <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
        <header style={{ marginBottom: '2rem', textAlign: 'center' }}>
          <h1 className="premium-gradient-text" style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>
            Analyses Techniques
          </h1>
          <div style={{ color: 'var(--text-secondary)' }}>
            Flux continu des opportunités détectées par le scanner LKL
          </div>
        </header>

        {analyses.length === 0 ? (
          <div className="glass-card" style={{ textAlign: 'center', padding: '3rem' }}>
            <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>📡</div>
            <h3>Aucune analyse récente</h3>
            <p style={{ opacity: 0.7 }}>Le bot scanne le marché... Les graphiques apparaîtront ici.</p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '2rem' }}>
            {analyses.map((a: any) => (
              <div key={a.id} className="glass-card" style={{ padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
                {/* Real TradingView Chart */}
                <div style={{ position: 'relative', height: '200px', background: '#0a0a0a' }}>
                  <TradingViewChart symbol={a.symbol} height={200} data={a.chart_data} />
                  <div style={{
                    position: 'absolute', top: 15, left: 15,
                    background: a.action === 'buy' ? '#10b981' : (a.action === 'sell' ? '#ef4444' : '#64748b'),
                    color: '#fff', fontWeight: 800, padding: '5px 10px', borderRadius: '8px',
                    fontSize: '0.9rem', boxShadow: '0 4px 10px rgba(0,0,0,0.5)',
                    zIndex: 10
                  }}>
                    {a.action ? a.action.toUpperCase() : 'NEUTRE'}
                  </div>
                  <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, padding: '10px 15px', background: 'linear-gradient(to top, rgba(0,0,0,0.9), transparent)', zIndex: 10 }}>
                    <div style={{ fontWeight: 700, fontSize: '1.2rem' }}>{a.symbol}</div>
                  </div>
                </div>

                {/* Details */}
                <div style={{ padding: '1.5rem', flex: 1, display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', borderBottom: '1px solid rgba(255,255,255,0.05)', paddingBottom: '10px' }}>
                    <span style={{ color: 'var(--text-secondary)' }}>Tendance H4</span>
                    <span style={{ fontWeight: 600 }}>{a.trend}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', borderBottom: '1px solid rgba(255,255,255,0.05)', paddingBottom: '10px' }}>
                    <span style={{ color: 'var(--text-secondary)' }}>Zone Fibo</span>
                    <span style={{ fontWeight: 600, color: 'var(--accent-blue)' }}>{a.fibo_zone}</span>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem' }}>
                    <span style={{ color: 'var(--text-secondary)' }}>Confirmation</span>
                    <span style={{ fontWeight: 600 }}>{a.confirmation_count} / 2</span>
                  </div>

                  <div style={{ marginTop: 'auto', paddingTop: '15px', fontSize: '0.8rem', color: 'var(--text-secondary)', fontStyle: 'italic' }}>
                    {new Date(a.created_at).toLocaleString()}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </RobotGuard>
  );
}
