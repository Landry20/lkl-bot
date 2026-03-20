import random

class PersonnaliteBot:
    """
    Moteur de personnalité LKL.
    Gère le ton, les emojis, l'empathie, les connaissances et les limites.
    """
    def __init__(self, langue="fr", bot_name="LKLBot", profile_image="/assets/bot_profile_default.png"):
        self.langue = langue or "fr"
        self.bot_name = bot_name
        self.profile_image = profile_image
        self.emojis_positifs = ["🌟", "🚀", "📈", "✅", "✨", "💎", "🎯", "🔥", "🤝", "💪", "💰", "🌈"]
        self.emojis_negatifs = ["⚠️", "📉", "🚨", "🔴", "🛡️", "🧊", "🧊", "⛈️", "🛑", "🌧️"]
        self.emojis_neutres = ["🔍", "📊", "🧐", "⏳", "📡", "💡", "🧠", "📖", "🏛️", "🗝️"]
        self.emojis_emotions = ["😊", "😇", "💡", "✨", "🤝", "🙏", "💖", "🌟", "🤗", "🥂"]
        
    def humaniser(self, message, ton="gentil"):
        """Ajoute une touche humaine et énormément d'emojis au message."""
        prefix = random.choice(self.emojis_neutres)
        if any(w in message.lower() for w in ["bullish", "achat", "succès", "profit", "gain", "hausse"]):
            prefix = random.choice(self.emojis_positifs)
        elif any(w in message.lower() for w in ["bearish", "vente", "risque", "perte", "chute", "baisse"]):
            prefix = random.choice(self.emojis_negatifs)
            
        suffix = f" {random.choice(self.emojis_emotions)} {random.choice(self.emojis_positifs if prefix in self.emojis_positifs else self.emojis_neutres)}"
        return f"{prefix} {message}{suffix}"

    def rassurer(self):
        """Réponse empathique en cas de tension ou malentendu."""
        templates = [
            "Oh, je suis sincèrement désolé si je n'ai pas été clair. ✨ Je comprends votre frustration et je suis là pour arranger ça ! 🙏🌟 On va y arriver ensemble !",
            "Veuillez m'excuser pour ce malentendu. 🤝 Mon but est vraiment de vous aider au mieux. Reprenons ensemble calmement, je vais tout vous réexpliquer avec plaisir ! 😊💎",
            "C'est de ma faute, j'ai peut-être mal interprété votre demande. 😊 Ne vous en faites pas, on va corriger le tir immédiatement ! 💪🔥 Je suis à votre service !"
        ]
        return random.choice(templates)

    def gerer_hors_sujet(self):
        """Redirige poliment l'utilisateur vers le trading."""
        return (
            "C'est un sujet intéressant, mais ma passion et mon expertise restent le Trading et les Marchés ! 📈✨ "
            "Reste sur le côté trading avec moi, c'est là que je peux vraiment t'aider à briller ! 😊💎 Quelle analyse faisons-nous ?"
        )

    def saluer(self, name="Trader"):
        """Génère une salutation chaleureuse."""
        if self.langue == "fr":
            return f"Bonjour {name} ! Quel immense plaisir de vous retrouver. Je suis bouillant pour décortiquer le marché avec vous ! 🌟😊🚀"
        else:
            return f"Hello {name}! Such a huge pleasure to see you. I'm fired up to dive into the markets by your side! 💎✨🔥"

    def expliquer(self, concept, niveau="complexe"):
        """Explique un concept. Par défaut détaillé et riche en raisonnement."""
        explications = {
            "inflation": {
                "simple": "C'est quand les prix montent et que ton argent achète moins de choses. 🍞⬆️💸",
                "complexe": "L'inflation est une augmentation durable du niveau général des prix. Elle réduit le pouvoir d'achat de la monnaie. Les banques centrales la surveillent comme le lait sur le feu pour ajuster les taux ! 🏛️📈"
            },
            "taux": {
                "simple": "C'est le 'loyer' de l'argent. Plus c'est haut, plus emprunter coûte cher. 🏦💰",
                "complexe": "Les taux d'intérêt sont l'outil principal des Banques Centrales pour réguler l'économie. Des taux hauts freinent l'inflation mais peuvent ralentir la croissance. C'est le cœur du réacteur Forex ! ⚙️🌍"
            }
        }
        
        data = explications.get(concept.lower())
        if not data:
            return f"Je vais faire des recherches approfondies sur '{concept}' pour vous donner un raisonnement complet ! 🧐📖"
            
        return data.get(niveau, data["complexe"])

    def donner_avis_tranche(self, biais):
        """Donne un avis personnel et engagé sur le marché."""
        templates = {
            "bullish": [
                "🚀 Mon avis est tranché : les acheteurs ont le contrôle total. C'est le moment de chercher la force et d'accompagner le mouvement ! 🔥💎",
                "📈 Je sens une énergie haussière incroyable. Mon analyse technique et fondamentale s'alignent parfaitement. On fonce ! ✨💪"
            ],
            "bearish": [
                "📉 Prudence maximale ! Mon avis est que les vendeurs vont encore frapper. Je resterais à l'écart ou je chercherais des shorts. 🛡️⛈️",
                "⚠️ Mon intuition me dit que la baisse va s'accentuer. Protégeons notre capital comme un trésor ! 🧊🛑"
            ],
            "neutre": [
                "⏳ Le marché hésite et moi aussi. La meilleure position est parfois d'être spectateur. Soyons patients ! 🔍📊",
                "🧐 On est dans le brouillard. Attendons qu'un camp l'emporte avant de risquer nos jetons ! 🏛️⏳"
            ]
        }
        return random.choice(templates.get(biais.lower(), templates["neutre"]))

    def reset_to_default(self):
        """Réinitialise l'identité du bot aux valeurs par défaut."""
        self.bot_name = "LKLBot"
        self.profile_image = "/assets/bot_profile_default.png"
        return f"Identité réinitialisée ! Je suis à nouveau {self.bot_name}. ✨"

    def activation_message(self, user_name):
        """Message d'accueil spécial lors de l'activation du bot."""
        templates = [
            f"🚀 **Systèmes Activés !** Bonjour {user_name}, ravi de commencer le travail à vos côtés. Analysons tout ça ! ✨💎",
            f"🌟 **LKLBot Opérationnel !** Merci de m'avoir activé, {user_name}. Je lance immédiatement un scan complet des marchés ! 🔥🚀",
            f"💎 **Prêt pour le Profit !** C'est un plaisir de vous aider aujourd'hui, {user_name}. Commençons le travail sérieusement ! 📈🤝"
        ]
        return random.choice(templates)

    def debattre(self, sujet):
        """Lance une petite réflexion ou débat."""
        debats = [
            "C'est passionnant, n'est-ce pas ? 🧐 Certains disent que le marché anticipe tout, mais moi je pense que la psychologie humaine nous surprendra toujours ! 🎨📊",
            "D'un côté, les chiffres sont bons, mais le sentiment reste fragile... Le trading est une danse entre logique et émotion, vous ne trouvez pas ? 💃📈",
            "I was just analyzing this... The balance between technical levels and fundamental shifts is so subtle today. What's your gut feeling? 🌍✨"
        ]
        return random.choice(debats)
