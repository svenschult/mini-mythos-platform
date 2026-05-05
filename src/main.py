from parser import parse_nmap_file
from analyzer import analyze_findings
from report import create_markdown_report


def main():
    input_file = "scans/example_nmap.txt"
    output_file = "reports/report.md"

    print("[+] Mini-Mythos startet...")
    print(f"[+] Lese Scan-Datei: {input_file}")

    findings = parse_nmap_file(input_file)
    analyzed_findings = analyze_findings(findings)

    create_markdown_report(analyzed_findings, output_file)

    print(f"[+] Report erstellt: {output_file}")


if __name__ == "__main__":
    main()