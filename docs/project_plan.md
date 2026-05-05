# Projektplan - Mini Mythos Pentest Assistant

## Ziel des Projekts

Entwicklung eines Python-Tools zur automatisierten Analyse von Nmap-Scans.

Das Tool soll:
- offene Ports erkennen
- Dienste analysieren
- Risiken bewerten
- Pentest-Hinweise geben
- Reports generieren

Ziel ist ein praxisnahes Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Projektübersicht

Projektname: Mini Mythos Pentest Assistant  
Technologie: Python  
Einsatzbereich: Pentesting / IT-Security  
Umgebung: Kali Linux + Metasploitable Lab  

---

## Projektstruktur

- Parser → liest Nmap-Scan-Dateien
- Analyzer → bewertet Risiken
- Report → erstellt Markdown-Reports
- AI-Modul → erklärt Findings

---

## Meilensteine

### Version 1
- [x] Projektstruktur erstellen
- [x] Nmap-Datei einlesen
- [x] einfacher Report

### Version 2
- [x] reale Scan-Daten integrieren
- [x] Risikoanalyse verbessern
- [x] CLI-Auswahl hinzufügen
- [x] Priorisierung (Top Targets)

### Version 3
- [x] KI-Modul (lokal)
- [ ] KI über Ollama integrieren

---

## Erweiterungen (geplant)

- Web-Oberfläche
- automatischer Nmap-Scan
- erweiterte Schwachstellen-Erkennung
- Export als PDF
- mehrere Zielsysteme

---

## Risiken

- falsche Risikobewertung durch einfache Logik
- KI liefert ungenaue Ergebnisse
- Abhängigkeit von externen Tools (Nmap, Ollama)

---

## Fazit

Das Projekt dient als Lern- und Demonstrationsprojekt.

Es zeigt:
- Python-Kenntnisse
- Verständnis für IT-Security
- strukturiertes Arbeiten
- Umgang mit Analyse-Tools