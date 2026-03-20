import { useEffect, useState } from 'react';
import { Globe, TrendingUp, Info, ShieldAlert, Map as MapIcon, Calendar } from 'lucide-react';

const API = "http://localhost:8000/api";

export default function MacroGeo() {
    const [latestAnalyses, setLatestAnalyses] = useState<any>(null);
    const [loading, setLoading] = useState(true);

    const fetchLatest = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`${API}/fundamental-analyses/latest`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            const data = await res.json();
            if (data.status === 'success') {
                setLatestAnalyses(data.data);
            }
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchLatest();
        const interval = setInterval(fetchLatest, 60000);
        return () => clearInterval(interval);
    }, []);

    if (loading) return <div style={{ padding: 50, textAlign: 'center' }}>Analyse des dossiers en cours...</div>;

    const geoData = latestAnalyses?.geo;
    const macroData = latestAnalyses?.macro;

    return (
        <div style={{ padding: '2rem', display: 'flex', flexDirection: 'column', gap: '2rem', maxWidth: '1600px', margin: '0 auto' }}>
            <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <h1 className="premium-gradient-text" style={{ fontSize: '2.5rem', margin: 0 }}>Macro & Géopolitique</h1>
                <div style={{ fontSize: '0.9rem', opacity: 0.6, display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <Globe size={18} className="animate-spin" style={{ animationDuration: '10s' }} />
                    Dernière Synthèse : {latestAnalyses?.synthese?.details?.divergence || 'Synchronisation...'}
                </div>
            </header>

            {latestAnalyses?.synthese && (
                <div className="glass-card" style={{ border: '1px solid var(--accent-blue)', background: 'linear-gradient(90deg, rgba(0,124,240,0.05) 0%, rgba(0,124,240,0) 100%)' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
                        <Info size={18} color="var(--accent-blue)" />
                        <h3 style={{ margin: 0, fontSize: '1.1rem' }}>Raisonnement Profond (Deep Reasoning)</h3>
                    </div>
                    <p style={{ margin: 0, fontWeight: 700, fontSize: '1.2rem', color: '#fff' }}>
                        {latestAnalyses.synthese.content}
                    </p>
                    <div style={{ marginTop: '10px', fontSize: '0.9rem', color: 'var(--accent-blue)' }}>
                        <strong>Divergence détectée :</strong> {latestAnalyses.synthese.details.divergence}
                    </div>
                </div>
            )}

            <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>

                {/* Section Gauche : Grid principale */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
                        {/* Macroeconomics */}
                        <div className="glass-card" style={{ borderLeft: '4px solid #10b981' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
                                <TrendingUp style={{ color: '#10b981' }} />
                                <h2 style={{ fontSize: '1.4rem', margin: 0 }}>Macroéconomie</h2>
                            </div>
                            {macroData ? (
                                <div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                                        <span style={{ fontWeight: 800, color: '#fff' }}>Biais: <span style={{ color: '#10b981' }}>{macroData.bias.toUpperCase()}</span></span>
                                        <span style={{ opacity: 0.6 }}>Confiance: {macroData.confidence}%</span>
                                    </div>
                                    <p style={{ lineHeight: '1.6', fontSize: '0.95rem' }}>{macroData.content}</p>
                                    <div style={{ marginTop: '1rem', display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                                        {macroData.details?.base?.map((d: any, i: number) => (
                                            <span key={i} style={{ background: 'rgba(16, 185, 129, 0.1)', padding: '4px 10px', borderRadius: '4px', fontSize: '0.8rem', color: '#10b981' }}>{d}</span>
                                        ))}
                                    </div>
                                </div>
                            ) : <div style={{ opacity: 0.5 }}>Aucune donnée macro.</div>}
                        </div>

                        {/* Geopolitics */}
                        <div className="glass-card" style={{ borderLeft: '4px solid #ef4444' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
                                <Globe style={{ color: '#ef4444' }} />
                                <h2 style={{ fontSize: '1.4rem', margin: 0 }}>Tensions Actives</h2>
                            </div>
                            {geoData ? (
                                <div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                                        <span style={{ fontWeight: 800, color: '#fff' }}>Risque: <span style={{ color: '#ef4444' }}>{geoData.confidence}%</span></span>
                                        <span style={{ opacity: 0.6 }}>Biais: {geoData.bias.toUpperCase()}</span>
                                    </div>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                                        {geoData.details?.explications?.map((e: string, i: number) => (
                                            <div key={i} style={{ fontSize: '0.9rem', padding: '10px', background: 'rgba(239, 68, 68, 0.05)', borderRadius: '8px', border: '1px solid rgba(239, 68, 68, 0.1)' }}>
                                                ⚠️ {e}
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            ) : <div style={{ opacity: 0.5 }}>Aucune alerte géo.</div>}
                        </div>
                    </div>

                    {/* Hotspot Visualization / Map Area */}
                    <div className="glass-card">
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
                            <MapIcon style={{ color: 'var(--accent-blue)' }} />
                            <h2 style={{ fontSize: '1.4rem', margin: 0 }}>Carte des Hotspots Géo-économiques</h2>
                        </div>
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '1rem' }}>
                            {geoData?.details?.hotspots ? Object.entries(geoData.details.hotspots).map(([area, info]: any) => (
                                <div key={area} style={{ padding: '15px', borderRadius: '12px', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--glass-border)' }}>
                                    <div style={{ fontSize: '0.8rem', opacity: 0.5, marginBottom: '5px' }}>ZÔNE</div>
                                    <div style={{ fontWeight: 800, marginBottom: '10px' }}>{area}</div>
                                    <div style={{ fontSize: '0.9rem', color: info.risk_level > 70 ? '#ef4444' : '#f59e0b' }}>Risque: {info.risk_level}%</div>
                                    <div style={{ marginTop: '8px', display: 'flex', gap: '5px' }}>
                                        {info.commodities?.map((c: string) => (
                                            <span key={c} style={{ fontSize: '0.7rem', background: 'rgba(0,124,240,0.2)', padding: '2px 6px', borderRadius: '4px' }}>{c}</span>
                                        ))}
                                    </div>
                                </div>
                            )) : <div style={{ opacity: 0.5 }}>Analyse de la carte en cours...</div>}
                        </div>
                    </div>
                </div>

                {/* Sidebar Droite : Sanctions & Pulse */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>

                    {/* Active Sanctions List */}
                    <div className="glass-card" style={{ borderTop: '4px solid #64748b' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
                            <ShieldAlert style={{ color: '#94a3b8' }} />
                            <h2 style={{ fontSize: '1.2rem', margin: 0 }}>Sanctions Actives (OFAC/UE)</h2>
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                            {geoData?.details?.sanctions ? geoData.details.sanctions.slice(0, 5).map((s: any, i: number) => (
                                <div key={i} style={{ fontSize: '0.85rem', padding: '12px', background: 'rgba(255,255,255,0.02)', borderRadius: '10px', border: '1px solid var(--glass-border)' }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '5px' }}>
                                        <span style={{ color: 'var(--accent-blue)', fontWeight: 700 }}>{s.source}</span>
                                        <span style={{ fontSize: '0.7rem', opacity: 0.5 }}>IMPACT: {s.impact_score}</span>
                                    </div>
                                    <div style={{ lineHeight: '1.4' }}>{s.title}</div>
                                </div>
                            )) : <div style={{ opacity: 0.5 }}>Aucune sanction récente.</div>}
                        </div>
                    </div>

                    {/* Central Bank Quick View */}
                    <div className="glass-card" style={{ borderTop: '4px solid var(--accent-blue)' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '1.5rem' }}>
                            <Calendar style={{ color: 'var(--accent-blue)' }} />
                            <h2 style={{ fontSize: '1.2rem', margin: 0 }}>Pulse Discours</h2>
                        </div>
                        {latestAnalyses?.discours ? (
                            <div>
                                <div style={{ fontSize: '0.9rem', opacity: 0.8, marginBottom: '10px' }}>{latestAnalyses.discours.content}</div>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                    <span style={{
                                        padding: '4px 10px',
                                        borderRadius: '20px',
                                        background: latestAnalyses.discours.bias === 'bullish' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)',
                                        color: latestAnalyses.discours.bias === 'bullish' ? '#10b981' : '#ef4444',
                                        fontSize: '0.8rem',
                                        fontWeight: 800
                                    }}>
                                        TON: {latestAnalyses.discours.details?.ton?.toUpperCase()}
                                    </span>
                                    <span style={{ fontSize: '0.8rem', opacity: 0.5 }}>Sentiment: {latestAnalyses.discours.details?.sentiment}</span>
                                </div>
                            </div>
                        ) : <div style={{ opacity: 0.5 }}>Aucun discours récent analysé.</div>}
                    </div>

                </div>

            </div>
        </div>
    );
}
