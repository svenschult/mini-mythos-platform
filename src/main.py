from parser import parse_nmap_file
from analyzer import analyze_findings
from report import create_markdown_report


def main():
    input_file = "scans/metasploitable_scan.txt"
    output_file = "reports/metasploitable_report.md"

    print("[+] Mini-Mythos Version 2 startet...")
    print(f"[+] Lese Scan-Datei: {input_file}")

    findings = parse_nmap_file(input_file)

    if not findings:
        print("[!] Keine offenen Dienste gefunden.")
        return

    analyzed_findings = analyze_findings(findings)
    create_markdown_report(analyzed_findings, output_file)

    print(f"[+] Gefundene Dienste: {len(analyzed_findings)}")
    print(f"[+] Report erstellt: {output_file}")


if __name__ == "__main__":
    main()