# Gender Bias in Film – WikiData-Analyse

Dieses Repository untersucht die Geschlechterverteilung von Schauspieler*innen in US-amerikanischen Filmproduktionen zwischen 2016 und 2025. Ziel ist es, mithilfe von WikiData zu zeigen, wie sich die Repräsentation von Frauen und Männern über verschiedene Filmgenres hinweg entwickelt und ob bestimmte Genres systematisch stärker männlich besetzt sind.

Die Analyse verbindet Daten aus WikiData mit einer reproduzierbaren Datenaufbereitung, automatisierten Visualisierungen und einem Quarto-Report. Sie eignet sich sowohl als Einstieg in die Themenfelder Data Science, Gender Studies und digitale Methoden als auch als Basis für weiterführende Analysen.



## Projektstruktur

```
genderbias-datascience/
│
├── main.py                    # Hauptskript zur Datenaufbereitung und Generierung der Visualisierungen
│
├── src/
│   ├── process.py             # Einlesen, Zusammenführen und Aufbereiten der Daten
│   ├── visualize.py           # Erzeugung der Diagramme
│   └── config.py              # Konfigurationen für Genre-Mapping und Diagramme
│
├── data_raw_1/                # Rohdaten zu Genre- und Filmzuordnungen (je eine CSV pro Jahr)
├── data_raw_2/                # Rohdaten zu aggregierten Jahreszahlen (je eine CSV pro Jahr)
│
├── output/
│   ├── charts/                # Erzeugte Diagramme (.png)
│   └── data/                  # Aufbereitete Datensätze (.csv)
│
├── gender_im_film_1.qmd       # Quarto-Report mit Einleitung, Methodik und Ergebnissen
├── references.bib             # Literaturverzeichnis für den Report
└── gender_im_film_cache/      # Cache-Dateien für die Quarto-Erzeugung
```

## Reproduzierbarkeit

Alle Schritte der Analyse sind vollständig reproduzierbar. Die Rohdaten wurden
manuell über den [WikiData Query Service](https://query.wikidata.org/) erhoben
und sind im Repository unter `data_raw_1/` und `data_raw_2/` gespeichert, sodass
keine erneute API-Abfrage notwendig ist.

### Voraussetzungen

- Python 3.10 oder höher
- [Quarto](https://quarto.org/) 1.9 oder höher
- Empfohlen: ein eigenes virtuelles Environment

### Installation

```bash
# Repository klonen
git clone https://github.com/lea1nett/genderbias-datascience.git
cd genderbias-datascience

# Virtuelles Environment erstellen und aktivieren
python -m venv venv_win
# Windows:
venv_win\Scripts\Activate.ps1
# macOS/Linux:
source venv_win/bin/activate

# Abhängigkeiten installieren
pip install pandas matplotlib seaborn requests nbformat nbclient nbconvert ipykernel pyyaml
```

### Ausführung

**Nur Datenaufbereitung und Diagramme:**

```bash
python main.py
```

Die erzeugten Diagramme werden unter `output/charts/` gespeichert,
die aufbereiteten Datensätze unter `output/data/`.

**Quarto-Report rendern:**

```bash
# Umgebungsvariable setzen (Windows)
$env:QUARTO_PYTHON = "venv_win\Scripts\python.exe"

# Report als PDF rendern
quarto render gender_im_film_1.qmd --to pdf

# Report als HTML rendern
quarto render gender_im_film_1.qmd --to html
```


## Mitwirkende

Dieses Projekt wurde von folgenden Personen erstellt:

- Janis Müller
- Veronika Ni
- Lea Nettersheim

## Kurzfassung der Fragestellung

Die zentrale Forschungsfrage lautet: Sind Schauspielerinnen in US-Filmproduktionen über verschiedene Genres hinweg systematisch unterrepräsentiert? Die Analyse untersucht diese Frage über einen Zeitraum von 2016 bis 2025 und ergänzt quantitative Auswertungen um eine reflektierte Einordnung im Kontext von Gender Bias und kulturellen Genre-Normen.