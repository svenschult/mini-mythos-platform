# Mini Mythos - Pentest Assistant

Ein einfaches Python-Tool zur Analyse von Nmap-Scans und Erstellung eines strukturierten Pentest-Reports.

## Features

- Einlesen von Nmap-Scan-Dateien
- Erkennung offener Ports und Dienste
- Einfache Risikobewertung
- Automatische Erstellung eines Reports

## Projektstruktur
- src/ → Logik (Parser, Analyse, Report)
- scans/ → Eingabedateien (Nmap Scans)
- reports/ → Generierte Reports
- docs/ → Projektdokumentation


## Beispiel

Input (Nmap Scan):
21/tcp open ftp
80/tcp open http

Output:
- Risikoanalyse der Dienste
- Empfehlungen für weitere Tests

## Nutzung

```bash
python src/main.py


## Ziel

Dieses Projekt simuliert einen einfachen automatisierten Pentest-Workflow und dient als Grundlage für zukünftige Erweiterungen (z. B. KI-Integration).

Roadmap
 Nmap Parser
 Analyse-Modul
 Report Generator
 KI-Integration
 Erweiterte Schwachstellenanalyse
 Web-Interface

##Autor

Sven Schult
