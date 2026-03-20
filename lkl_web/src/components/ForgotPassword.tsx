import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { Mail, Lock, ArrowLeft, ShieldCheck } from "lucide-react";
import { useSound } from "../hooks/useSound";

export default function ForgotPassword() {
    const [step, setStep] = useState(1);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const { playSound } = useSound();
    const navigate = useNavigate();

    const handleEmailSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        playSound('click');
        setLoading(true);
        // Simulation de vérification d'email
        setTimeout(() => {
            setLoading(false);
            setStep(2);
            playSound('receive');
        }, 1500);
    };

    const handleResetSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: "Les mots de passe ne correspondent pas", type: 'error' } }));
            return;
        }
        playSound('send');
        setLoading(true);
        // Simulation de reset
        setTimeout(() => {
            setLoading(false);
            window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: "Mot de passe réinitialisé !", type: 'success' } }));
            navigate("/login");
        }, 2000);
    };

    const iconStyle = {
        position: 'absolute' as const,
        left: '16px',
        top: '50%',
        transform: 'translateY(-50%)',
        color: 'var(--accent-blue)',
        opacity: 0.7
    };

    return (
        <div className="premium-gradient-bg flex-center" style={{ minHeight: "100vh", padding: "20px" }}>
            <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="glass-card snap-bounce"
                style={{ width: "100%", maxWidth: "420px", padding: "40px", textAlign: "center" }}
            >
                <Link to="/login" onClick={() => playSound('click')} style={{ display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--text-secondary)', textDecoration: 'none', fontSize: '0.9rem', marginBottom: '20px' }}>
                    <ArrowLeft size={16} /> Retour
                </Link>

                <h2 className="premium-gradient-text" style={{ fontSize: "2rem", fontWeight: 800, marginBottom: "10px" }}>Récupération</h2>
                <p style={{ color: "var(--text-secondary)", marginBottom: "30px" }}>
                    {step === 1 ? "Entrez votre email pour réinitialiser votre accès." : "Définissez votre nouveau mot de passe sécurisé."}
                </p>

                <AnimatePresence mode="wait">
                    {step === 1 ? (
                        <motion.form key="step1" initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 20 }} onSubmit={handleEmailSubmit} style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
                            <div style={{ position: 'relative', textAlign: 'left' }}>
                                <label style={{ fontSize: '0.8rem', marginBottom: '5px', display: 'block' }}>Email</label>
                                <Mail size={18} style={iconStyle} />
                                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="votre@email.com" required style={{ paddingLeft: '48px' }} />
                            </div>
                            <button type="submit" disabled={loading} className="premium-button" style={{ padding: '16px', fontWeight: 700 }}>
                                {loading ? "VÉRIFICATION..." : "VÉRIFIER L'EMAIL"}
                            </button>
                        </motion.form>
                    ) : (
                        <motion.form key="step2" initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} onSubmit={handleResetSubmit} style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
                            <div style={{ position: 'relative', textAlign: 'left' }}>
                                <label style={{ fontSize: '0.8rem', marginBottom: '5px', display: 'block' }}>Nouveau mot de passe</label>
                                <Lock size={18} style={iconStyle} />
                                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="••••••••" required style={{ paddingLeft: '48px' }} />
                            </div>
                            <div style={{ position: 'relative', textAlign: 'left' }}>
                                <label style={{ fontSize: '0.8rem', marginBottom: '5px', display: 'block' }}>Confirmez le mot de passe</label>
                                <ShieldCheck size={18} style={iconStyle} />
                                <input type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} placeholder="••••••••" required style={{ paddingLeft: '48px' }} />
                            </div>
                            <button type="submit" disabled={loading} className="premium-button" style={{ padding: '16px', fontWeight: 700 }}>
                                {loading ? "RÉINITIALISATION..." : "MODIFIER LE MOT DE PASSE"}
                            </button>
                        </motion.form>
                    )}
                </AnimatePresence>
            </motion.div>
        </div>
    );
}
