import sys
import os

# Ajustement du path pour les imports inter-modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.personnalite import PersonnaliteBot

class ClarificateurFondamental:
    """
    Clarification Fondamentale - Version Chic & Animée ✨
    """
    def __init__(self, analyses=None):
        self.analyses = analyses or {}
        self.bot = PersonnaliteBot()

    def clarifier_journee(self):
        """Synthèse ultra-détaillée avec une pluie d'emojis 🌟🔥💎"""
        events = self.analyses.get('today_events', [])
        if not events:
            return self.bot.humaniser("Ma vision pour aujourd'hui : le calme avant la tempête ? 🌊 Restons zen, surveillons les niveaux techniques, et attendons patiemment l'étincelle ! ☕✨🧘‍♂️")
        
        summary = "🚀 **ALERTE RAISONNEMENT : Voici ma lecture du jour !** 🚀\n\n"
        for ev in sorted(events, key=lambda x: x.get('impact', ''), reverse=True):
            impact_icon = "🔴 EXTRÊME" if ev['impact'] == 'HIGH' else "🟡 MODÉRÉ"
            summary += f"🔥 {impact_icon} | **{ev['currency']}** : {ev['event']} à {ev['time']} 📡\n"
            summary += f"   💡 *Mon avis* : Cet événement pourrait secouer les pips ! Soyez prêt à réagir si le biais se confirme. 💎📈\n\n"
        
        summary += "🤝 **On reste ensemble sur le coup !** 💪🔥"
        return summary

    def clarifier_semaine(self):
        """Vision hebdomadaire exhaustive et animée 🗓️🌍✨"""
        msg = (
            "🗓️ **VOTRE PERSPECTIVE HEBDOMADAIRE CHIC** 🗓️\n\n"
            "✨ Le sentiment du marché est un vrai débat en cours ! 🧐\n"
            "📈 **Côté Espoir** : Les chiffres de croissance nous donnent le sourire ! 💪\n"
            "📉 **Côté Prudence** : L'inflation joue avec nos nerfs... ⛈️\n\n"
            "💎 **Mon Conseil d'Ami** : Ne forcez rien, laissez le marché venir à vous. La discipline est la clé de la richesse ! 🥂✨🗝️"
        )
        return msg

    def clarifier_long_terme(self):
        """Raisonnement de fond ultra-complet 🏛️⚙️🌍"""
        raisonnement = (
            "Sur le très long terme, on observe une restructuration globale. 🏗️ "
            "Les banques centrales essaient de garder le contrôle tout en évitant le crash. 🏛️📈 "
            "C'est une période historique pour nous, les traders, car la volatilité crée des opportunités en or ! 💰💎 "
            "Gardez le cap, restez éduqués, et la fortune vous suivra ! 🚀🌈✨"
        )
        return self.bot.humaniser(raisonnement)

    def analyser_actif_special(self, symbol, type_actif="FOREX"):
        """Génère un raisonnement spécifique par classe d'actif."""
        if type_actif == "CRYPTO":
            raison = (
                f"L'analyse du {symbol} montre une volatilité propre aux actifs numériques. ⛓️✨ "
                "On surveille l'adoption institutionnelle et les flux on-chain. Le sentiment est roi ici ! 👑🚀"
            )
        elif type_actif == "INDEX":
            raison = (
                f"L'indice {symbol} reflète la santé globale de l'économie. 📈🌍 "
                "Les décisions de la Fed et les résultats des entreprises technologiques seront les catalyseurs ! 📡🏛️"
            )
        elif type_actif == "STOCK":
            raison = (
                f"Pour l'action {symbol}, tout va se jouer sur les prochains résultats (Earnings). 📖💰 "
                "La valorisation actuelle est un débat entre croissance et prudence. ⚖️✨"
            )
        else:
            raison = f"Analyse standard du Forex pour {symbol}. On surveille les taux et les news économiques ! 💹📊"
            
        return self.bot.humaniser(raison)

    def generer_synthese_complete(self, bias_global="neutre"):
        return {
            "daily": self.clarifier_journee(),
            "weekly": self.clarifier_semaine(),
            "conclusion": f"✅ **Ma Conclusion** : Le biais est {bias_global.upper()}. On reste zen et concentré ! 🧘‍♂️✨"
        }
