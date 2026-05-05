# Mini Mythos - Pentest Assistant

Ein Python-basiertes Tool zur Analyse von Nmap-Scans mit automatischer Risikobewertung, Priorisierung und KI-gestützten Erklärungen.

Dieses Projekt simuliert einen einfachen Pentest-Workflow und dient als Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Features

- 🔍 Einlesen von Nmap-Scan-Dateien  
- 🧠 Analyse offener Ports und Dienste  
- ⚠️ Risikobewertung (Low / Medium / High / Critical)  
- 🎯 Priorisierung von Angriffszielen (Top Targets)  
- 💣 Pentest-Hinweise für nächste Schritte  
- 🤖 KI-gestützte Erklärungen (lokal über Ollama)  
- 📄 Automatische Erstellung eines strukturierten Reports  

---

## Voraussetzungen

- Python 3.x  
- Nmap  
- Ollama (für KI-Funktion)  

Ollama Download: https://ollama.com

---

## Installation

Repository klonen:

git clone https://github.com/svenschult/mini-mythos-pentest-assistant.git
cd mini-mythos-pentest-assistant

Abhängigkeiten installieren:

pip install -r requirements.txt

Ollama starten und Modell laden:

ollama run llama3

---

## Nutzung

1. Nmap-Scan erstellen:

nmap -sV -O -oN scan.txt <ZIEL-IP>

2. Scan-Datei in den Ordner scans/ kopieren  

3. Tool starten:

python src/main.py

4. Datei auswählen → Report wird erstellt  

---

## Projektstruktur

mini-mythos-pentest-assistant
│
├── src/        → Kernlogik (Parser, Analyse, KI)
├── scans/      → Eingabedateien
├── reports/    → Ergebnisse
├── docs/       → Dokumentation
│
├── README.md
├── requirements.txt
└── .gitignore

---

## KI-Funktion

Das Tool nutzt ein lokales KI-Modell über Ollama.

Die KI:
- analysiert Services
- gibt Pentest-Einschätzungen
- schlägt nächste Schritte vor

---

## Beispiel Output

- FTP → Critical → möglicher Exploit  
- HTTP → High → Webanalyse starten  
- SSH → Medium → Passwortprüfung  

Zusätzlich:
- Priorisierung (Top Targets)
- KI-Erklärungen

---

## Roadmap

- [x] Parser  
- [x] Analyse  
- [x] CLI  
- [x] KI-Modul  
- [ ] Web UI  
- [ ] automatischer Scan  

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

Dieses Tool dient ausschließlich zu Lern- und Demonstrationszwecken in einer kontrollierten Umgebung.

Keine Nutzung gegen fremde Systeme ohne Erlaubnis.