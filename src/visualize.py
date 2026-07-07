import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from pathlib import Path
from config import COLORS, CHART_SETTINGS

def create_bar_chart(df, output_path, verbose=False):
    """Erstellt Balkendiagramm: Gesamtverteilung pro Genre."""
    # Berechne pro Genre den prozentualen Anteil (über alle Jahre)
    df_total = df.groupby(['genre_simplified', 'genderLabel'])['actorCount'].sum().reset_index()
    gender_order = ['male', 'female']
    df_pivot = df_total.pivot(index='genre_simplified', columns='genderLabel', values='actorCount').reindex(columns=gender_order, fill_value=0)
    df_pct = df_pivot.div(df_pivot.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=CHART_SETTINGS['figsize_bar'])
    # stacked 100% bar chart
    df_pct.plot(kind='bar', ax=ax, 
                stacked=True,
                color=[COLORS['male'], COLORS['female']],
                width=0.8)

    ax.set_title('Gender-Verteilung pro Filmgenre von 2016-2025 (in %)', 
                  fontsize=CHART_SETTINGS['fontsize_title'], fontweight='bold')
    ax.set_xlabel('Genre', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.set_ylabel('Prozent', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.set_ylim(0, 100)
    ax.set_yticks(range(0, 101, 10))
    ax.legend(['Männer', 'Frauen'], fontsize=CHART_SETTINGS['fontsize_legend'])
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=CHART_SETTINGS['dpi'], bbox_inches='tight')
    plt.close()
    if verbose:
        print(f"✓ Balken Chart gespeichert: {output_path}")

def create_line_charts(df, output_dir, overall_share_df=None, verbose=False):
    """Erstellt Line Charts pro Genre mit Jahrestrend."""
    
    output_dir.mkdir(parents=True, exist_ok=True)
    genres = sorted(df['genre_simplified'].unique())
    gender_labels = {'female': 'Frauen', 'male': 'Männer'}
    
    for genre in genres:
        df_genre = df[df['genre_simplified'] == genre]
        gender_order = ['female', 'male']
        df_pivot = df_genre.pivot(index='year', columns='genderLabel', values='share').reindex(columns=gender_order, fill_value=0)

        fig, ax = plt.subplots(figsize=CHART_SETTINGS['figsize_line'])
        for gender in gender_order:
            ax.plot(df_pivot.index, df_pivot[gender], marker='o', 
                    linewidth=CHART_SETTINGS['linewidth'],
                    markersize=CHART_SETTINGS['markersize'],
                    color=COLORS[gender],
                    label=f'{gender_labels[gender]} Anteil im Genre')

        if overall_share_df is not None:
            overall_share = overall_share_df.set_index('year').reindex(df_pivot.index).ffill().fillna(0)
            for gender in gender_order:
                ax.plot(overall_share.index, overall_share[gender], linestyle='--', 
                        linewidth=2, color=COLORS[gender],
                        label=f'{gender_labels[gender]} Anteil insgesamt')

        ax.set_title(f'Gender-Trend (in %): {genre} (2016-2025)', 
                      fontsize=CHART_SETTINGS['fontsize_title'], fontweight='bold')
        ax.set_xlabel('Jahr', fontsize=CHART_SETTINGS['fontsize_label'])
        ax.set_ylabel('Prozent', fontsize=CHART_SETTINGS['fontsize_label'])
        ax.set_ylim(0, 100)
        ax.set_yticks(range(0, 101, 10))
        ax.legend(fontsize=CHART_SETTINGS['fontsize_legend'])
        ax.grid(True, alpha=0.3)
        ax.set_xticks(sorted(df_pivot.index))
        plt.tight_layout()

        output_path = output_dir / f'gender_trend_{genre.lower().replace("_", "")}.png'
        plt.savefig(output_path, dpi=CHART_SETTINGS['dpi'], bbox_inches='tight')
        plt.close()
        if verbose:
            print(f"✓ Line Chart gespeichert: {output_path}")
    
    return len(genres)

def create_absolute_line_chart(year_counts_list, output_path, verbose=False):
    """Erstellt eine Linie mit absoluten Schauspielerzahlen (male/female) über Jahre."""
    # year_counts_list: [{year: [male, female]}, ...]
    rows = []
    for entry in year_counts_list:
        for year, vals in entry.items():
            rows.append({'year': int(year), 'male': int(vals[0]), 'female': int(vals[1])})

    df_years = pd.DataFrame(rows).sort_values('year')
    df_years = df_years.set_index('year')

    fig, ax = plt.subplots(figsize=CHART_SETTINGS['figsize_line'])
    df_years.plot(kind='line', ax=ax, marker='o', 
                  linewidth=CHART_SETTINGS['linewidth'],
                  markersize=CHART_SETTINGS['markersize'],
                  color=[COLORS['male'], COLORS['female']])

    ax.set_title('Absolute Anzahl Schauspieler*innen nach Geschlecht (2016-2025)', fontsize=CHART_SETTINGS['fontsize_title'], fontweight='bold')
    ax.set_xlabel('Jahr', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.set_ylabel('Anzahl Schauspieler*innen', fontsize=CHART_SETTINGS['fontsize_label'])
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=8, integer=True))
    ax.legend(['Männer', 'Frauen'], fontsize=CHART_SETTINGS['fontsize_legend'])
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=CHART_SETTINGS['dpi'], bbox_inches='tight')
    plt.close()
    if verbose:
        print(f"✓ Absolute Line Chart gespeichert: {output_path}")
