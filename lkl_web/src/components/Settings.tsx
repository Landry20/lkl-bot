import { useState, useEffect } from "react";
import { Lock, RefreshCcw, Bot, Calendar } from 'lucide-react';
import { getSettings, updateSettings, getCurrentUser, updateUserMt5, getMt5Accounts, updateTradingSettings } from "../api";
import { useSound } from "../hooks/useSound";

export default function Settings() {
    const [settings, setSettings] = useState<any>({});
    const [loading, setLoading] = useState(true);
    const [mt5Data, setMt5Data] = useState({
        mt5_broker: '',
        mt5_server: '',
        mt5_login: '',
        mt5_password: ''
    });
    const [isLocked, setIsLocked] = useState(false);
    const [updatingMt5, setUpdatingMt5] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [user, setUser] = useState<any>(null);
    const [botIdentity, setBotIdentity] = useState({
        name: localStorage.getItem('bot_name') || 'LKLBot',
        image: localStorage.getItem('bot_image') || '/assets/bot_profile_default.png'
    });
    const { playSound } = useSound();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [s, u] = await Promise.all([
                    getSettings(),
                    getCurrentUser(),
                    getMt5Accounts()
                ]);
                setSettings(s || {});
                setUser(u);

                if (u.mt5_login) {
                    setIsLocked(true);
                    setMt5Data({
                        mt5_broker: u.mt5_broker || '',
                        mt5_server: u.mt5_server || '',
                        mt5_login: u.mt5_login || '',
                        mt5_password: ''
                    });
                }
            } catch (e) {
                console.error(e);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const handleUpdateMt5 = async (e: React.FormEvent) => {
        e.preventDefault();
        setUpdatingMt5(true);
        try {
            const res = await updateUserMt5(mt5Data);
            setUser(res.user);
            setIsLocked(true);
            window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: "Compte MT5 mis à jour !", type: 'success' } }));
        } catch (e) { console.error(e); }
        finally { setUpdatingMt5(false); }
    };

    const handleToggleTradingAuth = async () => {
        const newState = !user?.trading_authorized;
        try {
            const res = await updateTradingSettings({ trading_authorized: newState });
            setUser(res.user);
            window.dispatchEvent(new CustomEvent('add-toast', {
                detail: { message: newState ? "Trading Autorisé ✅" : "Trading Révoqué 🛑", type: 'success' }
            }));
        } catch (e) {
            console.error(e);
        }
    };

    const handleResetBotIdentity = () => {
        setBotIdentity({ name: 'LKLBot', image: '/assets/bot_profile_default.png' });
        localStorage.setItem('bot_name', 'LKLBot');
        localStorage.setItem('bot_image', '/assets/bot_profile_default.png');
        window.dispatchEvent(new CustomEvent('add-toast', { detail: { message: "Identité réinitialisée ✨", type: 'info' } }));
    };

    const dayNames = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"];
    const workDays = JSON.parse(settings.work_days || "[0,1,2,3,4]");

    const handleToggleDay = async (dayIdx: number) => {
        let newDays = [...workDays];
        if (newDays.includes(dayIdx)) newDays = newDays.filter(d => d !== dayIdx);
        else newDays.push(dayIdx);
        const sorted = newDays.sort();
        await updateSettings({ work_days: JSON.stringify(sorted) });
        setSettings({ ...settings, work_days: JSON.stringify(sorted) });
    };

    if (loading) return <div className="flex-center" style={{ height: '60vh' }}>Chargement des réglages...</div>;

    return (
        <div style={{ padding: '20px', maxWidth: '1000px', margin: '0 auto' }}>
            <h1 className="premium-gradient-text" style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '2rem' }}>⚙️ Paramètres Système</h1>

            <div style={{ display: 'grid', gap: '30px' }}>

                {/* 1. CONFIGURATION MT5 */}
                <section className="glass-card">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                        <h2 style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '1.2rem' }}><Lock size={20} /> Compte Trading (MT5)</h2>
                        {user?.mt5_login && (
                            <button onClick={() => setIsLocked(!isLocked)} className="premium-button" style={{ padding: '5px 15px', fontSize: '0.8rem' }}>
                                {isLocked ? <><RefreshCcw size={14} style={{ marginRight: 5 }} /> CHANGER DE COMPTE</> : "RETOUR AUX DÉTAILS"}
                            </button>
                        )}
                    </div>

                    {isLocked && user?.mt5_login ? (
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', padding: '20px', background: 'rgba(255,255,255,0.02)', borderRadius: '15px' }}>
                            <div>
                                <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>Broker</div>
                                <div style={{ fontWeight: 700, fontSize: '1.1rem' }}>{user.mt5_broker}</div>
                            </div>
                            <div>
                                <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>Serveur</div>
                                <div style={{ fontWeight: 700, fontSize: '1.1rem' }}>{user.mt5_server}</div>
                            </div>
                            <div>
                                <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>Login ID</div>
                                <div style={{ fontWeight: 700, fontSize: '1.1rem' }}>{user.mt5_login}</div>
                            </div>
                            <div>
                                <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>Statut Connexion</div>
                                <div style={{ color: '#10b981', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <span className="status-indicator"></span> CONNECTÉ
                                </div>
                            </div>
                        </div>
                    ) : (
                        <form onSubmit={handleUpdateMt5} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
                            <div style={{ gridColumn: 'span 2', paddingBottom: '10px', opacity: 0.7, fontSize: '0.9rem' }}>
                                Entrez vos identifiants Metatrader 5 pour relier le robot à votre capital.
                            </div>
                            <div>
                                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Broker</label>
                                <input type="text" value={mt5Data.mt5_broker} onChange={(e) => setMt5Data({ ...mt5Data, mt5_broker: e.target.value })} placeholder="Ex: IC Markets" />
                            </div>
                            <div>
                                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Serveur</label>
                                <input type="text" value={mt5Data.mt5_server} onChange={(e) => setMt5Data({ ...mt5Data, mt5_server: e.target.value })} placeholder="Ex: Live-01" />
                            </div>
                            <div>
                                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Login (MT5)</label>
                                <input type="text" value={mt5Data.mt5_login} onChange={(e) => setMt5Data({ ...mt5Data, mt5_login: e.target.value })} placeholder="Numéro de compte" />
                            </div>
                            <div style={{ position: 'relative' }}>
                                <label style={{ fontSize: '0.8rem', opacity: 0.7 }}>Mot de passe</label>
                                <input type={showPassword ? "text" : "password"} value={mt5Data.mt5_password} onChange={(e) => setMt5Data({ ...mt5Data, mt5_password: e.target.value })} placeholder="••••••••" />
                            </div>
                            <button type="submit" disabled={updatingMt5} className="premium-button" style={{ gridColumn: 'span 2', padding: '15px' }}>
                                {updatingMt5 ? "CONNEXION EN COURS..." : "LIER LE COMPTE MT5"}
                            </button>
                        </form>
                    )}

                    {/* Autorisation Trader Section */}
                    <div style={{ marginTop: '30px', paddingTop: '20px', borderTop: '1px solid rgba(255,255,255,0.1)' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div>
                                <h3 style={{ margin: 0, fontSize: '1rem' }}>Autorisation de Trading IA</h3>
                                <p style={{ fontSize: '0.8rem', opacity: 0.6, margin: '5px 0 0 0' }}>Permettre à l'IA d'ouvrir des ordres sur votre compte MT5.</p>
                            </div>
                            <button
                                onClick={handleToggleTradingAuth}
                                className={user?.trading_authorized ? "danger-button" : "premium-button"}
                                style={{ padding: '10px 20px', borderRadius: '10px' }}
                            >
                                {user?.trading_authorized ? "RÉVOQUER L'IA" : "AUTORISER L'IA"}
                            </button>
                        </div>
                    </div>
                </section>

                {/* 2. IDENTITÉ DU BOT */}
                <section className="glass-card">
                    <h2 style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '1.2rem', marginBottom: '20px' }}><Bot size={20} /> Identité du Robot</h2>
                    <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '30px', alignItems: 'center' }}>
                        <div style={{ width: 120, height: 120, borderRadius: '20px', border: '2px solid var(--accent-blue)', overflow: 'hidden' }}>
                            <img
                                src={botIdentity.image}
                                onError={(e: any) => e.target.src = "/assets/bot_profile_default.png"}
                                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                            />
                        </div>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                            <input
                                type="text"
                                value={botIdentity.name}
                                onChange={(e) => {
                                    setBotIdentity({ ...botIdentity, name: e.target.value });
                                    localStorage.setItem('bot_name', e.target.value);
                                }}
                                placeholder="Nom du bot"
                            />
                            <button onClick={handleResetBotIdentity} style={{ background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', border: '1px solid #ef4444', padding: '10px' }}>
                                RÉINITIALISER
                            </button>
                        </div>
                    </div>
                </section>

                {/* 3. CALENDRIER DE TRAVAIL */}
                <section className="glass-card">
                    <h2 style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '1.2rem', marginBottom: '20px' }}><Calendar size={20} /> Calendrier de Travail</h2>
                    <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                        {dayNames.map((day, idx) => (
                            <div
                                key={idx}
                                onClick={() => handleToggleDay(idx)}
                                style={{
                                    flex: 1, padding: '15px', borderRadius: '12px', textAlign: 'center', cursor: 'pointer',
                                    background: workDays.includes(idx) ? 'var(--accent-blue)' : 'rgba(255,255,255,0.05)',
                                    border: '1px solid var(--glass-border)', transition: 'all 0.3s'
                                }}
                            >
                                <div style={{ fontWeight: 700 }}>{day}</div>
                                <div style={{ fontSize: '0.7rem', opacity: 0.6 }}>{workDays.includes(idx) ? "ACTIF" : "OFF"}</div>
                            </div>
                        ))}
                    </div>
                </section>

            </div>
        </div>
    );
}
