#!/usr/bin/env python3
"""Hauptskript: Datenaufbereitung + Visualisierung"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "src"))

from process import load_and_process_data, save_processed_data
from visualize import create_bar_chart, create_line_charts, create_absolute_line_chart

# Pfade
PROJECT_ROOT = Path(__file__).parent
DATA_RAW_2 = PROJECT_ROOT / "data_raw_2"
DATA_RAW_1 = PROJECT_ROOT / "data_raw_1"
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DATA = OUTPUT_DIR / "data"
OUTPUT_CHARTS = OUTPUT_DIR / "charts"

# 1. Datenaufbereitung
# Erst data_raw_2 einlesen, dann data_raw_1
df_processed_pct, df_processed_abs, year_counts, overall_share_df = load_and_process_data(DATA_RAW_2, DATA_RAW_1)

# 2. Processed Data speichern (prozentual & absolut)
processed_csv_pct = OUTPUT_DATA / "processed_data_percent.csv"
processed_csv_abs = OUTPUT_DATA / "processed_data_abs.csv"
save_processed_data(df_processed_pct, processed_csv_pct)
save_processed_data(df_processed_abs, processed_csv_abs)

# 3. Visualisierungen erstellen
print("\n" + "="*80)
print("VISUALISIERUNGEN")
print("="*80)

create_bar_chart(df_processed_abs, OUTPUT_CHARTS / "gender_by_genre.png")
num_charts = create_line_charts(df_processed_pct, OUTPUT_CHARTS, overall_share_df=overall_share_df)
# Zusätzlich: absolute Zahlen-Liniendiagramm
create_absolute_line_chart(year_counts, OUTPUT_CHARTS / "absolute_gender_trend.png")

print("\n" + "="*80)
print(f"✓ FERTIG! {num_charts} Genre Line Charts + 1 Balken Chart + 1 Absolute Line Chart erstellt")
print("="*80)
