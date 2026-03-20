import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_analysis_chart(symbol, price_data, ta_data, output_path):
    """
    Génère une image de l'analyse technique (Prix, SMMA, Fibonacci, S/R).
    """
    try:
        df = pd.DataFrame(price_data)
        plt.figure(figsize=(10, 6))
        plt.style.use('dark_background')
        
        # Plot Prix
        plt.plot(df.index, df['close'], label='Prix', color='#f8fafc', alpha=0.8)
        
        # Plot SMMA 50 (Simulée pour le graphique)
        if 'ma50' in ta_data:
            plt.axhline(y=ta_data['ma50'], color='#7928ca', linestyle='--', label='SMMA 50', alpha=0.6)
            
        # Plot Fibonacci Zones
        if 'fibo' in ta_data:
            f = ta_data['fibo']
            colors = {'38.2': '#007cf0', '50.0': '#00dfd8', '61.8': '#7928ca', '78.6': '#ef4444'}
            for level, price in f.items():
                if level in colors:
                    plt.axhline(y=price, color=colors[level], alpha=0.3, label=f'Fibo {level}%')
        
        # Titre et axes
        plt.title(f"Analyse LKL Bot - {symbol}", color='#007cf0', fontsize=14, fontweight='bold')
        plt.legend(loc='best', fontsize='small')
        plt.grid(True, alpha=0.1)
        
        # Sauvegarde
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=100, bbox_inches='tight')
        plt.close()
        return True
    except Exception as e:
        print(f"[CHART] Erreur generation: {e}")
        return False

def generate_fundamental_pulse_chart(currency_scores, output_path):
    """
    Génère un graphique à barres comparant la force fondamentale des devises.
    currency_scores: dict { 'USD': 45, 'EUR': -20, ... }
    """
    try:
        labels = list(currency_scores.keys())
        values = list(currency_scores.values())
        colors = ['#10b981' if v > 0 else '#ef4444' for v in values]

        plt.figure(figsize=(8, 5))
        plt.style.use('dark_background')
        
        bars = plt.bar(labels, values, color=colors, alpha=0.7)
        plt.axhline(0, color='white', linewidth=0.8, alpha=0.5)
        
        plt.title("LKL Fundamental Pulse - Force Relative", color='#007cf0', fontsize=12, pad=20)
        plt.grid(axis='y', alpha=0.1)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        plt.savefig(output_path, dpi=100, bbox_inches='tight', transparent=True)
        plt.close()
        return True
    except Exception as e:
        print(f"[CHART] Erreur generation pulse: {e}")
        return False
