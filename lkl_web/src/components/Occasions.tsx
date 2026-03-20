import { useState, useEffect } from "react";
import { getAnalyses } from "../api";
import { motion } from "framer-motion";
import { TrendingUp, TrendingDown, Info } from "lucide-react";
import { useSound } from "../hooks/useSound";

export default function Occasions() {
    const [occasions, setOccasions] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const { playSound } = useSound();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await getAnalyses();
                setOccasions(data.data || []);
            } catch (e) {
                console.error(e);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    if (loading) return <div className="flex-center" style={{ height: '60vh' }}>Chargement des occasions...</div>;

    return (
        <div style={{ padding: '20px' }}>
            <h1 className="premium-gradient-text" style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '2rem' }}>🎯 Occasions de Marché</h1>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '20px' }}>
                {occasions.map((o, idx) => (
                    <motion.div
                        key={idx}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="glass-card snap-bounce"
                        style={{ borderLeft: o.action === 'buy' ? '4px solid #10b981' : '4px solid #ef4444' }}
                    >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
                            <h2 style={{ fontSize: '1.4rem', margin: 0 }}>{o.symbol}</h2>
                            <span style={{
                                padding: '5px 12px',
                                borderRadius: '20px',
                                background: o.action === 'buy' ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
                                color: o.action === 'buy' ? '#10b981' : '#ef4444',
                                fontWeight: 700,
                                textTransform: 'uppercase',
                                fontSize: '0.8rem'
                            }}>
                                {o.action === 'buy' ? <TrendingUp size={14} style={{ marginRight: 5 }} /> : <TrendingDown size={14} style={{ marginRight: 5 }} />}
                                {o.action}
                            </span>
                        </div>

                        <div style={{ background: 'rgba(255,255,255,0.03)', padding: '15px', borderRadius: '12px', marginBottom: '15px' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: 'var(--accent-blue)', marginBottom: '8px' }}>
                                <Info size={16} /> <span style={{ fontWeight: 600 }}>Stratégie Fondamentale</span>
                            </div>
                            <p style={{ margin: 0, fontSize: '0.95rem', opacity: 0.8, lineHeight: '1.5' }}>
                                {o.reason || "Analyse de convergence des banques centrales et sentiment social favorable."}
                            </p>
                        </div>

                        <div style={{ display: 'flex', gap: '15px', fontSize: '0.9rem' }}>
                            <div style={{ flex: 1 }}>
                                <div style={{ opacity: 0.5, marginBottom: '5px' }}>Probabilité</div>
                                <div style={{ fontWeight: 700 }}>{o.probability || "85%"}</div>
                            </div>
                            <div style={{ flex: 1 }}>
                                <div style={{ opacity: 0.5, marginBottom: '5px' }}>Zone Fibo</div>
                                <div style={{ fontWeight: 700 }}>{o.fibo_zone || "61.8%"}</div>
                            </div>
                            <div style={{ flex: 1 }}>
                                <div style={{ opacity: 0.5, marginBottom: '5px' }}>Impact</div>
                                <div style={{ fontWeight: 700, color: 'var(--accent-blue)' }}>Haut</div>
                            </div>
                        </div>

                        <button
                            onClick={() => { playSound('click'); /* Logic to follow trade */ }}
                            className="premium-button"
                            style={{ width: '100%', marginTop: '20px', padding: '12px', fontSize: '0.9rem' }}
                        >
                            DÉTAILS DU SIGNAL
                        </button>
                    </motion.div>
                ))}
            </div>
        </div>
    );
}
