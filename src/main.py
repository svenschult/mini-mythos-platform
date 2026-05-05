import os
from parser import parse_nmap_file
from analyzer import analyze_findings
from report import create_markdown_report


def list_scan_files(scan_dir):
    files = [f for f in os.listdir(scan_dir) if f.endswith(".txt")]
    return files


def choose_scan_file(files):
    print("\nVerfügbare Scan-Dateien:\n")

    for i, file in enumerate(files):
        print(f"[{i}] {file}")

    while True:
        try:
            choice = int(input("\nWähle eine Datei (Nummer): "))
            if 0 <= choice < len(files):
                return files[choice]
        except:
            pass

        print("Ungültige Eingabe. Bitte erneut versuchen.")


def main():
    scan_dir = "scans"
    report_dir = "reports"

    print("[+] Mini-Mythos Version 2.1 startet...")

    files = list_scan_files(scan_dir)

    if not files:
        print("[!] Keine Scan-Dateien gefunden.")
        return

    selected_file = choose_scan_file(files)
    input_path = os.path.join(scan_dir, selected_file)

    output_file = selected_file.replace(".txt", "_report.md")
    output_path = os.path.join(report_dir, output_file)

    print(f"\n[+] Analysiere: {selected_file}")

    findings = parse_nmap_file(input_path)

    if not findings:
        print("[!] Keine verwertbaren Daten gefunden.")
        return

    analyzed_findings = analyze_findings(findings)
    create_markdown_report(analyzed_findings, output_path)

    print(f"[+] Report erstellt: {output_path}")


if __name__ == "__main__":
    main()