# Changelog

Alle wichtigen Änderungen am Projekt werden hier dokumentiert.

---

## Version 4.2

### Hinzugefügt
- Infrastructure Layer erweitert
- `host_inventory.py` hinzugefügt
- automatische Rollen-Erkennung für Zielsysteme
- offene Dienste werden als Host-Inventar dokumentiert

### Verbessert
- `main.py` als zentraler Orchestrator stabilisiert
- Report-Engine an neue Module angepasst
- Refactor-Branch konsolidiert

---

## Version 4.1

### Hinzugefügt
- `network_analysis.py` hinzugefügt
- einfache Netzwerk-Analyse integriert
- Erkennung privater Netzbereiche
- Homelab-/internes Netzwerk wird im Report erwähnt

---

## Version 4.0

### Plattform-Restrukturierung
- Projekt von einem einfachen Pentest-Tool zu einer modularen Security- und Infrastructure-Analysis-Plattform weiterentwickelt
- modulare Architektur eingeführt
- neue Modulstruktur aufgebaut:
  - core
  - security
  - automation
  - infrastructure

### Architektur
- Parser in eigenes Core-Modul verschoben
- Report-Engine modularisiert
- KI-Modul modularisiert
- Analyzer in Security-Modul ausgelagert
- automatische KI-Initialisierung in eigenes Automation-Modul verschoben

### Security Features
- Angriffspfad-Simulation hinzugefügt
- defensive Empfehlungen integriert
- Security Findings erweitert
- Priorisierung verbessert

### Reporting
- Report komplett restrukturiert
- neue Bereiche:
  - Executive Summary
  - Infrastructure Overview
  - Host Inventory
  - Security Findings
  - Attack Path Simulation
  - Defensive Recommendations
  - Next Steps

### Infrastruktur-Analyse
- automatische Zielerkennung verbessert
- Erkennung von:
  - Hostname
  - IP-Adresse
  - Betriebssystem
  - MAC-Adresse

---

## Version 3.1

### Hinzugefügt
- automatische Zielerkennung aus Nmap-Scans
- Erkennung von IP-Adresse, Hostname, Betriebssystem und MAC-Adresse

### Verbessert
- dynamischer Zielsystem-Block im Report
- vereinfachte Scan-Datei (`scan.txt`)

---

## Version 3.0

### Hinzugefügt
- KI-Modul über Ollama
- KI-gestützte Erklärungen
- automatische KI-Initialisierung
- automatischer Modell-Check

### Technologien
- Ollama
- Requests

---

## Version 2.2

### Hinzugefügt
- Pentest-Hinweise
- Priorisierung von Diensten
- Top-Targets im Report

### Verbessert
- Risikoanalyse erweitert

---

## Version 2.1

### Hinzugefügt
- CLI-Dateiauswahl

---

## Version 2.0

### Hinzugefügt
- Analyse realer Metasploitable-Scans
- verbesserte Risikoanalyse

---

## Version 1.0

### Erstes Release
- Projektstruktur erstellt
- Parser implementiert
- Report-Generator erstellt
- erste Analyse-Logik