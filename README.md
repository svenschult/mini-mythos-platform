# Mini Mythos - Pentest Assistant

Ein Python-basiertes Tool zur Analyse von Nmap-Scans mit automatischer Risikobewertung, Priorisierung und KI-gestützten Erklärungen.

Das Tool nutzt ein lokales KI-Modell über Ollama und erkennt Zielsysteme automatisch aus Nmap-Scans.

Dieses Projekt dient als Portfolio-Projekt im Bereich IT-Security / Pentesting.

---

## Features

- 🔍 Analyse von Nmap-Scans  
- 🧠 Automatische Erkennung offener Dienste  
- ⚠️ Risikobewertung (Low / Medium / High / Critical)  
- 🎯 Priorisierung von Angriffszielen  
- 💣 Pentest-Hinweise  
- 🤖 KI-gestützte Erklärungen über Ollama  
- ⚙️ Automatischer Start von Ollama  
- 📦 Automatische Modellprüfung  
- 🖥️ Erkennung von:
  - Hostname
  - IP-Adresse
  - Betriebssystem
  - MAC-Adresse / Hersteller
- 📄 Automatische Report-Erstellung  

---

## Voraussetzungen

- Python 3.x  
- Nmap  
- Ollama  

Ollama Download: https://ollama.com

---

## Installation

Repository klonen:

git clone https://github.com/svenschult/mini-mythos-pentest-assistant  
cd mini-mythos-pentest-assistant  

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

- Ollama wird gestartet (falls nicht aktiv)  
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

## Projektstruktur

mini-mythos-pentest-assistant  
│  
├── src/        → Parser, Analyse, KI, Setup  
├── scans/      → Nmap-Scans  
├── reports/    → generierte Reports  
├── docs/       → Dokumentation & Screenshots  
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
- Pentest-Hinweise  
- KI-Erklärungen  
- automatische Zielerkennung  

---

## Roadmap

- [x] Parser  
- [x] Risikoanalyse  
- [x] CLI-Version  
- [x] KI-Modul  
- [x] Ollama Integration  
- [x] automatische Zielerkennung  
- [x] automatische KI-Initialisierung  
- [ ] modernes Web UI  
- [ ] automatischer Nmap-Scan  
- [ ] erweiterte Schwachstellenanalyse  
- [ ] PDF-Export  

---

## Technologien

- Python  
- Nmap  
- Ollama  
- Requests  

---

## Autor

Sven

---

## Hinweis

Dieses Tool dient ausschließlich zu Lern- und Demonstrationszwecken in einer kontrollierten Umgebung.

Keine Nutzung gegen fremde Systeme ohne ausdrückliche Erlaubnis.