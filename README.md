# Mini Mythos Platform

Eine modulare Plattform für Infrastructure-, Netzwerk- und Security-Analyse mit Python, Automatisierung und KI-Unterstützung.

Mini Mythos dient als praxisnahes Homelab- und Portfolio-Projekt mit Fokus auf:

- Infrastruktur verstehen
- Netzwerke analysieren
- Security bewerten
- Angriffswege nachvollziehen
- defensive Maßnahmen ableiten
- Automatisierung und Reporting

---

## Projektziel

Mini Mythos soll langfristig zu einer modularen Security- und Infrastructure-Analysis-Plattform ausgebaut werden.

Das Projekt kombiniert:

- Python-Automatisierung
- Netzwerk-Analyse
- Security Assessment
- KI-Unterstützung
- Reporting & Dokumentation
- Homelab-Integration

---

## Features

- 🔍 Analyse von Nmap-Scans
- 🧠 automatische Zielerkennung
- ⚠️ Risikobewertung
- 🎯 Priorisierung von Angriffszielen
- 💣 Pentest-Hinweise
- 🛡️ defensive Empfehlungen
- 🤖 KI-gestützte Einschätzungen über Ollama
- ⚙️ automatische KI-Initialisierung
- 📄 automatische Report-Erstellung
- 🖥️ Erkennung von:
  - Hostname
  - IP-Adresse
  - Betriebssystem
  - MAC-Adresse / Hersteller

---

## Architektur

mini-mythos-platform
│
├── src/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── parser.py
│   │   ├── report.py
│   │   └── ai_assistant.py
│   │
│   ├── security/
│   │   └── analyzer.py
│   │
│   └── automation/
│       └── setup_ai.py
│
├── scans/
├── reports/
├── docs/
│
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore

---

## Voraussetzungen

- Python 3.x
- Nmap
- Ollama

Ollama Download:

https://ollama.com

---

## Installation

Repository klonen:

git clone https://github.com/DEINNAME/mini-mythos-platform

Projektordner öffnen:

cd mini-mythos-platform

Abhängigkeiten installieren:

pip install -r requirements.txt

---

## Nutzung

### 1. Nmap-Scan erstellen

Beispiel:

nmap -sV -O -oN scan.txt <ZIEL-IP>

Die Datei muss anschließend hier liegen:

scans/scan.txt

---

### 2. Tool starten

python src/main.py

---

## Automatische KI-Initialisierung

Beim Start passiert automatisch:

- Ollama wird gestartet
- KI-Modell wird geprüft
- Modell wird geladen (falls nötig)

Keine manuelle Einrichtung erforderlich.

---

## Automatische Zielerkennung

Mini Mythos erkennt automatisch:

- Ziel-IP
- Hostname
- Betriebssystem
- MAC-Adresse / Hersteller

direkt aus dem Nmap-Scanbericht.

---

## Security-Ansatz

Mini Mythos fokussiert sich nicht nur auf Angriffe, sondern auf das Verständnis kompletter Security-Szenarien.

Die Plattform soll zukünftig:

- mögliche Angreiferpfade simulieren
- Fehlkonfigurationen erkennen
- defensive Maßnahmen empfehlen
- Infrastruktur dokumentieren

---

## Geplante Erweiterungen

- modernes Web UI
- automatischer Nmap-Scan
- Dashboard
- Netzwerk-Topologie
- Vergleich mehrerer Scans
- PDF-Export
- erweiterte Schwachstellenanalyse
- Asset Discovery
- Hardening-Checks

---

## Technologien

- Python
- Nmap
- Ollama
- Requests
- Git / GitHub

---

## Projektstatus

Aktive Entwicklung

Der Fokus liegt aktuell auf:
- modularer Architektur
- Security-Analyse
- Homelab-Integration
- Automatisierung

---

## Autor

Sven Schult

---

## Hinweis

Dieses Projekt dient ausschließlich zu Lern-, Analyse- und Demonstrationszwecken in kontrollierten Umgebungen.

Keine Nutzung gegen fremde Systeme ohne ausdrückliche Erlaubnis.