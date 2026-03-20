import React, { useState, useEffect } from 'react';
import { AlertTriangle, RefreshCw, X, ChevronDown, ChevronUp } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const ErrorOverlay: React.FC = () => {
    const [error, setError] = useState<any>(null);
    const [showDetails, setShowDetails] = useState(false);

    useEffect(() => {
        const handleError = (e: any) => {
            setError(e.detail);
        };
        window.addEventListener('system-error', handleError);
        return () => window.removeEventListener('system-error', handleError);
    }, []);

    if (!error) return null;

    return (
        <AnimatePresence>
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                style={{
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    background: 'rgba(5, 8, 15, 0.85)',
                    backdropFilter: 'blur(12px)',
                    zIndex: 9999,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '20px'
                }}
            >
                <motion.div
                    initial={{ scale: 0.9, y: 20 }}
                    animate={{ scale: 1, y: 0 }}
                    className="glass-card"
                    style={{
                        maxWidth: '600px',
                        width: '100%',
                        padding: '40px',
                        borderRadius: '32px',
                        border: '1px solid rgba(255, 60, 60, 0.3)',
                        textAlign: 'center',
                        position: 'relative',
                        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)'
                    }}
                >
                    <button
                        onClick={() => setError(null)}
                        style={{ position: 'absolute', top: 20, right: 20, background: 'none', border: 'none', color: 'var(--text-secondary)', cursor: 'pointer' }}
                    >
                        <X size={24} />
                    </button>

                    <div style={{
                        width: '80px',
                        height: '80px',
                        background: 'rgba(239, 68, 68, 0.1)',
                        borderRadius: '24px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        margin: '0 auto 24px',
                        color: '#ef4444'
                    }}>
                        <AlertTriangle size={40} />
                    </div>

                    <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '16px', color: '#fff' }}>
                        Oups ! Quelque chose a freiné le robot.
                    </h2>

                    <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem', marginBottom: '32px', lineHeight: 1.6 }}>
                        Une erreur est survenue lors de la communication avec le serveur (Status: {error.status || 'Inconnu'}).
                        Le robot ne peut pas continuer tant que cette erreur n'est pas résolue.
                    </p>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <button
                            onClick={() => window.location.reload()}
                            className="premium-button"
                            style={{
                                width: '100%',
                                padding: '18px',
                                fontSize: '1.1rem',
                                fontWeight: 700,
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                gap: '10px'
                            }}
                        >
                            <RefreshCw size={20} /> ACTUALISER LA PAGE
                        </button>

                        <button
                            onClick={() => setShowDetails(!showDetails)}
                            style={{
                                background: 'rgba(255,255,255,0.05)',
                                border: '1px solid rgba(255,255,255,0.1)',
                                color: 'var(--text-secondary)',
                                padding: '12px',
                                borderRadius: '12px',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                gap: '8px',
                                cursor: 'pointer',
                                fontSize: '0.9rem'
                            }}
                        >
                            {showDetails ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                            Détails techniques pour Lou Kou
                        </button>
                    </div>

                    <AnimatePresence>
                        {showDetails && (
                            <motion.div
                                initial={{ height: 0, opacity: 0 }}
                                animate={{ height: 'auto', opacity: 1 }}
                                exit={{ height: 0, opacity: 0 }}
                                style={{ overflow: 'hidden' }}
                            >
                                <div style={{
                                    marginTop: '20px',
                                    padding: '16px',
                                    background: '#000',
                                    borderRadius: '16px',
                                    textAlign: 'left',
                                    fontFamily: 'monospace',
                                    fontSize: '0.85rem',
                                    color: '#66ee66',
                                    maxHeight: '200px',
                                    overflowY: 'auto',
                                    border: '1px solid rgba(255,255,255,0.1)'
                                }}>
                                    <div><strong>URL:</strong> {error.url}</div>
                                    <div><strong>Status:</strong> {error.status}</div>
                                    <div style={{ marginTop: '8px', color: 'var(--text-secondary)' }}>
                                        <strong>Message:</strong><br />
                                        {typeof error.data === 'string' ? error.data : JSON.stringify(error.data, null, 2)}
                                    </div>
                                </div>
                            </motion.div>
                        )}
                    </AnimatePresence>
                </motion.div>
            </motion.div>
        </AnimatePresence>
    );
};

export default ErrorOverlay;
