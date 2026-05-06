import os

from parser import parse_nmap_file, parse_target_info
from analyzer import analyze_findings
from report import create_markdown_report
from setup_ai import setup_ai


def main():
    scan_dir = "scans"
    report_dir = "reports"

    print("[+] Initialisiere KI...")
    setup_ai()

    print("[+] Mini-Mythos startet...")

    input_file = "scan.txt"
    input_path = os.path.join(scan_dir, input_file)

    output_file = "report.md"
    output_path = os.path.join(report_dir, output_file)

    print(f"[+] Analysiere: {input_file}")

    findings = parse_nmap_file(input_path)

    if not findings:
        print("[!] Keine verwertbaren Daten gefunden.")
        return

    target_info = parse_target_info(input_path)

    analyzed_findings = analyze_findings(findings)

    create_markdown_report(
        analyzed_findings,
        output_path,
        target_info
    )

    print(f"[+] Report erstellt: {output_path}")


if __name__ == "__main__":
    main()