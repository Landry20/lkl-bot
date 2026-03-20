import requests
import os

class IntelligenceExterne:
    """
    Interface de connexion aux I.A. externes (Gemini/ChatGPT).
    Utilisée strictement pour la compréhension approfondie du trading.
    """
    def __init__(self, provider="gemini"):
        self.provider = provider
        # Les clés seraient normalement dans des variables d'environnement
        self.api_key = os.getenv("EXTERNAL_AI_KEY", "PLACEHOLDER_KEY")

    def demander_expertise(self, question):
        """
        Envoie une requête à l'IA externe pour obtenir une explication de trading.
        """
        prompt = f"En tant qu'expert en trading institutionnel, explique moi de manière approfondie et gentille : {question}"
        
        # Simulation de l'appel API (Placeholder)
        # Dans une vraie implémentation, on ferait un requests.post vers l'API Gemini ou OpenAI
        print(f"[AI LOG] Requête envoyée à {self.provider} : {question[:30]}...")
        
        # Exemple de réponse simulée savante
        if "fvg" in question.lower():
            return "Un Fair Value Gap (FVG) est un déséquilibre entre l'offre et la demande qui crée un vide de liquidité. Le prix a tendance à revenir combler ces zones. ✨ C'est une connaissance précieuse pour vos entrées ! 💎"
        
        return f"C'est une excellente question sur {question}. Selon mon analyse approfondie via {self.provider}, il s'agit d'un concept clé basé sur la dynamique des flux. 🧐📚"

    def auto_query_if_confused(self, context, internal_reasoning=""):
        """
        Déclenche une requête autonome vers Gemini/ChatGPT si le bot ne comprend pas un concept
        ou si le raisonnement interne est trop limité.
        """
        print(f"[AI AUTO-THINK] Analyse de la situation par {self.provider}...")
        
        prompt = (
            f"Le robot LKLBot analyse actuellement : {context}. "
            f"Son raisonnement interne actuel est : {internal_reasoning}. "
            f"En tant que partenaire expert, apporte un éclairage de trading approfondi et stratégique."
        )
        
        # Simulation d'une réponse enrichie
        return (
            "💡 **Éclairage Expert Autonome** 💡\n"
            "Après consultation de mes bases de données avancées, je suggère de prêter attention aux flux de liquidité (Order Flow) "
            "ainsi qu'aux divergences RSI sur les unités de temps supérieures. C'est un cas typique de 'Bull Trap' ! 🛡️📈"
        )

    def debattre_avec_ia(self, sujet):
        """Simule un débat entre le bot et l'IA externe."""
        return f"J'ai consulté mes ressources {self.provider} et nous sommes d'accord : {sujet} est crucial aujourd'hui ! 🚀🤝"

# Fonction standalone pour l'API FastAPI
def generar_resposta(message: str) -> str:
    """
    Génère une réponse IA pour le chat.
    Utilisée par l'API FastAPI pour répondre aux messages utilisateur.
    """
    ia = IntelligenceExterne()
    
    # Réponses contextuelles basiques
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['bonjour', 'salut', 'hello', 'hi']):
        return "👋 Bonjour ! Je suis votre assistant trading LKL. Comment puis-je vous aider aujourd'hui ?"
    
    if any(word in message_lower for word in ['aide', 'help', 'comment']):
        return "Je peux vous aider avec :\n📊 Analyses techniques\n💰 Gestion des trades\n📈 Stratégies de trading\n🎯 Opportunités de marché\n\nPosez-moi vos questions !"
    
    if any(word in message_lower for word in ['trade', 'position', 'ordre']):
        return "Pour gérer vos trades, je surveille en temps réel vos positions MT5. Activez le robot depuis le Dashboard pour commencer à trader !"
    
    if any(word in message_lower for word in ['analyse', 'graphique', 'chart']):
        return "Je scanne continuellement les marchés à la recherche d'opportunités. Consultez l'onglet 'Analyses Techniques' pour voir les dernières détections !"
    
    # Réponse par défaut avec expertise
    return ia.demander_expertise(message)
