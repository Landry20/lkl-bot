import { useCallback } from 'react';

/**
 * Hook LKL pour les effets sonores UI chic
 * Utilise l'AudioContext pour éviter de dépendre de fichiers externes lourds.
 */
export const useSound = () => {
    const playSound = useCallback((type: 'send' | 'receive' | 'click') => {
        try {
            const AudioContext = window.AudioContext || (window as any).webkitAudioContext;
            if (!AudioContext) return;

            const ctx = new AudioContext();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.connect(gain);
            gain.connect(ctx.destination);

            const now = ctx.currentTime;

            if (type === 'send') {
                // Son "Clink" ascendant, léger
                osc.type = 'sine';
                osc.frequency.setValueAtTime(800, now);
                osc.frequency.exponentialRampToValueAtTime(1200, now + 0.1);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
            } else if (type === 'receive') {
                // Son "Pling" cristallin
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(1200, now);
                osc.frequency.exponentialRampToValueAtTime(800, now + 0.15);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            } else {
                // Son "Click" sec et discret
                osc.type = 'square';
                osc.frequency.setValueAtTime(200, now);
                gain.gain.setValueAtTime(0.05, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
            }

            osc.start(now);
            osc.stop(now + 0.2);
        } catch (e) {
            console.warn("Audio Context non supporté", e);
        }
    }, []);

    return { playSound };
};
