"""Erzeugt den Übungsordner für den Kurs claude-grundlagen.

Alle Daten sind synthetisch (erfundene Firmen, Namen, Zahlen). Deterministisch
über random.seed(42), damit Regenerieren identische Dateien liefert.

Run: python3 generate.py  ->  schreibt ./uebungsordner/ neu.
"""

from __future__ import annotations

import csv
import random
import shutil
from pathlib import Path

random.seed(42)
ROOT = Path(__file__).parent / "uebungsordner"

FIRMEN = ["Nordlicht GmbH", "Bergmann & Sohn", "Cityfloristik Krause", "TechnikPunkt AG",
          "Bäckerei Sonnenschein", "Malermeister Vogt", "Praxis Dr. Winter", "Autohaus Klee"]
PRODUKTE = ["Beratung", "Wartungsvertrag", "Schulung", "Lizenz Basic", "Lizenz Pro", "Support-Paket"]
MONATE = [f"2025-{m:02d}" for m in range(1, 13)]


def schreibe(pfad: Path, text: str) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(text, encoding="utf-8")


def posteingang() -> None:
    d = ROOT / "posteingang"
    schreibe(d / "Scan_0034.txt", "Rechnung Nr. 2025-0187\nNordlicht GmbH\nWartungsvertrag Q1\nBetrag: 1.240,00 EUR\nZahlbar bis: 15.04.2025\n")
    schreibe(d / "scan_0035 (1).txt", "Rechnung Nr. 2025-0201\nBäckerei Sonnenschein\nSchulung Kasse\nBetrag: 380,00 EUR\nZahlbar bis: 30.04.2025\n")
    schreibe(d / "wichtig!!.txt", "Notiz vom Empfang: Frau Berger (TechnikPunkt AG) bittet um Rückruf wegen Angebot Support-Paket. Tel 0711 555 0192.\n")
    schreibe(d / "besprechung_montag.md", "# Besprechung Montag\n\n- Angebot TechnikPunkt nachfassen\n- Urlaubsplan August abstimmen\n- Neue Kaffeemaschine (ernsthaft)\n")
    schreibe(d / "IMG_beschreibung_teamtag.txt", "Fotoliste Teamtag: 14 Bilder, noch unsortiert, liegen auf der Kamera.\n")
    schreibe(d / "angebot_entwurf_v2_final_FINAL.md", "# Angebot Support-Paket (Entwurf)\n\nKunde: TechnikPunkt AG\nLeistungen: Hotline, Vor-Ort-Service, 12 Monate\nPreis: offen\n")
    schreibe(d / "todo alt.txt", "erledigt: Server-Umzug\noffen: Ablage sortieren (seit März...)\n")
    schreibe(d / "Protokoll_Teamrunde_KW12.md", "# Teamrunde KW12\n\nAnwesend: L. Brandt, S. Yilmaz, P. Okafor\nBeschluss: Ablagestruktur wird vereinheitlicht.\n")
    schreibe(d / "reisekosten_maerz.csv", "datum,zweck,betrag_eur\n2025-03-04,Kundentermin Bergmann,42.80\n2025-03-18,Messe Stuttgart,109.50\n")
    schreibe(d / "lieferschein_0442.txt", "Lieferschein 0442, Malermeister Vogt, 6x Lizenz Basic, geliefert 2025-03-21\n")
    schreibe(d / "notiz_telefonat_krause.txt", "Cityfloristik Krause verlängert Wartungsvertrag um 12 Monate. Bestätigung schicken.\n")
    schreibe(d / "entwurf_newsletter_april.md", "# Newsletter April (Entwurf)\n\nThema: Frühjahrsaktion Schulungen, 10 Prozent Rabatt bis 30.04.\n")


def projekt() -> None:
    d = ROOT / "projekt-fruehlingsfest"
    schreibe(d / "planung.md", "# Kundenevent Frühlingsfest\n\nDatum: 16.05.2025, Ort: Firmenhof\nBudget: 4.500 EUR\nOffene Punkte: Catering-Angebot, Einladungsliste, Ablaufplan\n")
    with (d / "einladungsliste.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["firma", "kontakt", "zusage"])
        for firma in FIRMEN:
            w.writerow([firma, f"kontakt@{firma.split()[0].lower()}.example", random.choice(["offen", "ja", "nein"])])
    with (d / "budgetposten.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["posten", "geplant_eur", "ist_eur"])
        for posten, plan in [("Catering", 2200), ("Musik", 600), ("Deko", 350), ("Technik", 500), ("Sonstiges", 850)]:
            w.writerow([posten, plan, round(plan * random.uniform(0.7, 1.2), 2)])


def auswertung() -> None:
    d = ROOT / "auswertung"
    d.mkdir(parents=True, exist_ok=True)
    with (d / "umsatz_2025.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["monat", "firma", "produkt", "umsatz_eur"])
        for monat in MONATE[:6]:
            for _ in range(random.randint(6, 10)):
                w.writerow([monat, random.choice(FIRMEN), random.choice(PRODUKTE), round(random.uniform(150, 4800), 2)])
    with (d / "kundenliste.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["firma", "ort", "kunde_seit", "betreuung"])
        orte = ["Stuttgart", "Esslingen", "Ludwigsburg", "Böblingen"]
        betreuer = ["L. Brandt", "S. Yilmaz", "P. Okafor"]
        for firma in FIRMEN:
            w.writerow([firma, random.choice(orte), random.choice(["2019", "2021", "2022", "2024"]), random.choice(betreuer)])


def ablage_chaos() -> None:
    d = ROOT / "ablage-chaos"
    namen = [
        "bericht_final.md", "bericht_final_v2.md", "bericht_final_v2_neu.md",
        "Unbenannt.txt", "Unbenannt (2).txt", "notizen.txt", "Notizen_NEU.txt",
        "protokoll kw 3.md", "Protokoll-KW04.md", "protokollKW05.md",
        "rechnung__0221.txt", "Rechnung 0222.txt", "RECHNUNG_0223_kopie.txt",
        "urlaub2025.csv", "Urlaubsplanung_2025_final.csv",
        "praesentation_notizen_alt.md", "praes_notizen_aktuell.md",
        "vertrag_entwurf(1).txt", "vertrag_entwurf(2).txt", "vertrag_UNTERSCHRIEBEN.txt",
        "einkaufsliste_büro.txt", "buero_einkauf_neu.txt",
        "backup_alt.txt", "temp123.txt",
    ]
    for i, name in enumerate(namen):
        schreibe(d / name, f"Synthetische Beispieldatei Nr. {i + 1} für die Aufräum-Übung. Inhalt: {random.choice(['Berichtsentwurf', 'Protokollnotiz', 'Rechnungstext', 'Planungsliste'])}, Stand {random.choice(MONATE)}.\n")


def main() -> None:
    if ROOT.exists():
        shutil.rmtree(ROOT)
    posteingang()
    projekt()
    auswertung()
    ablage_chaos()
    original = ROOT / "_original"
    for ordner in ["posteingang", "projekt-fruehlingsfest", "auswertung", "ablage-chaos"]:
        shutil.copytree(ROOT / ordner, original / ordner)
    n = sum(1 for p in ROOT.rglob("*") if p.is_file())
    print(f"uebungsordner/ erzeugt: {n} Dateien (inkl. _original-Reset-Kopie).")


if __name__ == "__main__":
    main()
