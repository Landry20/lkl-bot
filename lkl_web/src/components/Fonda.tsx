import { useEffect, useState } from "react";
import { getAnalyses } from "../api";
import echo from "../echo";
import { motion, AnimatePresence } from "framer-motion";

export default function Fonda() {
  const [analyses, setAnalyses] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);

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
    <div style={{ maxWidth: '1400px', margin: '0 auto' }}>
      <header style={{ marginBottom: '2rem', textAlign: 'center' }}>
        <h1 className="premium-gradient-text" style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>
          Analyses Techniques
        </h1>
        <div style={{ color: 'var(--text-secondary)' }}>
          Flux continu des opportunités détectées par le scanner LKL
        </div>
      </header>

      {/* Lightbox */}
      <AnimatePresence>
        {selectedImage && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedImage(null)}
            style={{
              position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
              background: 'rgba(0,0,0,0.9)', zIndex: 9999,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              cursor: 'zoom-out'
            }}
          >
            <motion.img
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              src={selectedImage}
              style={{ maxHeight: '90vh', maxWidth: '90vw', borderRadius: '10px' }}
            />
          </motion.div>
        )}
      </AnimatePresence>

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
              {/* Image Chart */}
              <div
                style={{ position: 'relative', height: '220px', background: '#000', cursor: 'zoom-in' }}
                onClick={() => setSelectedImage(a.image_url || `/${a.symbol}_analysis.png`)}
              >
                <img
                  src={a.image_url || `/${a.symbol}_analysis.png`}
                  alt={a.symbol}
                  style={{ width: '100%', height: '100%', objectFit: 'cover', opacity: 0.9 }}
                  onError={(e: any) => e.target.style.display = 'none'}
                />
                <div style={{
                  position: 'absolute', top: 15, left: 15,
                  background: a.action === 'buy' ? '#10b981' : (a.action === 'sell' ? '#ef4444' : '#64748b'),
                  color: '#fff', fontWeight: 800, padding: '5px 10px', borderRadius: '8px',
                  fontSize: '0.9rem', boxShadow: '0 4px 10px rgba(0,0,0,0.5)'
                }}>
                  {a.action ? a.action.toUpperCase() : 'NEUTRE'}
                </div>
                <div style={{ position: 'absolute', bottom: 10, right: 10, background: 'rgba(0,0,0,0.6)', padding: '5px 10px', borderRadius: '20px', fontSize: '0.8rem' }}>
                  🔍 Agrandir
                </div>
              </div>

              {/* Details & Reasoning */}
              <div style={{ padding: '1.5rem', flex: 1, display: 'flex', flexDirection: 'column', gap: '15px' }}>

                {/* Header info */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h3 style={{ margin: 0 }}>{a.symbol}</h3>
                  <span style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>{a.timeframe}</span>
                </div>

                <div style={{ background: 'rgba(255,255,255,0.03)', padding: '15px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.05)' }}>
                  <h4 style={{ margin: '0 0 10px 0', fontSize: '0.95rem', color: 'var(--accent-blue)' }}>💡 Pourquoi ce signal ?</h4>
                  <div style={{ fontSize: '0.9rem', opacity: 0.8, lineHeight: '1.5' }}>
                    {a.details ? a.details.split(',').map((d: string, i: number) => (
                      <div key={i} style={{ marginBottom: '4px' }}>• {d.trim()}</div>
                    )) : "Analyse technique validée par la stratégie."}
                  </div>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', marginTop: 'auto', paddingTop: '10px', borderTop: '1px solid rgba(255,255,255,0.05)' }}>
                  <span style={{ color: 'var(--text-secondary)' }}>Tendance H4: <b style={{ color: '#fff' }}>{a.trend}</b></span>
                  <span style={{ color: 'var(--text-secondary)' }}>Confirmations: <b style={{ color: '#fff' }}>{a.confirmation_count}/2</b></span>
                </div>

                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', textAlign: 'right' }}>
                  {new Date(a.created_at).toLocaleString()}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}