# Projektplan - Mini Mythos Pentest Assistant

## Ziel des Projekts

Entwicklung eines Python-Tools zur automatisierten Analyse von Nmap-Scans.

Das Tool soll:
- offene Ports erkennen
- Dienste analysieren
- Risiken bewerten
- Pentest-Hinweise geben
- Reports generieren
- KI zur Unterstützung nutzen

Ziel ist ein praxisnahes Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Projektübersicht

Projektname: Mini Mythos Pentest Assistant  
Technologie: Python  
Einsatzbereich: IT-Security / Pentesting  
Umgebung: Kali Linux + Metasploitable Lab  

---

## Architektur

Das Projekt besteht aus mehreren Modulen:

- Parser → liest Nmap-Scan-Dateien
- Analyzer → bewertet Risiken und Prioritäten
- Report → erstellt strukturierte Reports
- AI-Modul → generiert KI-Erklärungen
- Setup-Modul → startet Ollama automatisch und prüft Abhängigkeiten

---

## Funktionsweise

1. Nmap-Scan wird erstellt (extern)
2. Scan-Datei wird eingelesen
3. Dienste werden analysiert
4. Risiken und Prioritäten werden berechnet
5. KI erstellt zusätzliche Erklärungen
6. Report wird generiert

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

### Version 2.2
- [x] Pentest-Hinweise hinzufügen
- [x] bekannte Dienste besser bewerten

### Version 3
- [x] KI-Modul (lokal)
- [x] Integration mit Ollama
- [x] automatische KI-Initialisierung

---

## Erweiterungen (geplant)

- Web-Oberfläche (Flask)
- automatischer Nmap-Scan
- erweiterte Schwachstellen-Erkennung
- mehrere Zielsysteme
- Export als PDF

---

## Risiken

- einfache Heuristik kann falsche Bewertungen liefern
- KI kann ungenaue oder allgemeine Antworten geben
- Abhängigkeit von externen Tools (Nmap, Ollama)

---

## Fazit

Das Projekt dient als Lern- und Demonstrationsprojekt.

Es zeigt:

- Python-Kenntnisse
- Verständnis für IT-Security
- strukturiertes Arbeiten
- Nutzung von Analyse-Tools
- Integration von KI in reale Workflows