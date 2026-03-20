import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Play, Square, Activity, TrendingUp, DollarSign, CheckCircle, AlertTriangle, User } from 'lucide-react';
import { getAnalyses, getTrades, getSettings, updateSettings, getCurrentUser } from "../api";
import { useSound } from "../hooks/useSound";
import echo from "../echo";

export default function Dashboard() {
  const [trades, setTrades] = useState<any[]>([]);
  const [settings, setSettings] = useState<any>({});
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [isActivating, setIsActivating] = useState(false);
  const [isToggling, setIsToggling] = useState(false);
  const [lastSync, setLastSync] = useState<string>("");
  const { playSound } = useSound();

  const botIdentity = {
    name: localStorage.getItem('bot_name') || 'LKLBot',
    image: localStorage.getItem('bot_image') || '/assets/bot_profile_default.png'
  };

  const fetchData = async (isFirst = false) => {
    if (isFirst) setLoading(true);
    try {
      const [, tradesData, settingsData, userData] = await Promise.all([
        getAnalyses(),
        getTrades(),
        getSettings(),
        getCurrentUser()
      ]);
      setTrades(tradesData.data || []);
      setSettings(settingsData || {});
      setUser(userData);
      setLastSync(new Date().toLocaleTimeString());
    } catch (e) {
      console.error("Fetch Data Error", e);
    } finally {
      if (isFirst) setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(true);
    const interval = setInterval(() => fetchData(false), 60000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const handleTradeUpdate = (e: any) => {
      setTrades(prev => [e.trade, ...prev.slice(0, 19)]);
    };
    echo.channel('trades').listen('TradeUpdated', handleTradeUpdate);

    // Listen to bot status changes via WebSocket
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    if (user.id) {
      echo.channel(`stats.${user.id}`).listen('StatsUpdated', (e: any) => {
        if (e.stats.bot_running !== undefined) {
          setSettings((prev: any) => ({ ...prev, bot_running: e.stats.bot_running }));
          setIsToggling(false);
          setLastSync(new Date().toLocaleTimeString());
        }
      });
    }

    return () => {
      echo.leave('trades');
      if (user.id) echo.leave(`stats.${user.id}`);
    };
  }, []);

  const handleToggleBot = async () => {
    const currentState = settings.bot_running || '0';
    const newState = currentState === '1' ? '0' : '1';

    setIsToggling(true);
    try {
      playSound('click');
      if (newState === '1') {
        setIsActivating(true);
        setTimeout(() => setIsActivating(false), 5000);
      }

      await updateSettings({ bot_running: newState });
      setSettings((prev: any) => ({ ...prev, bot_running: newState }));

      window.dispatchEvent(new CustomEvent('add-toast', {
        detail: {
          message: newState === '1' ? 'Robot démarré avec succès !' : 'Le robot a bien été arrêté.',
          type: newState === '1' ? 'success' : 'info'
        }
      }));
    } catch (error: any) {
      console.error("Toggle Bot Error:", error);
      setIsActivating(false);
      window.dispatchEvent(new CustomEvent('add-toast', {
        detail: {
          message: `Échec de l'action : ${error.message || 'Serveur injoignable'}`,
          type: 'error'
        }
      }));
    } finally {
      setIsToggling(false);
    }
  };

  if (loading) {
    return <div className="flex-center" style={{ height: '80vh' }}>Chargement du centre de pilotage...</div>;
  }

  const isBotActive = settings.bot_running === '1';
  const isMt5Connected = !!user?.mt5_login;

  const globalProfit = trades.reduce((acc, t) => acc + (parseFloat(t.profit) || 0), 0).toFixed(2);
  const winRateValue = trades.length > 0 ? (trades.filter(t => parseFloat(t.profit) > 0).length / trades.length * 100).toFixed(1) : "0";

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto' }}>

      {/* Bot Activation Overlay */}
      <AnimatePresence>
        {isActivating && (
          <motion.div
            key="activation-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            style={{
              position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
              zIndex: 10000, display: 'flex', alignItems: 'center', justifyContent: 'center',
              background: 'rgba(5, 8, 15, 0.8)', backdropFilter: 'blur(8px)', padding: '20px'
            }}
          >
            <motion.div
              initial={{ scale: 0.8, y: 20 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.8, y: 20 }}
              style={{
                border: '2px solid var(--accent-blue)', borderRadius: '32px',
                padding: '60px 40px', textAlign: 'center', background: 'var(--bg-dark)',
                maxWidth: '500px', width: '100%', boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)'
              }}
            >
              <div className="status-indicator" style={{ width: '40px', height: '40px', margin: '0 auto 30px' }}></div>
              <h2 className="premium-gradient-text" style={{ fontSize: '2.5rem', fontWeight: 900, marginBottom: '20px' }}>
                {botIdentity.name.toUpperCase()} ACTIVÉ !
              </h2>
              <p style={{ fontSize: '1.3rem', opacity: 0.9, lineHeight: 1.5 }}>
                🚀 Je commence l'analyse des marchés immédiatement. ✨💎
              </p>
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 4, repeat: Infinity, ease: 'linear' }}
                style={{ marginTop: '40px', fontSize: '2rem' }}
              >
                ⚙️
              </motion.div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '10px' }}>
        <div style={{ fontSize: '0.85rem', opacity: 0.6, display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Activity size={14} className={loading ? "spin" : ""} />
          Dernière mise à jour : {lastSync || "--:--:--"}
        </div>
      </div>

      <div id="dashboard-content-main">
        {/* Hero Control Section */}
        <section className="glass-card snap-bounce" style={{
          padding: '40px', borderRadius: '30px', marginBottom: '30px',
          border: isBotActive ? '2px solid var(--accent-blue)' : '1px solid var(--glass-border)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '30px' }}>
              <div style={{
                width: '120px', height: '120px', borderRadius: '25%', overflow: 'hidden',
                border: '3px solid var(--accent-blue)', boxShadow: '0 10px 30px rgba(0,124,240,0.3)'
              }}>
                <img
                  src={botIdentity.image}
                  onError={(e: any) => e.target.src = "/assets/bot_profile_default.png"}
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              </div>
              <div>
                <h1 style={{ fontSize: '2.5rem', margin: 0 }}>{botIdentity.name}</h1>
                <p style={{ opacity: 0.7, fontSize: '1.1rem' }}>
                  {isBotActive ? "⚡ Surveillance active du marché" : "💤 Robot en mode veille"}
                </p>
                {isMt5Connected && (
                  <div style={{ marginTop: '10px', display: 'flex', alignItems: 'center', gap: '8px', color: '#10b981', fontSize: '0.9rem', fontWeight: 600 }}>
                    <User size={16} /> {user.mt5_name || "Compte lié"} ({user.mt5_login})
                  </div>
                )}
              </div>
            </div>

            <button
              onClick={handleToggleBot}
              disabled={isToggling}
              className={isBotActive ? "danger-button" : "premium-button"}
              style={{
                padding: '20px 50px', fontSize: '1.2rem', fontWeight: 800, borderRadius: '20px',
                minWidth: '280px', position: 'relative', opacity: isToggling ? 0.8 : 1
              }}
            >
              {isToggling ? (
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <motion.div
                    animate={{ rotate: 360 }}
                    transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                  >
                    ⚙️
                  </motion.div>
                  TRAITEMENT...
                </div>
              ) : (
                isBotActive ? (
                  <span style={{ display: 'flex', alignItems: 'center' }}>
                    <Square size={20} style={{ marginRight: 10 }} /> ARRÊTER LE ROBOT
                  </span>
                ) : (
                  <span style={{ display: 'flex', alignItems: 'center' }}>
                    <Play size={20} style={{ marginRight: 10 }} /> DÉMARRER LE ROBOT
                  </span>
                )
              )}
            </button>
          </div>
        </section>

        {/* KPI Cloud */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '25px', marginBottom: '30px' }}>
          {[
            { label: "Solde de Compte", val: isMt5Connected ? `$${parseFloat(user.mt5_balance || 0).toLocaleString()}` : "---", icon: <DollarSign color="var(--accent-blue)" /> },
            { label: "Equity (Nette)", val: isMt5Connected ? `$${parseFloat(user.mt5_equity || 0).toLocaleString()}` : "---", icon: <TrendingUp color="#10b981" /> },
            { label: "Profit Global (Trades)", val: isMt5Connected ? `${globalProfit} $` : "---", icon: <Activity color="#8b5cf6" /> },
            { label: "Win Rate", val: isMt5Connected ? `${winRateValue}%` : "---", icon: <CheckCircle color="#f59e0b" /> }
          ].map((kpi) => (
            <div key={kpi.label} className="glass-card" style={{ padding: '25px', borderRadius: '20px', textAlign: 'center' }}>
              <div style={{ opacity: 0.6, fontSize: '0.9rem', marginBottom: '10px' }}>{kpi.label}</div>
              <div style={{ fontSize: '1.8rem', fontWeight: 900, marginBottom: '10px' }}>{kpi.val}</div>
              <div style={{ display: 'flex', justifyContent: 'center' }}>{kpi.icon}</div>
            </div>
          ))}
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '30px' }}>
          {/* Real-time Executions */}
          <div className="glass-card" style={{ padding: '25px', borderRadius: '24px' }}>
            <h3 style={{ marginBottom: '20px' }}>Dernières Exécutions Réelles</h3>
            {trades.length > 0 ? (
              <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr style={{ opacity: 0.5, fontSize: '0.8rem', textAlign: 'left' }}>
                    <th style={{ padding: '10px' }}>SYMBOLE</th>
                    <th>TYPE</th>
                    <th>LOTS</th>
                    <th>PROFIT</th>
                    <th>STATUS</th>
                  </tr>
                </thead>
                <tbody>
                  {trades.slice(0, 8).map(t => (
                    <tr key={t.id} style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                      <td style={{ padding: '15px 10px', opacity: 0.7, fontSize: '0.9rem' }}>
                        {new Date(t.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                      </td>
                      <td style={{ fontWeight: 700 }}>{t.symbol}</td>
                      <td style={{ color: t.type === 'buy' ? '#10b981' : '#ef4444', fontWeight: 600 }}>{t.type.toUpperCase()}</td>
                      <td>{t.lots}</td>
                      <td style={{ fontWeight: 700, color: (parseFloat(t.profit) >= 0) ? '#10b981' : '#ef4444' }}>
                        {parseFloat(t.profit) > 0 ? `+${t.profit}` : t.profit}$
                      </td>
                      <td>{t.status === 'closed' ? <span style={{ padding: '4px 8px', background: 'rgba(16,185,129,0.1)', color: '#10b981', borderRadius: '6px', fontSize: '0.7rem' }}>CLÔTURÉ</span> : "ACTIF"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div style={{ textAlign: 'center', padding: '40px', opacity: 0.5 }}>Aucun trade enregistré pour ce compte.</div>
            )}
          </div>

          {/* System Status */}
          <div className="glass-card" style={{ padding: '25px', borderRadius: '24px' }}>
            <h3 style={{ marginBottom: '20px' }}>État du Système</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <div style={{ padding: '15px', background: 'rgba(255,255,255,0.03)', borderRadius: '15px', display: 'flex', alignItems: 'center', gap: '15px' }}>
                <CheckCircle color="#10b981" />
                <div>
                  <div style={{ fontWeight: 600 }}>IA & Moteur d'Analyse</div>
                  <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>Prêt pour l'exécution</div>
                </div>
              </div>
              <div style={{ padding: '15px', background: 'rgba(255,255,255,0.03)', borderRadius: '15px', display: 'flex', alignItems: 'center', gap: '15px' }}>
                <div className="status-indicator" style={{ background: isMt5Connected ? '#10b981' : '#ef4444' }}></div>
                <div>
                  <div style={{ fontWeight: 600 }}>Connexion MT5</div>
                  <div style={{ fontSize: '0.8rem', opacity: 0.5 }}>{isMt5Connected ? "Liaison établie" : "Non configurée"}</div>
                </div>
              </div>
              {!isBotActive && (
                <div style={{ padding: '15px', background: 'rgba(245,158,11,0.1)', border: '1px solid #f59e0b', borderRadius: '15px', display: 'flex', alignItems: 'center', gap: '15px' }}>
                  <AlertTriangle color="#f59e0b" />
                  <div style={{ color: '#f59e0b' }}>
                    <div style={{ fontWeight: 600 }}>Robot en Pause</div>
                    <div style={{ fontSize: '0.8rem' }}>En attente d'ordres...</div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
