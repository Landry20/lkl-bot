import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, Info, AlertCircle, CheckCircle, ExternalLink } from 'lucide-react';

export interface Toast {
    id: number;
    message: string;
    type: 'info' | 'error' | 'success';
    url?: string | null;
}

const ToastContainer = () => {
    const [toasts, setToasts] = useState<Toast[]>([]);

    useEffect(() => {
        const handleAddToast = (event: any) => {
            const { message, type, url } = event.detail;
            const id = Date.now();
            setToasts(prev => [...prev, { id, message, type, url }]);
            setTimeout(() => removeToast(id), 10000); // 10s pour laisser le temps de cliquer
        };

        window.addEventListener('add-toast', handleAddToast);
        return () => window.removeEventListener('add-toast', handleAddToast);
    }, []);

    const removeToast = (id: number) => {
        setToasts(prev => prev.filter(t => t.id !== id));
    };

    return (
        <div style={{ position: 'fixed', top: '20px', right: '20px', zIndex: 1000, display: 'flex', flexDirection: 'column', gap: '10px' }}>
            <AnimatePresence>
                {toasts.map(toast => (
                    <motion.div
                        key={toast.id}
                        initial={{ opacity: 0, x: 50 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, scale: 0.9 }}
                        style={{
                            background: '#1e293b',
                            border: '1px solid var(--glass-border)',
                            borderRadius: '12px',
                            padding: '12px 20px',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '12px',
                            boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
                            minWidth: '280px',
                            maxWidth: '450px'
                        }}
                    >
                        {toast.type === 'error' && <AlertCircle size={20} color="#ef4444" />}
                        {toast.type === 'info' && <Info size={20} color="#3b82f6" />}
                        {toast.type === 'success' && <CheckCircle size={20} color="#22c55e" />}

                        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '4px' }}>
                            <span style={{ fontSize: '0.9rem', color: '#f1f5f9' }}>{toast.message}</span>
                            {toast.url && (
                                <a
                                    href={toast.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    style={{
                                        color: 'var(--accent-blue)',
                                        fontSize: '0.8rem',
                                        textDecoration: 'none',
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: '5px',
                                        fontWeight: 600
                                    }}
                                >
                                    <ExternalLink size={14} /> Ouvrir le lien
                                </a>
                            )}
                        </div>

                        <X
                            size={16}
                            style={{ cursor: 'pointer', color: '#64748b' }}
                            onClick={() => removeToast(toast.id)}
                        />
                    </motion.div>
                ))}
            </AnimatePresence>
        </div>
    );
};

export default ToastContainer;
