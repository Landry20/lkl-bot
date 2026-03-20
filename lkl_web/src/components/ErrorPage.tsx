import { motion } from "framer-motion";

interface ErrorPageProps {
    status: number;
    message: string;
    onRetry: () => void;
}

export default function ErrorPage({ status, message, onRetry }: ErrorPageProps) {
    return (
        <div style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "radial-gradient(circle at center, #2d0a0a 0%, #0a0000 100%)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 9999,
            padding: "20px"
        }}>
            <motion.div
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                style={{
                    maxWidth: "500px",
                    width: "100%",
                    padding: "50px",
                    textAlign: "center",
                    border: "2px solid #ef4444",
                    backgroundColor: "rgba(0, 0, 0, 0.8)",
                    borderRadius: "32px",
                    boxShadow: "0 0 50px rgba(239, 68, 68, 0.3)"
                }}
            >
                <div style={{ fontSize: "5rem", marginBottom: "20px" }}>⚠️</div>
                <h1 style={{ color: "#ef4444", fontSize: "2.5rem", marginBottom: "10px" }}>ERREUR SYSTÈME</h1>
                <p style={{ color: "#94a3b8", fontSize: "1.1rem", marginBottom: "30px", lineHeight: "1.6" }}>
                    Un problème critique est survenu lors de la communication avec le serveur (Code: {status || 'ERR'}).
                    L'accès au terminal est temporairement suspendu.
                </p>

                <div className="glass-card" style={{
                    background: "rgba(239, 68, 68, 0.1)",
                    border: "1px dashed #ef4444",
                    marginBottom: "30px",
                    padding: "15px",
                    fontSize: "0.9rem",
                    color: "#fecaca"
                }}>
                    {message}
                </div>

                <button
                    onClick={onRetry}
                    style={{
                        width: "100%",
                        background: "#ef4444",
                        padding: "20px",
                        fontSize: "1.2rem",
                        fontWeight: "bold",
                        boxShadow: "0 0 20px rgba(239, 68, 68, 0.5)"
                    }}
                >
                    ACTUALISER ET RÉESSAYER
                </button>

                <p style={{ marginTop: "20px", color: "var(--text-secondary)", fontSize: "0.8rem" }}>
                    Si le problème persiste, veuillez contacter le support technique LKL.
                </p>
            </motion.div>
        </div>
    );
}
