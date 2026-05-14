import os
import shutil
import platform
import importlib


def check_nmap():
    if shutil.which("nmap") is not None:
        return True

    system = platform.system()

    possible_paths = []

    if system == "Windows":
        possible_paths = [
            r"C:\Program Files (x86)\Nmap\nmap.exe",
            r"C:\Program Files\Nmap\nmap.exe"
        ]

    elif system == "Linux":
        possible_paths = [
            "/usr/bin/nmap",
            "/usr/local/bin/nmap"
        ]

    elif system == "Darwin":
        possible_paths = [
            "/opt/homebrew/bin/nmap",
            "/usr/local/bin/nmap"
        ]

    for path in possible_paths:
        if os.path.exists(path):
            return True

    return False


def check_ollama():
    if shutil.which("ollama") is not None:
        return True

    system = platform.system()

    possible_paths = []

    if system == "Windows":
        possible_paths = [
            r"C:\Users\sven_\AppData\Local\Programs\Ollama\ollama.exe",
            r"C:\Program Files\Ollama\ollama.exe"
        ]

    elif system == "Linux":
        possible_paths = [
            "/usr/bin/ollama",
            "/usr/local/bin/ollama"
        ]

    elif system == "Darwin":
        possible_paths = [
            "/opt/homebrew/bin/ollama",
            "/usr/local/bin/ollama"
        ]

    for path in possible_paths:
        if os.path.exists(path):
            return True

    return False


def check_python_package(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


def run_dependency_check():
    print("\n[+] Dependency Check\n")

    dependencies = {
        "Nmap": check_nmap(),
        "Ollama": check_ollama(),
        "Requests": check_python_package("requests"),
        "Matplotlib": check_python_package("matplotlib"),
        "ReportLab": check_python_package("reportlab")
    }

    for dependency, status in dependencies.items():
        if status:
            print(f"[✓] {dependency} gefunden")
        else:
            print(f"[!] {dependency} fehlt")

    return dependencies