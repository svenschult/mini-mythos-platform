import os
import socket
import subprocess
import ipaddress
import shutil
import platform


def find_nmap_executable():
    if shutil.which("nmap") is not None:
        return "nmap"

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
            return path

    return None


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception:
        return None


def get_network_range(local_ip):
    try:
        network = ipaddress.ip_network(f"{local_ip}/24", strict=False)
        return str(network)
    except Exception:
        return None


def run_nmap_scan(output_path="scans/scan.txt"):
    nmap_path = find_nmap_executable()

    if not nmap_path:
        print("[!] Nmap wurde nicht gefunden.")
        print("[i] Bitte Nmap installieren oder vorhandene scans/scan.txt verwenden.")
        return False

    local_ip = get_local_ip()

    if not local_ip:
        print("[!] Lokale IP konnte nicht erkannt werden.")
        return False

    network_range = get_network_range(local_ip)

    if not network_range:
        print("[!] Netzwerkbereich konnte nicht ermittelt werden.")
        return False

    print(f"[+] Lokale IP erkannt: {local_ip}")
    print(f"[+] Erkannter Netzwerkbereich: {network_range}")

    confirm = input(
        f"[?] Dieses Netzwerk scannen? {network_range} (y/n): "
    ).lower()

    if confirm != "y":
        print("[+] Scan abgebrochen.")
        return False

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    command = [
        nmap_path,
        "-sV",
        "-O",
        "-oN",
        output_path,
        network_range
    ]

    print("[+] Starte Nmap-Scan...")
    print(f"[i] Befehl: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        print(f"[+] Scan gespeichert: {output_path}")
        return True

    except subprocess.CalledProcessError:
        print("[!] Nmap-Scan ist fehlgeschlagen.")
        return False