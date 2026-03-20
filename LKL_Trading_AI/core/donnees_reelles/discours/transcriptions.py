from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import json

class TranscriptionBridge:
    """
    Pont pour transcrire ou récupérer des transcriptions de discours financiers.
    Gère les vidéos YouTube (FED/BCE) et les pages de transcriptions officielles.
    """
    
    @staticmethod
    def get_youtube_transcript(video_id):
        """
        Récupère la transcription d'une vidéo YouTube (ex: conférence de presse FED).
        """
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'fr'])
            full_text = " ".join([t['text'] for t in transcript_list])
            return full_text
        except Exception as e:
            print(f"[TRANSCRIPT] Erreur YouTube ({video_id}): {e}")
            return None

    @staticmethod
    def get_official_ecb_transcript(url):
        """
        Scrape la transcription officielle sur le site de la BCE.
        """
        try:
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'lxml')
                # Sélecteur typique pour le corps du discours sur le site de la BCE
                content = soup.find('main') or soup.find('div', class_='section')
                if content:
                    return content.text.strip()
        except Exception as e:
            print(f"[TRANSCRIPT] Erreur BCE Scrape: {e}")
        return None

def transcrire_media_recent(media_info):
    """
    Prend une info média (URL ou ID Vidéo) et retourne le texte compris par le bot.
    """
    if "youtube.com" in media_info or "youtu.be" in media_info:
        # Extraire l'ID (simplifié)
        video_id = media_info.split("v=")[-1] if "v=" in media_info else media_info.split("/")[-1]
        return TranscriptionBridge.get_youtube_transcript(video_id)
    
    if "ecb.europa.eu" in media_info:
        return TranscriptionBridge.get_official_ecb_transcript(media_info)
        
    return "Contenu média non supporté ou nécessite une API externe (Whisper/Google)."

if __name__ == "__main__":
    # Test avec une vidéo connue de la FED (si applicable)
    print(transcrire_media_recent("https://www.youtube.com/watch?v=dQw4w9WgXcQ")) # Rickroll pour le test ;)
