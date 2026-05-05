import subprocess
import requests
import time


def is_ollama_running():
    try:
        requests.get("http://localhost:11434")
        return True
    except:
        return False


def start_ollama():
    print("[+] Starte Ollama...")

    try:
        subprocess.Popen(["ollama", "serve"], shell=True)
        time.sleep(3)
    except Exception as e:
        print(f"[!] Fehler beim Starten von Ollama: {e}")


def ensure_model():
    print("[+] Prüfe Modell...")

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )

        if "llama3" not in result.stdout:
            print("[+] Lade Modell llama3...")
            subprocess.run(["ollama", "pull", "llama3"])
        else:
            print("[+] Modell vorhanden")

    except Exception as e:
        print(f"[!] Fehler beim Modell-Check: {e}")


def setup_ai():
    if not is_ollama_running():
        start_ollama()
    else:
        print("[+] Ollama läuft bereits")

    ensure_model()