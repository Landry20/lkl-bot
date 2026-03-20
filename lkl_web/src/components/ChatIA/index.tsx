import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Send, Loader2, CheckCheck, Sparkles } from 'lucide-react';
import { useSound } from '../../hooks/useSound';
import echo from '../../echo';

const API = "http://localhost:8000/api";

interface Message {
    id: string;
    text: string;
    sender: 'user' | 'bot';
    type: 'text' | 'image' | 'video';
    media_url?: string;
    timestamp: Date;
}

export default function ChatIA() {
    const [messages, setMessages] = useState<Message[]>([
        { id: '1', text: "Bonjour ! Je suis l'IA LKL. Comment puis-je vous aider dans votre trading aujourd'hui ?", sender: 'bot', type: 'text', timestamp: new Date() }
    ]);
    const [input, setInput] = useState('');
    const [isTyping, setIsTyping] = useState(false);
    const [file, setFile] = useState<File | null>(null);
    const { playSound } = useSound();
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    const fetchData = async () => {
        try {
            const token = localStorage.getItem('token');
            const res = await fetch(`${API}/chats`, {
                headers: { 'Authorization': `Bearer ${token}`, 'Accept': 'application/json' }
            });
            const data = await res.json();
            if (data.status === 'success') {
                const formatted = data.data.data.map((m: any) => ({
                    id: m.id.toString(),
                    text: m.message,
                    sender: m.sender,
                    type: m.type,
                    media_url: m.media_url,
                    timestamp: new Date(m.created_at)
                })).reverse();
                setMessages(formatted);
            }
        } catch (e) {
            console.error(e);
        }
    };

    useEffect(() => {
        fetchData();

        // Listen to Echo
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        if (user.id) {
            echo.private(`chat.${user.id}`)
                .listen('.MessageSent', (e: any) => {
                    const newMsg: Message = {
                        id: e.chat.id.toString(),
                        text: e.chat.message,
                        sender: e.chat.sender,
                        type: e.chat.type,
                        media_url: e.chat.media_url,
                        timestamp: new Date(e.chat.created_at)
                    };
                    setMessages((prev: Message[]) => {
                        if (prev.find(m => m.id === newMsg.id)) return prev;
                        if (newMsg.sender === 'bot') playSound('receive');
                        return [...prev, newMsg];
                    });
                    if (e.chat.sender === 'bot') {
                        setIsTyping(false);
                    }
                });
        }

        return () => {
            if (user.id) echo.leave(`chat.${user.id}`);
        };
    }, []);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isTyping]);

    const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
        }
    };

    const handleSend = async (customMsg?: string) => {
        const textToSend = customMsg || input;
        if (!textToSend.trim() && !file) return;

        // Optimistic UI
        const tempId = Date.now().toString();
        const optimisticMsg: Message = {
            id: tempId,
            text: textToSend,
            sender: 'user',
            type: file ? (file.type.startsWith('video') ? 'video' : 'image') : 'text',
            media_url: file ? URL.createObjectURL(file) : undefined,
            timestamp: new Date()
        };

        setMessages(prev => [...prev, optimisticMsg]);
        setInput('');
        setFile(null);
        setIsTyping(true);
        playSound('send');
        if (fileInputRef.current) fileInputRef.current.value = '';

        const token = localStorage.getItem('token');
        const user = JSON.parse(localStorage.getItem('user') || '{}');

        try {
            const formData = new FormData();
            formData.append('message', textToSend);
            formData.append('user_id', user.id);
            if (file) {
                formData.append('file', file);
            }

            const url = file
                ? `http://localhost:8001/api/chats/upload`
                : `http://localhost:8001/api/chats`;

            await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                    // Pas de Content-Type pour FormData, le navigateur le gère
                },
                body: file ? formData : JSON.stringify({ message: textToSend, user_id: user.id })
            });
        } catch (e) {
            console.error(e);
            setMessages(prev => prev.filter(m => m.id !== tempId));
            setIsTyping(false);
        }
    };

    return (
        <div className="glass-card messenger-container" style={{ height: '600px', display: 'flex', flexDirection: 'column', padding: 0, overflow: 'hidden' }}>
            {/* Header */}
            <div style={{ padding: '1rem 1.5rem', borderBottom: '1px solid var(--glass-border)', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div className="status-indicator"></div>
                <h3 style={{ margin: 0, fontSize: '1.1rem' }}>LKL Assistance IA</h3>
            </div>

            {/* Messages Area */}
            <div className="messages-area" style={{ flex: 1, padding: '1.5rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <AnimatePresence initial={false}>
                    {messages.map((m, index) => (
                        <motion.div
                            key={m.id}
                            initial={{ opacity: 0, y: 20, scale: 0.95 }}
                            animate={{ opacity: 1, y: 0, scale: 1 }}
                            exit={{ opacity: 0, scale: 0.9 }}
                            transition={{ duration: 0.3, ease: 'easeOut' }}
                            style={{
                                alignSelf: m.sender === 'user' ? 'flex-end' : 'flex-start',
                                maxWidth: '80%',
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: m.sender === 'user' ? 'flex-end' : 'flex-start'
                            }}
                        >
                            <motion.div
                                whileHover={{ scale: 1.02 }}
                                style={{
                                    padding: '0.8rem 1.2rem',
                                    borderRadius: m.sender === 'user' ? '18px 18px 2px 18px' : '18px 18px 18px 2px',
                                    background: m.sender === 'user' ? 'var(--accent-blue)' : 'rgba(255,255,255,0.05)',
                                    color: '#fff',
                                    fontSize: '0.95rem',
                                    lineHeight: '1.4',
                                    boxShadow: '0 4px 15px rgba(0,0,0,0.1)',
                                    position: 'relative'
                                }}
                            >
                                {m.type === 'text' && m.text}
                                {m.type === 'image' && <img src={m.media_url} alt="IA analysis" style={{ maxWidth: '100%', borderRadius: '8px', marginTop: '5px' }} />}
                                {m.type === 'video' && (
                                    <video controls style={{ maxWidth: '100%', borderRadius: '8px', marginTop: '5px' }}>
                                        <source src={m.media_url} type="video/mp4" />
                                    </video>
                                )}
                                {m.type !== 'text' && m.text && <p style={{ marginTop: '10px' }}>{m.text}</p>}

                                {m.sender === 'user' && (
                                    <motion.div
                                        initial={{ scale: 0 }}
                                        animate={{ scale: 1 }}
                                        transition={{ delay: 0.2 }}
                                        style={{ position: 'absolute', bottom: '5px', right: '8px', display: 'flex', gap: '2px', opacity: 0.7 }}
                                    >
                                        <CheckCheck size={12} color="#fff" />
                                    </motion.div>
                                )}
                            </motion.div>
                            <span style={{ fontSize: '0.7rem', opacity: 0.5, marginTop: '4px' }}>
                                {m.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                            </span>
                        </motion.div>
                    ))}
                </AnimatePresence>

                <AnimatePresence>
                    {isTyping && (
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -10 }}
                            transition={{ duration: 0.2 }}
                            style={{ alignSelf: 'flex-start', display: 'flex', alignItems: 'center', gap: '10px', padding: '0.5rem 1rem', background: 'rgba(255,255,255,0.03)', borderRadius: '15px' }}
                        >
                            <motion.div
                                animate={{ rotate: [0, 10, -10, 0] }}
                                transition={{ duration: 1, repeat: Infinity }}
                                style={{ fontSize: '1.2rem' }}
                            >
                                🤖
                            </motion.div>
                            <Sparkles size={16} className="spin" style={{ color: 'var(--accent-blue)' }} />
                            <span style={{ fontSize: '0.85rem', opacity: 0.7 }}>LKL analyse<motion.span animate={{ opacity: [0, 1, 0] }} transition={{ duration: 1.5, repeat: Infinity }}>...</motion.span></span>
                        </motion.div>
                    )}
                </AnimatePresence>
                <div ref={messagesEndRef} />
            </div>

            {/* Quick Replies */}
            {messages.length > 0 && messages[messages.length - 1].sender === 'bot' && !isTyping && (
                <div style={{ padding: '0 1.5rem 1rem 1.5rem', display: 'flex', gap: '10px', overflowX: 'auto' }}>
                    {['OK compris ! ✅', 'Parle-moi du Gold 🌟', 'À plus tard ! 👋'].map(reply => (
                        <button
                            key={reply}
                            onClick={() => handleSend(reply)}
                            style={{
                                padding: '6px 15px', fontSize: '0.8rem', whiteSpace: 'nowrap',
                                background: 'rgba(255,255,255,0.05)', border: '1px solid var(--glass-border)',
                                boxShadow: 'none'
                            }}
                        >
                            {reply}
                        </button>
                    ))}
                </div>
            )}

            {/* Input Area */}
            <div style={{ padding: '1.5rem', borderTop: '1px solid var(--glass-border)', background: 'rgba(0,0,0,0.2)' }}>
                {file && (
                    <div className="glass-card" style={{ padding: '8px 15px', marginBottom: '10px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                        <span style={{ fontSize: '0.85rem' }}>📎 {file.name}</span>
                        <button onClick={() => setFile(null)} style={{ background: 'none', border: 'none', color: '#ef4444', cursor: 'pointer' }}>✕</button>
                    </div>
                )}
                <div style={{ position: 'relative', display: 'flex', gap: '10px' }}>
                    <input
                        type="file"
                        ref={fileInputRef}
                        onChange={handleFileSelect}
                        accept="image/*,video/*"
                        style={{ display: 'none' }}
                    />
                    <button
                        onClick={() => fileInputRef.current?.click()}
                        style={{
                            background: 'rgba(255,255,255,0.1)',
                            border: '1px solid var(--glass-border)',
                            color: '#fff',
                            borderRadius: '12px',
                            cursor: 'pointer',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            width: '45px'
                        }}
                        title="Envoyer une image ou vidéo"
                    >
                        📎
                    </button>
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                        placeholder="Posez une question ou envoyez un graphique..."
                        style={{
                            flex: 1,
                            padding: '0.8rem 1.2rem',
                            borderRadius: '12px',
                            background: 'rgba(255,255,255,0.05)',
                            border: '1px solid var(--glass-border)',
                            color: '#fff',
                            outline: 'none'
                        }}
                    />
                    <button
                        onClick={() => handleSend()}
                        className="premium-button"
                        style={{
                            padding: '0.8rem',
                            borderRadius: '12px',
                            background: 'var(--accent-blue)',
                            border: 'none',
                            cursor: 'pointer',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center'
                        }}
                    >
                    <Send size={20} />
                </button>
            </div>
        </div>
        </div >
    );
}
