import { useNavigate, useLocation, Link, Outlet } from "react-router-dom";
import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { getNotifications, getUnreadCount, markAsRead } from "../api";
import { BrainCircuit } from "lucide-react";
import ErrorOverlay from "./ErrorOverlay";

const LivingRobot = () => (
    <motion.div
        animate={{
            y: [0, -5, 0],
            scale: [1, 1.02, 1],
            rotate: [0, 1, -1, 0]
        }}
        transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
        style={{
            width: '80px', height: '80px', margin: '0 auto 20px',
            background: 'linear-gradient(135deg, var(--accent-blue), #10b981)',
            borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: '0 0 20px rgba(0, 124, 240, 0.3)',
            border: '2px solid rgba(255,255,255,0.2)'
        }}
    >
        <BrainCircuit size={40} color="white" />
        <motion.div
            animate={{ opacity: [0.3, 1, 0.3] }}
            transition={{ duration: 2, repeat: Infinity }}
            style={{ position: 'absolute', top: '10px', right: '10px', width: '8px', height: '8px', background: '#10b981', borderRadius: '50%' }}
        />
    </motion.div>
);

export default function MainLayout() {
    const navigate = useNavigate();
    const location = useLocation();
    const [userName, setUserName] = useState("Utilisateur");
    const [showNotifications, setShowNotifications] = useState(false);
    const [notifications, setNotifications] = useState<any[]>([]);
    const [unreadCount, setUnreadCount] = useState(0);
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

    const fetchNotifications = async () => {
        try {
            const data = await getNotifications();
            setNotifications(data.data || []);
            const count = await getUnreadCount();
            setUnreadCount(count.count || 0);
        } catch (e) {
            console.error(e);
        }
    };

    const handleMarkasRead = async (id: number) => {
        try {
            await markAsRead(id);
            setNotifications(notifications.map(n => n.id === id ? { ...n, read_at: new Date() } : n));
            setUnreadCount(prev => Math.max(0, prev - 1));
        } catch (e) {
            console.error(e);
        }
    };

    useEffect(() => {
        const userStr = localStorage.getItem("user");
        if (userStr) {
            const user = JSON.parse(userStr);
            setUserName(user.name || "Trader");
        }

        if (!localStorage.getItem("token")) {
            navigate("/login");
        } else {
            getUnreadCount().then(res => setUnreadCount(res.count || 0)).catch(console.error);
            const interval = setInterval(fetchNotifications, 15000);
            return () => clearInterval(interval);
        }
    }, [navigate]);

    const handleLogout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        navigate("/login");
    };

    const menuItems = [
        { name: "Dashboard", path: "/", icon: "📊" },
        { name: "Chat IA", path: "/chat-ia", icon: "🤖" },
        { name: "Annonces", path: "/announce", icon: "📰" },
        { name: "Occasions", path: "/occasions", icon: "🎯" },
        { name: "Graphiques", path: "/trading-terminal", icon: "📈" },
        { name: "Paramètres", path: "/settings", icon: "⚙️" },
        { name: "Archives", path: "/archives", icon: "📁" },
    ];

    return (
        <div style={{
            display: "flex", // Flex box simpler alternative to grid for height issues
            height: "100vh",
            background: "var(--bg-dark)",
            overflow: "hidden"
        }}>
            <ErrorOverlay />
            {/* Sidebar */}
            <aside className={`glass-card ${mobileMenuOpen ? 'mobile-open' : ''}`} style={{
                width: "280px",
                margin: "20px",
                borderRadius: "24px",
                display: "flex",
                flexDirection: "column",
                padding: "30px 20px",
                height: "calc(100vh - 40px)",
                flexShrink: 0,
                zIndex: 1000,
                transition: 'transform 0.3s ease'
            }}>
                <div style={{ textAlign: "center", marginBottom: "40px" }}>
                    <LivingRobot />
                    <h2 className="premium-gradient-text" style={{ fontSize: "1.5rem", marginTop: "10px" }}>LKL PANEL</h2>
                </div>

                <nav style={{ flex: 1, display: "flex", flexDirection: "column", gap: "10px", overflowY: "auto" }}>
                    {menuItems.map(item => (
                        <Link
                            key={item.path}
                            to={item.path}
                            onClick={() => setMobileMenuOpen(false)}
                            className={location.pathname === item.path ? "active-nav-item" : "nav-item"}
                            style={{
                                display: "flex", alignItems: "center", gap: "15px", padding: "15px 20px",
                                borderRadius: "15px", textDecoration: "none", color: "white", transition: "all 0.3s",
                                background: location.pathname === item.path ? "var(--accent-blue)" : "transparent"
                            }}
                        >
                            <span style={{ fontSize: "1.2rem" }}>{item.icon}</span>
                            <span style={{ fontWeight: 600 }}>{item.name}</span>
                        </Link>
                    ))}
                </nav>

                <button
                    onClick={handleLogout}
                    style={{
                        marginTop: "20px", background: "rgba(239, 68, 68, 0.1)", color: "#ef4444", border: "1px solid rgba(239, 68, 68, 0.2)"
                    }}
                >
                    Se déconnecter
                </button>
            </aside>

            {/* Main Content Area */}
            <main style={{
                flex: 1,
                padding: "20px",
                display: "flex",
                flexDirection: "column",
                gap: "20px",
                height: "100vh",
                overflowY: "auto",
                position: "relative"
            }}>
                {/* Topbar */}
                <header className="glass-card" style={{
                    padding: "15px 30px",
                    borderRadius: "20px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    position: "sticky",
                    top: 0,
                    zIndex: 100,
                    marginBottom: "10px",
                    flexShrink: 0
                }}>
                    <div style={{ display: "flex", alignItems: "center", gap: "15px" }}>
                        <div className="status-indicator"></div>
                        <div>
                            <div style={{ fontSize: "0.8rem", color: "var(--text-secondary)" }}>Bienvenue,</div>
                            <div style={{ fontWeight: 700, fontSize: "1.1rem" }}>{userName}</div>
                        </div>
                    </div>

                    <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
                        <button
                            onClick={() => window.location.reload()}
                            style={{ background: "rgba(255,255,255,0.05)", padding: "10px", width: "45px", height: "45px", borderRadius: "12px", border: 'none', color: 'white', cursor: 'pointer' }}
                        >
                            🔄
                        </button>

                        <div style={{ position: "relative" }}>
                            <button
                                onClick={() => {
                                    setShowNotifications(!showNotifications);
                                    if (!showNotifications) fetchNotifications();
                                }}
                                style={{ background: "rgba(255,255,255,0.05)", padding: "10px", width: "45px", height: "45px", borderRadius: "12px", cursor: 'pointer', border: 'none', color: 'white' }}
                            >
                                🔔
                            </button>
                            {unreadCount > 0 && (
                                <div style={{
                                    position: "absolute", top: "-5px", right: "-5px", background: "#ef4444", color: "white",
                                    fontSize: "0.7rem", padding: "2px 6px", borderRadius: "10px", border: "2px solid var(--bg-dark)"
                                }}>{unreadCount}</div>
                            )}

                            <AnimatePresence>
                                {showNotifications && (
                                    <motion.div
                                        initial={{ opacity: 0, y: 10, scale: 0.95 }}
                                        animate={{ opacity: 1, y: 0, scale: 1 }}
                                        exit={{ opacity: 0, y: 10, scale: 0.95 }}
                                        className="glass-card"
                                        style={{
                                            position: "absolute", top: "60px", right: 0, width: "380px", maxHeight: "500px",
                                            overflowY: "auto", padding: "0", zIndex: 1000, background: "#1e293b",
                                            boxShadow: "0 10px 40px rgba(0,0,0,0.5)", border: "1px solid rgba(255,255,255,0.1)"
                                        }}
                                    >
                                        <div style={{ padding: "15px", borderBottom: "1px solid rgba(255,255,255,0.1)", display: "flex", justifyContent: "space-between", alignItems: "center", background: 'rgba(0,0,0,0.2)' }}>
                                            <h4 style={{ margin: 0, fontSize: '1rem' }}>Notifications</h4>
                                        </div>

                                        {notifications.length === 0 ? (
                                            <div style={{ padding: "30px", textAlign: "center", color: "var(--text-secondary)" }}>
                                                Aucune notification
                                            </div>
                                        ) : (
                                            notifications.map((notif: any) => (
                                                <div key={notif.id} onClick={() => handleMarkasRead(notif.id)} style={{ padding: "15px", borderBottom: "1px solid rgba(255,255,255,0.05)", cursor: "pointer" }}>
                                                    <div style={{ fontSize: "0.9rem", color: notif.read_at ? "#94a3b8" : "#fff" }}>
                                                        {typeof notif.data === 'string' ? JSON.parse(notif.data).message : notif.data?.message}
                                                    </div>
                                                </div>
                                            ))
                                        )}
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </div>
                    </div>
                </header>

                {/* Page Content */}
                <div style={{ flex: 1 }}>
                    <Outlet />
                </div>
            </main>
        </div>
    );
}
