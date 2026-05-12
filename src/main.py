import os

from core.parser import parse_nmap_file, parse_target_info
from core.report import create_markdown_report
from security.analyzer import analyze_findings
from security.attack_paths import generate_attack_paths
from infrastructure.network_analysis import analyze_network
from infrastructure.host_inventory import create_host_inventory
from automation.setup_ai import setup_ai
from infrastructure.topology import generate_topology_notes


def main():
    scan_dir = "scans"
    report_dir = "reports"

    os.makedirs(report_dir, exist_ok=True)

    print("[+] Initialisiere KI...")
    setup_ai()

    print("[+] Mini Mythos Platform startet...")

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
    attack_paths = generate_attack_paths(analyzed_findings)
    network_analysis = analyze_network(target_info)
    host_inventory = create_host_inventory(target_info, analyzed_findings)
    topology_notes = generate_topology_notes(target_info, host_inventory)
    
    create_markdown_report(
        analyzed_findings,
        output_path,
        target_info,
        attack_paths,
        network_analysis,
        host_inventory,
        topology_notes
    )

    print(f"[+] Report erstellt: {output_path}")


if __name__ == "__main__":
    main()