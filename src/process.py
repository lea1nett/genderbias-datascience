import pandas as pd
from pathlib import Path
from config import GENRE_MAPPING

def load_and_process_data(data_raw_path):
    """Lädt CSV-Dateien, addiert Daten pro Jahr und Genre."""
    
    csv_files = sorted(data_raw_path.glob("*.csv"))
    dataframes_by_year = {}
    
    print("="*80)
    print("DATENAUFBEREITUNG")
    print("="*80)
    
    for csv_file in csv_files:
        year = int(csv_file.stem.replace('query', ''))
        df = pd.read_csv(csv_file)
        df['year'] = year
        dataframes_by_year[year] = df
        print(f"✓ '{csv_file.name}' eingelesen - Jahr: {year} ({len(df)} Zeilen)")
    
    # Zusammenführen
    df_combined = pd.concat(dataframes_by_year.values(), ignore_index=True)
    
    # Genre-Mapping
    df_combined['genre_simplified'] = df_combined['genreLabel'].map(GENRE_MAPPING)
    
    # Aggregieren pro Jahr, Genre und Geschlecht
    df_processed = df_combined.groupby(['year', 'genre_simplified', 'genderLabel'])['actorCount'].sum().reset_index()
    
    print(f"\n✓ Daten verarbeitet: {len(df_processed)} Zeilen")
    print(f"✓ Jahre: {sorted(df_processed['year'].unique())}")
    print(f"✓ Genres: {sorted(df_processed['genre_simplified'].unique())}")
    
    return df_processed

def save_processed_data(df, output_path):
    """Speichert verarbeitete Daten als CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n✓ Processed Data gespeichert: {output_path}")
