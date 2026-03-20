import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Download, X, Smartphone, Monitor } from 'lucide-react';

const InstallBanner = () => {
    const [deferredPrompt, setDeferredPrompt] = useState<any>(null);
    const [isVisible, setIsVisible] = useState(false);
    const [isMobile, setIsMobile] = useState(false);

    useEffect(() => {
        // Détection mobile rapide
        const checkMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
        setIsMobile(checkMobile);

        const handleBeforeInstallPrompt = (e: any) => {
            e.preventDefault();
            setDeferredPrompt(e);
            // Ne montrer la bannière que si l'app n'est pas déjà installée (ou si on peut le deviner)
            if (!window.matchMedia('(display-mode: standalone)').matches) {
                setIsVisible(true);
            }
        };

        window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);

        // Pour iOS et certains Android, le prompt n'existe pas, on montre quand même pour donner des instructions
        if (checkMobile && !window.matchMedia('(display-mode: standalone)').matches) {
            setIsVisible(true);
        }

        return () => window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    }, []);

    const handleInstallClick = async () => {
        if (deferredPrompt) {
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            if (outcome === 'accepted') {
                setIsVisible(false);
            }
            setDeferredPrompt(null);
        } else if (isMobile) {
            // Instructions mobile
            alert("Pour installer LKL Bot sur votre téléphone :\n1. Cliquez sur l'icône de partage ou les 3 points du navigateur.\n2. Sélectionnez 'Ajouter à l'écran d'accueil'.");
        }
    };

    if (!isVisible) return null;

    return (
        <AnimatePresence>
            <motion.div
                initial={{ y: -100 }}
                animate={{ y: 0 }}
                exit={{ y: -100 }}
                style={{
                    position: 'sticky',
                    top: 0,
                    zIndex: 2000,
                    background: 'linear-gradient(90deg, #007cf0, #7928ca)',
                    padding: '12px 20px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    color: 'white',
                    boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
                    borderBottom: '1px solid rgba(255,255,255,0.2)'
                }}
            >
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    {isMobile ? <Smartphone size={20} /> : <Monitor size={20} />}
                    <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>
                        Installer LKL Bot sur votre {isMobile ? 'téléphone' : 'ordinateur'} pour une expérience optimale !
                    </span>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <button
                        onClick={handleInstallClick}
                        style={{
                            background: 'white',
                            color: '#007cf0',
                            padding: '6px 16px',
                            borderRadius: '20px',
                            fontSize: '0.85rem',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '6px'
                        }}
                    >
                        <Download size={14} /> Installer
                    </button>
                    <X
                        size={20}
                        style={{ cursor: 'pointer', opacity: 0.7 }}
                        onClick={() => setIsVisible(false)}
                    />
                </div>
            </motion.div>
        </AnimatePresence>
    );
};

export default InstallBanner;
