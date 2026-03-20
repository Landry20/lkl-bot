import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import json

class NewsScraper:
    def __init__(self):
        self.ff_url = "https://nfs.forexfactory.net/ff_calendar_thisweek.xml"
        self.investir_url = "https://investir.lesechos.fr/marches/agenda" # Pour plus tard via scraping simple

    def get_forex_factory_calendar(self):
        """
        Récupère le calendrier économique de Forex Factory via leur flux XML.
        """
        try:
            response = requests.get(self.ff_url, timeout=10)
            if response.status_code != 200:
                print(f"[ERROR] Forex Factory: Status {response.status_code}")
                return []

            root = ET.fromstring(response.content)
            events = []
            for event in root.findall('event'):
                data = {
                    'title': event.find('title').text,
                    'country': event.find('country').text,
                    'date': event.find('date').text,
                    'time': event.find('time').text,
                    'impact': event.find('impact').text,
                    'forecast': event.find('forecast').text,
                    'previous': event.find('previous').text
                }
                events.append(data)
            return events
        except Exception as e:
            print(f"[ERROR] Forex Factory scraping error: {str(e)}")
            return []

    def get_daily_impact(self, currency="USD"):
        """
        Analyse l'impact des annonces du jour pour une devise donnée.
        """
        all_events = self.get_forex_factory_calendar()
        today = datetime.now().strftime("%m-%d-%Y")
        
        daily_events = [e for e in all_events if e['country'] == currency and e['date'] == today]
        
        high_impact = [e for e in daily_events if e['impact'] == 'High']
        medium_impact = [e for e in daily_events if e['impact'] == 'Medium']
        
        return {
            'currency': currency,
            'today': today,
            'high_impact_count': len(high_impact),
            'medium_impact_count': len(medium_impact),
            'events': daily_events
        }

if __name__ == "__main__":
    scraper = NewsScraper()
    print("Test Forex Factory Scraper...")
    usd_impact = scraper.get_daily_impact("USD")
    print(json.dumps(usd_impact, indent=2))
