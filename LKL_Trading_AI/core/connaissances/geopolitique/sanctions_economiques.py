
"""
Sanctions économiques - Types, impacts Forex, exemples récents
Version : 2.0
"""

SANCTIONS_TYPES = """
1. Sanctions financières (SWIFT exclusion, gel actifs)
2. Sanctions énergétiques (embargo pétrole/gaz)
3. Sanctions commerciales (tarifs douaniers, quotas)
4. Sanctions individuelles (gel comptes oligarques)
5. Sanctions technologiques (puces, logiciels)
"""

IMPACTS_SANCTIONS = {
    "SWIFT exclusion": "Devise concernée ↓ très fort (RUB 2022 -40% en jours)",
    "Embargo pétrole/gaz": "Devise exportatrice ↑ (si contournement), importatrice ↓ (EUR 2022)",
    "Tarifs douaniers US-Chine": "CNY ↓ contrôlé, USD ↑, AUD ↓ (Chine demande fer)",
    "Gel réserves": "Or ↑ (alternative), CNY/RUB paiements alternatifs ↑ long terme"
}

EXEMPLES_SANCTIONS = """
- Russie 2022 : SWIFT + gel ~300 Md$ → RUB 150 → 50 (contrôle capital) → stabilisation artificielle
- Iran 2018-2025 : Embargo pétrole → rial ↓ massif, or ↑ local
- Chine vs USA 2018-2024 : Tarifs → CNY contrôlé 7-7.3, AUD/NZD ↓ (Chine ralentie)
- Venezuela 2017-2025 : Sanctions pétrole → bolivar hyperinflation, BTC ↑ local
"""

def get_sanctions_summary():
    return """
Sanctions SWIFT → devise ↓ massif  
Embargo énergie → exportateur ↑ si contournement, importateur ↓  
Tarifs → CNY/AUD ↓ contrôlé  
Gel réserves → or ↑ long terme
"""

def get_full_sanctions():
    return (
        SANCTIONS_TYPES + "\n\n" +
        "Impacts par type :\n" + "\n".join([f"- {k}: {v}" for k,v in IMPACTS_SANCTIONS.items()]) + "\n\n" +
        "Exemples récents :\n" + EXEMPLES_SANCTIONS
    )