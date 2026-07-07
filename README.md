# Gender Bias in Film – WikiData-Analyse

Dieses Repository untersucht die Geschlechterverteilung von Schauspieler*innen in US-amerikanischen Filmproduktionen zwischen 2016 und 2025. Ziel ist es, mithilfe von WikiData zu zeigen, wie sich die Repräsentation von Frauen und Männern über verschiedene Filmgenres hinweg entwickelt und ob bestimmte Genres systematisch stärker männlich besetzt sind.

Die Analyse verbindet Daten aus WikiData mit einer reproduzierbaren Datenaufbereitung, automatisierten Visualisierungen und einem Quarto-Report. Sie eignet sich sowohl als Einstieg in die Themenfelder Data Science, Gender Studies und digitale Methoden als auch als Basis für weiterführende Analysen.

## Reproduzierbarkeit

Das Projekt ist so angelegt, dass die Datenaufbereitung, die Erstellung der Auswertungen und die Generierung des Reports nachvollziehbar und wiederholbar sind.

### Voraussetzungen

- Python 3.x
- Quarto
- Eine Python-Umgebung mit den benötigten Paketen wie pandas und matplotlib

### Ablauf

1. Virtuelle Umgebung aktivieren
   - Beispiel unter Windows:
     `.\venv_win\Scripts\Activate.ps1`

2. Datenverarbeitung ausführen
   - `python main.py`
   - Dieses Skript lädt die Rohdaten, bereitet sie auf und erzeugt die verarbeiteten CSV-Dateien sowie die Grafiken im Ordner [output](output).

3. Report erzeugen
   - `quarto render gender_im_film_1.qmd --to pdf`
   - Dadurch wird der Quarto-Report als PDF erstellt.

### Erwartete Ausgaben

- Verarbeitete Daten in [output/data](output/data)
- Diagramme in [output/charts](output/charts)
- Quarto-Report als PDF im Projektordner

## Aufbau und Struktur des Repositories

- [main.py](main.py) – Hauptskript zur Datenaufbereitung und Generierung der Visualisierungen
- [src/process.py](src/process.py) – Einlesen, Zusammenführen und Aufbereiten der Daten
- [src/visualize.py](src/visualize.py) – Erzeugung der Diagramme
- [src/config.py](src/config.py) – Konfigurationen für Genre-Mapping und Diagramme
- [gender_im_film_1.qmd](gender_im_film_1.qmd) – Quarto-Report mit Einleitung, Methodik und Ergebnissen
- [data_raw_1](data_raw_1) – Rohdaten zu Genre- und Filmzuordnungen
- [data_raw_2](data_raw_2) – Rohdaten zu aggregierten Jahreszahlen
- [output](output) – erzeugte Daten und Grafiken
- [references.bib](references.bib) – Literaturverzeichnis für den Report
- [gender_im_film_cache](gender_im_film_cache) – Cache-Dateien für die Quarto-Erzeugung

## Mitwirkende

Dieses Projekt wurde von folgenden Personen erstellt:

- Janis Müller
- Veronika Ni
- Lea Nettersheim

## Kurzfassung der Fragestellung

Die zentrale Forschungsfrage lautet: Sind Schauspielerinnen in US-Filmproduktionen über verschiedene Genres hinweg systematisch unterrepräsentiert? Die Analyse untersucht diese Frage über einen Zeitraum von 2016 bis 2025 und ergänzt quantitative Auswertungen um eine reflektierte Einordnung im Kontext von Gender Bias und kulturellen Genre-Normen.