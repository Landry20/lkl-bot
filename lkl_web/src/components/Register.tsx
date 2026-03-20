import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate, Link } from 'react-router-dom';
import { User, Mail, Lock, Phone, CreditCard, Calendar, Eye, EyeOff } from 'lucide-react';
import { register } from '../api';
import { useSound } from '../hooks/useSound';

const countries = ["France", "Côte d'Ivoire", "Sénégal", "Bénin", "Togo", "Mali", "Burkina Faso", "Cameroun", "Gabon"];
const idTypes = ["Passeport", "Carte d'Identité", "Permis de Conduire"];

const Register = () => {
    const [step, setStep] = useState(1);
    const [loading, setLoading] = useState(false);
    const [lang, setLang] = useState(localStorage.getItem('language') || 'fr');
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [formData, setFormData] = useState({
        name: '', email: '', password: '', password_confirmation: '',
        phone: '', id_type: 'Passeport', id_country: 'Côte d\'Ivoire', id_number: '', dob: '',
        mt5_login: '', mt5_password: '', mt5_server: '', mt5_broker: ''
    });
    const { playSound } = useSound();
    const navigate = useNavigate();

    const translations: any = {
        fr: {
            title: "LKL Bot",
            stepOf: "Étape {step} sur 2",
            name: "Nom Complet",
            email: "Email",
            password: "Mot de passe",
            confirmPassword: "Confirmer mot de passe",
            next: "Suivant",
            back: "Retour",
            register: "S'enregistrer",
            creating: "CRÉATION...",
            phone: "Téléphone",
            dob: "Date de naissance",
            idNumber: "Numéro de pièce (Optionnel)",
            success: "Compte créé avec succès",
            alreadyHave: "Déjà un compte ?",
            login: "Se connecter"
        },
        en: {
            title: "LKL Bot",
            stepOf: "Step {step} of 2",
            name: "Full Name",
            email: "Email",
            password: "Password",
            confirmPassword: "Confirm Password",
            next: "Next",
            back: "Back",
            register: "Register",
            creating: "CREATING...",
            phone: "Phone",
            dob: "Date of Birth",
            idNumber: "ID Number (Optional)",
            success: "Account created successfully",
            alreadyHave: "Already have an account?",
            login: "Login"
        }
    };

    const t = translations[lang];

    const toggleLang = (l: string) => {
        playSound('click');
        setLang(l);
        localStorage.setItem('language', l);
    };

    const handleChange = (e: any) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const nextStep = () => { playSound('click'); setStep(step + 1); };
    const prevStep = () => { playSound('click'); setStep(step - 1); };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        playSound('send');
        setLoading(true);
        try {
            const res = await register(formData);
            if (res.access_token) {
                localStorage.setItem('token', res.access_token);
                localStorage.setItem("user", JSON.stringify(res.user));
                window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: t.success, type: 'success' } }));
                navigate('/');
            }
        } catch (error) {
            console.error("Registration error", error);
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
        opacity: 0.7,
        zIndex: 2
    };

    const inputGroupStyle = {
        position: 'relative' as const,
        width: '100%'
    };

    const registerInputStyle = {
        paddingLeft: '48px',
        width: '100%'
    };

    return (
        <div style={{ minHeight: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center', background: 'radial-gradient(circle at 50% 0%, #172554 0%, #0a0e17 100%)', position: 'relative', padding: '20px' }}>
            {/* Lang Switcher */}
            <div style={{ position: 'absolute', top: '20px', right: '20px', display: 'flex', gap: '10px' }}>
                <button onClick={() => toggleLang('fr')} style={{ padding: '5px 10px', background: lang === 'fr' ? 'var(--accent-blue)' : 'rgba(255,255,255,0.1)', fontSize: '0.8rem', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>FR</button>
                <button onClick={() => toggleLang('en')} style={{ padding: '5px 10px', background: lang === 'en' ? 'var(--accent-blue)' : 'rgba(255,255,255,0.1)', fontSize: '0.8rem', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>EN</button>
            </div>

            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="glass-card snap-bounce"
                style={{ width: '100%', maxWidth: '500px', padding: '3rem' }}
            >
                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                    <h2 className="premium-gradient-text" style={{ fontSize: '2.5rem', fontWeight: 800 }}>{t.title}</h2>
                    <p style={{ color: 'var(--text-secondary)', marginTop: '0.5rem' }}>{t.stepOf.replace('{step}', step.toString())}</p>
                </div>

                <form onSubmit={handleSubmit}>
                    <AnimatePresence mode="wait">
                        {step === 1 && (
                            <motion.div
                                key="step1"
                                initial={{ opacity: 0, x: -20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: 20 }}
                                style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}
                            >
                                <div style={inputGroupStyle} className="snap-bounce">
                                    <User size={18} style={iconStyle} />
                                    <input type="text" name="name" placeholder={t.name} value={formData.name} onChange={(e) => { handleChange(e); playSound('click'); }} required style={registerInputStyle} />
                                </div>
                                <div style={inputGroupStyle} className="snap-bounce">
                                    <Mail size={18} style={iconStyle} />
                                    <input type="text" name="email" placeholder={t.email} value={formData.email} onChange={(e) => { handleChange(e); playSound('click'); }} required style={registerInputStyle} />
                                </div>
                                <div style={inputGroupStyle} className="snap-bounce">
                                    <Lock size={18} style={iconStyle} />
                                    <input
                                        type={showPassword ? "text" : "password"}
                                        name="password"
                                        placeholder={t.password}
                                        value={formData.password}
                                        onChange={(e) => { handleChange(e); playSound('click'); }}
                                        required
                                        style={{ ...registerInputStyle, paddingRight: '48px' }}
                                    />
                                    <div
                                        onClick={() => { playSound('click'); setShowPassword(!showPassword); }}
                                        style={{ position: 'absolute', right: '16px', top: '50%', transform: 'translateY(-50%)', cursor: 'pointer', color: 'var(--text-secondary)', zIndex: 2 }}
                                    >
                                        {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                                    </div>
                                </div>
                                <div style={inputGroupStyle}>
                                    <Lock size={18} style={iconStyle} />
                                    <input
                                        type={showConfirmPassword ? "text" : "password"}
                                        name="password_confirmation"
                                        placeholder={t.confirmPassword}
                                        value={formData.password_confirmation}
                                        onChange={handleChange}
                                        required
                                        style={{ ...registerInputStyle, paddingRight: '48px' }}
                                    />
                                    <div
                                        onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                        style={{ position: 'absolute', right: '16px', top: '50%', transform: 'translateY(-50%)', cursor: 'pointer', color: 'var(--text-secondary)', zIndex: 2 }}
                                    >
                                        {showConfirmPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                                    </div>
                                </div>
                                <button type="button" onClick={nextStep} className="premium-button" style={{ width: '100%', padding: '16px', fontWeight: 700 }}>{t.next}</button>
                            </motion.div>
                        )}

                        {step === 2 && (
                            <motion.div
                                key="step2"
                                initial={{ opacity: 0, x: -20 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: 20 }}
                                style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}
                            >
                                <div style={inputGroupStyle}>
                                    <Phone size={18} style={iconStyle} />
                                    <input type="text" name="phone" placeholder={t.phone} value={formData.phone} onChange={handleChange} style={registerInputStyle} />
                                </div>
                                <div style={inputGroupStyle}>
                                    <Calendar size={18} style={iconStyle} />
                                    <input type="date" name="dob" placeholder={t.dob} value={formData.dob} onChange={handleChange} style={registerInputStyle} />
                                </div>
                                <div style={{ display: 'flex', gap: '1rem' }}>
                                    <select name="id_type" value={formData.id_type} onChange={handleChange} style={selectStyle}>
                                        {idTypes.map(t => <option key={t} value={t}>{t}</option>)}
                                    </select>
                                    <select name="id_country" value={formData.id_country} onChange={handleChange} style={selectStyle}>
                                        {countries.map(c => <option key={c} value={c}>{c}</option>)}
                                    </select>
                                </div>
                                <div style={inputGroupStyle}>
                                    <CreditCard size={18} style={iconStyle} />
                                    <input type="text" name="id_number" placeholder={t.idNumber} value={formData.id_number} onChange={handleChange} style={registerInputStyle} />
                                </div>
                                <div style={{ display: 'flex', gap: '1rem' }}>
                                    <button type="button" onClick={prevStep} style={backButtonStyle} disabled={loading}>{t.back}</button>
                                    <button type="submit" className="premium-button" style={{ flex: 1, padding: '16px', fontWeight: 700 }} disabled={loading}>
                                        {loading ? t.creating : t.register}
                                    </button>
                                </div>
                            </motion.div>
                        )}
                    </AnimatePresence>
                </form>

                <div style={{ marginTop: "30px", textAlign: "center", fontSize: "0.95rem", color: "var(--text-secondary)" }}>
                    {t.alreadyHave} <Link to="/login" onClick={() => playSound('click')} style={{ color: "var(--accent-blue)", textDecoration: "none", fontWeight: 700, marginLeft: '5px' }}>{t.login}</Link>
                </div>
            </motion.div>
        </div>
    );
};

const selectStyle = {
    flex: 1,
    padding: '12px',
    background: 'rgba(255,255,255,0.05)',
    border: '1px solid var(--glass-border)',
    borderRadius: '8px',
    color: '#fff'
};

const backButtonStyle = {
    flex: 1,
    background: 'rgba(255,255,255,0.1)',
    color: '#fff',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: 600
};

export default Register;


