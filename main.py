#!/usr/bin/env python3
"""Hauptskript: Datenaufbereitung + Visualisierung"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "src"))

from process import load_and_process_data, save_processed_data
from visualize import create_bar_chart, create_line_charts

# Pfade
PROJECT_ROOT = Path(__file__).parent
DATA_RAW = PROJECT_ROOT / "data_raw"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DATA = OUTPUT_DIR / "data"
OUTPUT_CHARTS = OUTPUT_DIR / "charts"

# 1. Datenaufbereitung
df_processed = load_and_process_data(DATA_RAW)

# 2. Processed Data speichern
processed_csv = OUTPUT_DATA / "processed_data.csv"
save_processed_data(df_processed, processed_csv)

# 3. Visualisierungen erstellen
print("\n" + "="*80)
print("VISUALISIERUNGEN")
print("="*80)

create_bar_chart(df_processed, OUTPUT_CHARTS / "gender_by_genre.png")
num_charts = create_line_charts(df_processed, OUTPUT_CHARTS)

print("\n" + "="*80)
print(f"✓ FERTIG! {num_charts} Line Charts + 1 Balken Chart erstellt")
print("="*80)
