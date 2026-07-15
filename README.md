# claude-grundlagen-material

Übungsmaterial für den Kurs `claude-grundlagen` auf [kurse.kirenz.de](https://kurse.kirenz.de).

Alle Daten in diesem Repo sind synthetisch (erfundene Firmen, Namen und Zahlen). Es besteht kein Bezug zu echten Personen, Kunden oder Unternehmen.

## Download

Der fertige Übungsordner steht als ZIP im Release zur Verfügung:

https://github.com/kirenz/claude-grundlagen-material/releases/download/v1/uebungsordner-v1.zip

## Inhalt

Das ZIP enthält den Ordner `uebungsordner/` mit fünf Unterordnern:

- `posteingang/`: 12 unsortierte Alltagsdateien
- `projekt-fruehlingsfest/`: Notizen und zwei CSV-Dateien
- `auswertung/`: `umsatz_2025.csv` und `kundenliste.csv`
- `ablage-chaos/`: 24 chaotisch benannte Dateien
- `_original/`: unveränderte Reset-Kopie aller vier oben genannten Ordner

## Material erzeugen

Der Übungsordner wird nicht von Hand gepflegt, sondern per Skript erzeugt:

```bash
python3 generate.py
```

Das Skript ist deterministisch (`random.seed(42)`): ein erneuter Lauf überschreibt `uebungsordner/` und liefert identische Dateien.

## Zurücksetzen

Wurde der Übungsordner während einer Übung verändert oder umbenannt, lässt er sich über die Kopie in `_original/` zurücksetzen, indem die jeweilige Datei oder der jeweilige Ordner von dort zurückkopiert wird. Alternativ stellt ein erneuter Lauf von `python3 generate.py` den kompletten Ausgangszustand wieder her.
