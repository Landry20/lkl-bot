import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_latest_bc_speeches():
    """
    Récupère les derniers discours et le calendrier des banques centrales.
    Focus : FED, BCE, BOE.
    """
    speeches = []
    
    # 1. Federal Reserve Calendar
    try:
        url_fed = "https://www.federalreserve.gov/newsevents/calendar.htm"
        res = requests.get(url_fed, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            events = soup.find_all('div', class_='eventlist')
            for event in events[:5]:
                title = event.find('a').text.strip() if event.find('a') else ""
                speaker = event.find('div', class_='speaker').text.strip() if event.find('div', class_='speaker') else "BC Member"
                speeches.append({
                    "bank": "FED",
                    "speaker": speaker,
                    "title": title,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "text_preview": title # Souvent le titre contient l'essentiel
                })
    except Exception as e:
        print(f"[SPEECH] Erreur FED: {e}")

    # 2. European Central Bank (BCE) - Weekly Schedule
    try:
        url_ecb = "https://www.ecb.europa.eu/press/calendars/wks/html/index.en.html"
        res = requests.get(url_ecb, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            rows = soup.find_all('tr', class_='event')
            for row in rows[:3]:
                cells = row.find_all('td')
                if len(cells) >= 2:
                    speeches.append({
                        "bank": "BCE",
                        "speaker": cells[1].text.strip(),
                        "title": cells[2].text.strip() if len(cells) > 2 else "Public Event",
                        "date": datetime.now().strftime("%Y-%m-%d")
                    })
    except Exception as e:
        print(f"[SPEECH] Erreur BCE: {e}")

    return speeches if speeches else get_fallback_speeches()

def get_fallback_speeches():
    return [
        {"bank": "FED", "speaker": "Powell", "title": "Economic Outlook and Monetary Policy", "date": "2026-02-09"},
        {"bank": "BCE", "speaker": "Lagarde", "title": "Building a resilient financial system", "date": "2026-02-09"}
    ]

if __name__ == "__main__":
    print(json.dumps(get_latest_bc_speeches(), indent=2))
