import pandas as pd
import re
from config import GENRE_MAPPING

def load_and_process_data(data_raw_counts_path, data_raw_genre_path):
    """Lädt CSV-Dateien aus data_raw_2 für Jahreszahlen und data_raw_1 für Genre-Daten."""
    data_frame_list_counts = []
    data_frame_list_genre = []

    for idx, data_raw_path in enumerate((data_raw_counts_path, data_raw_genre_path)):
        print(f"\nLese Daten aus: {data_raw_path}")
        csv_files = sorted(data_raw_path.glob("*.csv"))

        if not csv_files:
            raise FileNotFoundError(f"Keine CSV-Dateien in {data_raw_path} gefunden.")

        for csv_file in csv_files:
            match = re.search(r"\d{4}", csv_file.stem)
            if not match:
                raise ValueError(f"Jahr konnte nicht aus dem Dateinamen extrahiert werden: {csv_file.name}")

            year = int(match.group())
            df = pd.read_csv(csv_file)
            df['year'] = year
            if idx == 0:
                data_frame_list_counts.append(df)
            else:
                data_frame_list_genre.append(df)
            print(f"✓ '{csv_file.name}' eingelesen - Jahr: {year} ({len(df)} Zeilen)")

    print("="*80)
    print("DATENAUFBEREITUNG")
    print("="*80)

    # data_raw_counts_path (data_raw_2): enthält nur Jahreszahlen pro Geschlecht
    if not data_frame_list_counts:
        raise FileNotFoundError("Keine CSVs in data_raw_2 gefunden für absolute Trendberechnung.")
    df_combined_counts = pd.concat(data_frame_list_counts, ignore_index=True)

    # data_raw_genre_path (data_raw_1): enthält Genre-Informationen
    if not data_frame_list_genre:
        raise FileNotFoundError("Keine CSVs in data_raw_1 gefunden für Genre-Auswertungen.")
    df_combined_genre = pd.concat(data_frame_list_genre, ignore_index=True)

    # Genre-Mapping
    df_combined_genre['genre_simplified'] = df_combined_genre['genreLabel'].map(GENRE_MAPPING)

    # Absolute Aggregation: pro Jahr, Genre und Geschlecht (nur genre-labeled data)
    df_abs = df_combined_genre.groupby(['year', 'genre_simplified', 'genderLabel'])['actorCount'].sum().reset_index()

    # Jahresübersicht (absolute Zahlen) für die Linienchart: nur aus data_raw_2
    year_totals_counts = df_combined_counts.groupby(['year', 'genderLabel'])['actorCount'].sum().unstack(fill_value=0)
    year_counts_list = []
    for year in sorted(year_totals_counts.index):
        male = int(year_totals_counts.loc[year].get('male', 0))
        female = int(year_totals_counts.loc[year].get('female', 0))
        year_counts_list.append({int(year): [male, female]})

    # Gesamtjahres-Anteil aus data_raw_2, zum Vergleich in Genreplots
    overall_share_df = year_totals_counts.div(year_totals_counts.sum(axis=1), axis=0) * 100
    overall_share_df = overall_share_df.reset_index()

    # Prozentualer Anteil pro Jahr + Genre (für Graphiken) - berechnet aus df_abs
    df_abs_total = df_abs.copy()
    total_per_group = df_abs_total.groupby(['year', 'genre_simplified'])['actorCount'].transform('sum')
    # Avoid division by zero
    total_per_group = total_per_group.replace(0, pd.NA)
    df_abs_total['share'] = (df_abs_total['actorCount'] / total_per_group * 100).fillna(0)

    df_processed_pct = df_abs_total.copy()

    print(f"\n✓ Daten verarbeitet: {len(df_abs)} Zeilen (absolute Aggregation)")
    print(f"✓ Jahre: {sorted(df_abs['year'].unique())}")
    print(f"✓ Genres: {sorted(df_abs['genre_simplified'].unique())}")

    return df_processed_pct, df_abs, year_counts_list, overall_share_df

def save_processed_data(df, output_path):
    """Speichert verarbeitete Daten als CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n✓ Processed Data gespeichert: {output_path}")
