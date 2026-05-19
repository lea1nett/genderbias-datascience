import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from config import COLORS, CHART_SETTINGS

def create_bar_chart(df, output_path):
    """Erstellt Balkendiagramm: Gesamtverteilung pro Genre."""
    
    df_total = df.groupby(['genre_simplified', 'genderLabel'])['actorCount'].sum().reset_index()
    df_pivot = df_total.pivot(index='genre_simplified', columns='genderLabel', values='actorCount')
    
    fig, ax = plt.subplots(figsize=CHART_SETTINGS['figsize_bar'])
    df_pivot.plot(kind='bar', ax=ax, 
                   color=[COLORS['female'], COLORS['male']], 
                   width=0.8)
    
    ax.set_title('Gender-Verteilung pro Filmgenre (2016-2026)', 
                  fontsize=CHART_SETTINGS['fontsize_title'], fontweight='bold')
    ax.set_xlabel('Genre', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.set_ylabel('Anzahl Schauspieler', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.legend(['Frauen', 'Männer'], fontsize=CHART_SETTINGS['fontsize_legend'])
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=CHART_SETTINGS['dpi'], bbox_inches='tight')
    plt.close()
    print(f"✓ Balken Chart gespeichert: {output_path}")

def create_line_charts(df, output_dir):
    """Erstellt Line Charts pro Genre mit Jahrestrend."""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    genres = sorted(df['genre_simplified'].unique())
    
    for genre in genres:
        df_genre = df[df['genre_simplified'] == genre]
        df_pivot = df_genre.pivot(index='year', columns='genderLabel', values='actorCount')
        
        fig, ax = plt.subplots(figsize=CHART_SETTINGS['figsize_line'])
        df_pivot.plot(kind='line', ax=ax, marker='o', 
                       linewidth=CHART_SETTINGS['linewidth'],
                       markersize=CHART_SETTINGS['markersize'],
                       color=[COLORS['female'], COLORS['male']])
        
        ax.set_title(f'Gender-Trend: {genre} (2016-2026)', 
                      fontsize=CHART_SETTINGS['fontsize_title'], fontweight='bold')
        ax.set_xlabel('Jahr', fontsize=CHART_SETTINGS['fontsize_label'])
        ax.set_ylabel('Anzahl Schauspieler', fontsize=CHART_SETTINGS['fontsize_label'])
        ax.legend(['Frauen', 'Männer'], fontsize=CHART_SETTINGS['fontsize_legend'])
        ax.grid(True, alpha=0.3)
        ax.set_xticks(sorted(df_pivot.index))
        plt.tight_layout()
        
        output_path = output_dir / f'gender_trend_{genre.lower().replace("_", "")}.png'
        plt.savefig(output_path, dpi=CHART_SETTINGS['dpi'], bbox_inches='tight')
        plt.close()
        print(f"✓ Line Chart gespeichert: {output_path}")
    
    return len(genres)
