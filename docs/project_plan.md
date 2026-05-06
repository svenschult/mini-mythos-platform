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
- Zielsysteme automatisch erkennen

Ziel ist ein praxisnahes Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Projektübersicht

Projektname: Mini Mythos Pentest Assistant  
Technologie: Python  
Einsatzbereich: IT-Security / Pentesting  
Umgebung: Kali Linux + Metasploitable / Windows Server Lab  

---

## Architektur

Das Projekt besteht aus mehreren Modulen:

- Parser → liest Nmap-Scan-Dateien
- Analyzer → bewertet Risiken und Prioritäten
- Report → erstellt strukturierte Reports
- AI-Modul → generiert KI-Erklärungen
- Setup-Modul → startet Ollama automatisch und prüft Abhängigkeiten
- Target-Parser → erkennt Zielinformationen aus Nmap-Scans
- Changelog → dokumentiert Versionsänderungen

---

## Funktionsweise

1. Nmap-Scan wird erstellt
2. Scan-Datei wird eingelesen
3. Dienste werden analysiert
4. Risiken und Prioritäten werden berechnet
5. Zielsystem wird automatisch erkannt
6. KI erstellt zusätzliche Einschätzungen
7. Report wird generiert

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

### Version 3.1
- [x] automatische Zielerkennung
- [x] dynamischer Zielsystem-Block
- [x] Changelog hinzugefügt

---

## Erweiterungen (geplant)

- modernes Web UI
- automatischer Nmap-Scan
- erweiterte Schwachstellen-Erkennung
- mehrere Zielsysteme
- Export als PDF
- Dashboard mit Statistiken

---

## Risiken

- einfache Heuristik kann falsche Bewertungen liefern
- KI kann ungenaue oder allgemeine Antworten geben
- Abhängigkeit von externen Tools (Nmap, Ollama)
- lange Antwortzeiten bei großen Scans

---

## Fazit

Das Projekt dient als Lern- und Demonstrationsprojekt.

Es zeigt:

- Python-Kenntnisse
- Verständnis für IT-Security
- strukturiertes Arbeiten
- Nutzung von Analyse-Tools
- Integration von KI in reale Workflows
- Versionierung und Projektdokumentation