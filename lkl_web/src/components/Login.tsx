import React, { useState } from "react";
import { Link } from "react-router-dom";
import { login } from "../api";
import { motion } from "framer-motion";
import { Eye, EyeOff, Mail, Lock } from "lucide-react";
import { useSound } from "../hooks/useSound";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);
    const [loading, setLoading] = useState(false);
    const [lang, setLang] = useState(localStorage.getItem('language') || 'fr');
    const { playSound } = useSound();

    const translations: any = {
        fr: {
            subtitle: "Connectez-vous à votre terminal",
            email: "Email",
            password: "Mot de passe",
            login: "SE CONNECTER",
            connecting: "CONNEXION EN COURS...",
            noAccount: "Pas encore de compte ?",
            register: "S'inscrire",
            success: "Connexion réussie",
            error: "Identifiants incorrects"
        },
        en: {
            subtitle: "Connect to your terminal",
            email: "Email",
            password: "Password",
            login: "LOGIN",
            connecting: "CONNECTING...",
            noAccount: "Don't have an account?",
            register: "Register",
            success: "Login successful",
            error: "Invalid credentials"
        }
    };

    const t = translations[lang];

    const toggleLang = (l: string) => {
        playSound('click');
        setLang(l);
        localStorage.setItem('language', l);
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        playSound('send');
        setLoading(true);
        try {
            const res = await login({ email, password });
            if (res.access_token) {
                localStorage.setItem("token", res.access_token);
                localStorage.setItem("user", JSON.stringify(res.user));
                window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: t.success, type: 'success' } }));

                // Force reload to ensure auth state is updated
                setTimeout(() => {
                    window.location.href = "/";
                }, 500);
            } else {
                window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: res.message || t.error, type: 'error' } }));
            }
        } catch (err) {
            console.error(err);
            window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: t.error, type: 'error' } }));
        } finally {
            setLoading(false);
        }
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
        <div className="premium-gradient-bg" style={{
            minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px", position: "relative"
        }}>
            {/* Lang Switcher */}
            <div style={{ position: 'absolute', top: '20px', right: '20px', display: 'flex', gap: '10px' }}>
                <button onClick={() => toggleLang('fr')} style={{ padding: '5px 10px', background: lang === 'fr' ? 'var(--accent-blue)' : 'rgba(255,255,255,0.1)', fontSize: '0.8rem', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>FR</button>
                <button onClick={() => toggleLang('en')} style={{ padding: '5px 10px', background: lang === 'en' ? 'var(--accent-blue)' : 'rgba(255,255,255,0.1)', fontSize: '0.8rem', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>EN</button>
            </div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="glass-card snap-bounce"
                style={{ width: "100%", maxWidth: "420px", padding: "40px", textAlign: "center" }}
            >
                <div style={{ marginBottom: "30px" }}>
                    <img src="/lkl_logo_white.png" alt="LKL Logo" style={{ width: "80px", marginBottom: "10px" }} />
                    <h1 className="premium-gradient-text" style={{ fontSize: "2.5rem", margin: 0, fontWeight: 800 }}>LKL BOT</h1>
                    <p style={{ color: "var(--text-secondary)", marginTop: "10px", fontSize: '1rem' }}>{t.subtitle}</p>
                </div>

                <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
                    <div className="input-field" style={{ textAlign: "left" }}>
                        <label style={{ color: "#fff", marginBottom: '8px', display: 'block', fontSize: '0.9rem' }}>{t.email}</label>
                        <div style={{ position: 'relative' }}>
                            <Mail size={18} style={iconStyle} />
                            <input
                                type="text"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder="votre@email.com"
                                style={{ paddingLeft: '48px', width: '100%' }}
                                required
                            />
                        </div>
                    </div>
                    <div className="input-field" style={{ textAlign: "left" }}>
                        <label style={{ color: "#fff", marginBottom: '8px', display: 'block', fontSize: '0.9rem' }}>{t.password}</label>
                        <div style={{ position: 'relative' }}>
                            <Lock size={18} style={iconStyle} />
                            <input
                                type={showPassword ? "text" : "password"}
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="••••••••"
                                style={{ paddingLeft: '48px', paddingRight: '48px', width: '100%' }}
                                required
                            />
                            <div
                                onClick={() => setShowPassword(!showPassword)}
                                style={{ position: 'absolute', right: '16px', top: '50%', transform: 'translateY(-50%)', cursor: 'pointer', color: 'var(--text-secondary)' }}
                            >
                                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                            </div>
                        </div>
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="premium-button"
                        style={{
                            marginTop: "10px",
                            padding: "16px",
                            fontSize: "1rem",
                            fontWeight: 700,
                            letterSpacing: '1px'
                        }}
                    >
                        {loading ? t.connecting : t.login}
                    </button>
                </form>

                <div style={{ marginTop: "20px", fontSize: "0.9rem" }}>
                    <Link to="/forgot-password" onClick={() => playSound('click')} style={{ color: "var(--text-secondary)", textDecoration: "none" }}>Mot de passe oublié ?</Link>
                </div>

                <div style={{ marginTop: "20px", fontSize: "0.95rem", color: "var(--text-secondary)" }}>
                    {t.noAccount} <Link to="/register" onClick={() => playSound('click')} style={{ color: "var(--accent-blue)", textDecoration: "none", fontWeight: 700, marginLeft: '5px' }}>{t.register}</Link>
                </div>
            </motion.div>
        </div>
    );
}
