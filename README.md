# Mini Mythos - Pentest Assistant

Ein Python-basiertes Tool zur Analyse von Nmap-Scans mit automatischer Risikobewertung, Priorisierung und KI-gestützten Erklärungen.

Das Tool nutzt ein lokales KI-Modell über Ollama und richtet sich beim Start automatisch selbst ein.

Dieses Projekt dient als Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Features

- 🔍 Einlesen von Nmap-Scan-Dateien  
- 🧠 Analyse offener Ports und Dienste  
- ⚠️ Risikobewertung (Low / Medium / High / Critical)  
- 🎯 Priorisierung von Angriffszielen  
- 💣 Pentest-Hinweise  
- 🤖 KI-gestützte Erklärungen (lokal)  
- ⚙️ Automatischer Start von Ollama  
- 📦 Automatisches Laden des KI-Modells  
- 📄 Report-Erstellung  

---

## Voraussetzungen

- Python 3.x  
- Nmap  
- Ollama  

Download Ollama: https://ollama.com

---

## Installation

Repository klonen:

git clone https://github.com/DEINNAME/mini-mythos-pentest-assistant.git  
cd mini-mythos-pentest-assistant  

Abhängigkeiten installieren:

pip install -r requirements.txt  

---

## Nutzung

1. Nmap-Scan erstellen:

nmap -sV -O -oN scan.txt <ZIEL-IP>

2. Scan-Datei in den Ordner scans/ kopieren  

3. Tool starten:

python src/main.py  

---

## Automatische KI-Initialisierung

Beim Start passiert automatisch:

- Ollama wird gestartet (falls nicht aktiv)  
- Modell wird geprüft  
- Modell wird geladen (falls nötig)  

Keine manuelle Einrichtung erforderlich.

---

## Projektstruktur

mini-mythos-pentest-assistant  
│  
├── src/        → Logik (Parser, Analyse, KI, Setup)  
├── scans/      → Nmap-Dateien  
├── reports/    → Ergebnisse  
├── docs/       → Dokumentation  
│  
├── README.md  
├── requirements.txt  
└── .gitignore  

---

## Beispiel Output

- FTP → Critical → möglicher Exploit  
- HTTP → High → Webanalyse starten  
- SSH → Medium → Passwortprüfung  

Zusätzlich:
- Priorisierung  
- KI-Erklärungen  
- Pentest-Hinweise  

---

## Roadmap

- [x] Parser  
- [x] Analyse  
- [x] CLI  
- [x] KI-Modul  
- [x] Auto-Setup (Ollama)  
- [ ] Web UI verbessern  
- [ ] Auto Nmap Scan  
- [ ] Erweiterte Analyse  

---

## Technologien

- Python  
- Nmap  
- Ollama  
- Requests  

---

## Autor

Sven Schult 

---

## Hinweis

Dieses Tool dient ausschließlich zu Lern- und Demonstrationszwecken.

Keine Nutzung gegen fremde Systeme ohne Erlaubnis.