import { useState, useEffect } from "react";
import { getAnalyses } from "../api";
import { motion, AnimatePresence } from "framer-motion";
import { MessageSquare, Target, Menu, X } from "lucide-react";
import { useSound } from "../hooks/useSound";

export default function TradingTerminal() {
    const [analyses, setAnalyses] = useState<any[]>([]);
    const [selected, setSelected] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [showMenu, setShowMenu] = useState(false);
    const { playSound } = useSound();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await getAnalyses();
                setAnalyses(data.data || []);
                if (data.data && data.data.length > 0) setSelected(data.data[0]);
            } catch (e) {
                console.error(e);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <div className="flex-center" style={{ height: '60vh' }}>Initialisation du terminal...</div>;

    return (
        <div style={{ padding: '10px', display: 'flex', flexDirection: 'column', gap: '15px', height: 'calc(100vh - 120px)', position: 'relative' }}>

            <div className="terminal-grid glass-card" style={{ padding: 0 }}>
                {/* Toggle Button */}
                <div
                    className="menu-toggle-btn"
                    onClick={() => { playSound('click'); setShowMenu(!showMenu); }}
                >
                    {showMenu ? <X size={20} /> : <Menu size={20} />}
                </div>

                {/* Sidebar Overlay */}
                <div className={`terminal-sidebar-overlay glass-card ${showMenu ? 'open' : ''}`} style={{ margin: 0, borderRadius: '0 24px 24px 0', borderLeft: 'none', background: '#0f172a' }}>
                    <div style={{ padding: '60px 20px 20px' }}>
                        <div style={{ padding: '10px', fontSize: '0.8rem', opacity: 0.5, textTransform: 'uppercase', letterSpacing: '1px' }}>Symboles Analysés</div>
                        {analyses.map((a, idx) => (
                            <div
                                key={idx}
                                onClick={() => { playSound('click'); setSelected(a); setShowMenu(false); }}
                                className={selected === a ? "active-nav-item" : ""}
                                style={{
                                    padding: '15px',
                                    borderRadius: '12px',
                                    cursor: 'pointer',
                                    marginBottom: '8px',
                                    background: selected === a ? 'var(--accent-blue)' : 'rgba(255,255,255,0.03)',
                                    transition: 'all 0.2s'
                                }}
                            >
                                <div style={{ fontWeight: 700 }}>{a.symbol}</div>
                                <div style={{ fontSize: '0.75rem', opacity: 0.7 }}>{a.action.toUpperCase()} - {a.fibo_zone}</div>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Main View Area */}
                <div className="chart-container-full" style={{ padding: '10px', overflowY: 'auto' }}>
                    {selected ? (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                            <h2 className="premium-gradient-text" style={{ margin: '0 0 10px 50px', fontSize: '1.5rem' }}>
                                {selected.symbol} - ANLYSE IA
                            </h2>

                            <motion.div
                                className="glass-card snap-bounce"
                                initial={{ opacity: 0, scale: 0.98 }}
                                animate={{ opacity: 1, scale: 1 }}
                                style={{ padding: 0, overflow: 'hidden', minHeight: '450px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#000', border: '1px solid rgba(255,255,255,0.1)' }}
                            >
                                <img
                                    src={selected.chart_url || `/assets/analyses/${selected.symbol}_analysis.png`}
                                    alt="Visualisation Technique"
                                    onError={(e: any) => {
                                        e.target.src = "/assets/chart_placeholder.png"; // Fallback
                                    }}
                                    style={{ width: '100%', height: 'auto', display: 'block' }}
                                />
                            </motion.div>

                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' }}>
                                <div className="glass-card" style={{ padding: '20px' }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-blue)', marginBottom: '10px' }}>
                                        <MessageSquare size={18} /> <h4 style={{ margin: 0 }}>Pourquoi ce Trade ?</h4>
                                    </div>
                                    <p style={{ lineHeight: '1.5', opacity: 0.8, fontSize: '0.9rem' }}>
                                        {selected.reason || "L'IA a détecté une divergence structurelle suggérant une opportunité de suivi."}
                                    </p>
                                </div>

                                <div className="glass-card" style={{ padding: '20px' }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: '#10b981', marginBottom: '10px' }}>
                                        <Target size={18} /> <h4 style={{ margin: 0 }}>Données Techniques</h4>
                                    </div>
                                    <ul style={{ padding: 0, listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.9rem' }}>
                                        <li style={{ display: 'flex', justifyContent: 'space-between' }}>
                                            <span style={{ opacity: 0.6 }}>Zone d'entrée</span>
                                            <span style={{ fontWeight: 700 }}>{selected.fibo_zone}</span>
                                        </li>
                                        <li style={{ display: 'flex', justifyContent: 'space-between' }}>
                                            <span style={{ opacity: 0.6 }}>Stop Loss</span>
                                            <span style={{ fontWeight: 700, color: '#ef4444' }}>{selected.sl || "Auto"}</span>
                                        </li>
                                        <li style={{ display: 'flex', justifyContent: 'space-between' }}>
                                            <span style={{ opacity: 0.6 }}>Take Profit</span>
                                            <span style={{ fontWeight: 700, color: '#10b981' }}>{selected.tp || "Auto"}</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="flex-center" style={{ height: '100%', opacity: 0.5 }}>Sélectionnez un symbole pour voir l'analyse.</div>
                    )}
                </div>
            </div>
        </div>
    );
}
