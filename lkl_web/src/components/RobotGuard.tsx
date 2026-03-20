// Composant de garde-fou pour bloquer les fonctionnalités tant que le robot n'est pas actif
import { type ReactNode, useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { Bot, AlertCircle } from 'lucide-react';

interface RobotGuardProps {
    children: ReactNode;
    fallback?: ReactNode;
    showStandbyMessage?: boolean;
}

export default function RobotGuard({ children, fallback, showStandbyMessage = true }: RobotGuardProps) {
    const [robotActive, setRobotActive] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Vérifier l'état initial du robot
        const checkRobotStatus = async () => {
            try {
                const res = await fetch('http://localhost:8001/api/robot/status');
                const data = await res.json();
                setRobotActive(data.data.active);
            } catch (e) {
                console.error('Erreur vérification statut robot:', e);
                setRobotActive(false);
            } finally {
                setLoading(false);
            }
        };

        checkRobotStatus();

        // Écouter les changements d'état via événements personnalisés
        const handleRobotActivated = () => setRobotActive(true);
        const handleRobotDeactivated = () => setRobotActive(false);

        window.addEventListener('robot-activated', handleRobotActivated);
        window.addEventListener('robot-deactivated', handleRobotDeactivated);

        return () => {
            window.removeEventListener('robot-activated', handleRobotActivated);
            window.removeEventListener('robot-deactivated', handleRobotDeactivated);
        };
    }, []);

    if (loading) {
        return (
            <div className="flex-center" style={{ height: '60vh' }}>
                <div className="spinner"></div>
            </div>
        );
    }

    if (!robotActive) {
        if (fallback) return <>{fallback}</>;

        if (!showStandbyMessage) return null;

        return (
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="glass-card"
                style={{
                    padding: '3rem',
                    textAlign: 'center',
                    maxWidth: '600px',
                    margin: '3rem auto'
                }}
            >
                <div style={{ fontSize: '4rem', marginBottom: '1rem' }}>
                    <Bot size={80} style={{ color: 'var(--text-secondary)', opacity: 0.5 }} />
                </div>
                <h2 style={{ fontSize: '1.8rem', marginBottom: '1rem', color: 'var(--text-primary)' }}>
                    🤖 Robot en Veille
                </h2>
                <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem', marginBottom: '1.5rem' }}>
                    Le robot LKL est actuellement en mode veille. Démarrez-le depuis le Dashboard pour accéder à cette fonctionnalité.
                </p>
                <div
                    className="glass-card"
                    style={{
                        padding: '1rem',
                        background: 'rgba(239, 68, 68, 0.1)',
                        borderLeft: '4px solid #ef4444'
                    }}
                >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', justifyContent: 'center' }}>
                        <AlertCircle size={20} style={{ color: '#ef4444' }} />
                        <span style={{ color: '#ef4444', fontWeight: 600 }}>
                            Démarrez le robot pour commencer à trader
                        </span>
                    </div>
                </div>
            </motion.div>
        );
    }

    return <>{children}</>;
}
