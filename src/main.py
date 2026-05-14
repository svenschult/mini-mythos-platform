import os
from datetime import datetime

from core.parser import parse_nmap_file, parse_target_info
from core.report import create_markdown_report

from security.analyzer import analyze_findings
from security.attack_paths import generate_attack_paths

from infrastructure.network_analysis import analyze_network
from infrastructure.host_inventory import create_host_inventory
from infrastructure.topology import generate_topology_notes

from compliance.nis2_mapper import (
    map_findings_to_nis2,
    calculate_nis2_statistics
)
from compliance.nis2_pdf_report import create_nis2_pdf_report

from automation.setup_ai import setup_ai


def main():
    scan_dir = "scans"
    report_dir = "reports"

    os.makedirs(report_dir, exist_ok=True)

    print("[+] Initialisiere KI...")
    setup_ai()

    print("[+] Mini Mythos Platform startet...")

    print("\n[+] Report-Auswahl")
    print("1 - Normalen Security Report erstellen")
    print("2 - NIS2 Report erstellen")
    print("3 - Beide Reports erstellen")
    print("4 - Beenden")

    choice = input("\n[?] Auswahl: ")

    create_normal_report = False
    create_nis2_report = False

    if choice == "1":
        create_normal_report = True
    elif choice == "2":
        create_nis2_report = True
    elif choice == "3":
        create_normal_report = True
        create_nis2_report = True
    elif choice == "4":
        print("[+] Programm beendet.")
        return
    else:
        print("[!] Ungültige Eingabe.")
        return

    input_file = "scan.txt"
    input_path = os.path.join(scan_dir, input_file)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    history_dir = os.path.join(report_dir, "history")
    os.makedirs(history_dir, exist_ok=True)

    output_file = f"report_{timestamp}.md"
    output_path = os.path.join(history_dir, output_file)

    print(f"\n[+] Analysiere: {input_file}")

    findings = parse_nmap_file(input_path)

    if not findings:
        print("[!] Keine verwertbaren Daten gefunden.")
        return

    target_info = parse_target_info(input_path)
    analyzed_findings = analyze_findings(findings)

    attack_paths = generate_attack_paths(analyzed_findings)
    network_analysis = analyze_network(target_info)

    host_inventory = create_host_inventory(
        target_info,
        analyzed_findings
    )

    topology_notes = generate_topology_notes(
        target_info,
        host_inventory
    )

    nis2_mapping = map_findings_to_nis2(
        analyzed_findings,
        attack_paths,
        network_analysis,
        host_inventory
    )

    nis2_statistics = calculate_nis2_statistics(
        nis2_mapping
    )

    if create_normal_report:
        create_markdown_report(
            analyzed_findings,
            output_path,
            target_info,
            attack_paths,
            network_analysis,
            host_inventory,
            topology_notes
        )

        print(f"[+] Security Report erstellt: {output_path}")

    if create_nis2_report:
        nis2_output_file = f"nis2_report_{timestamp}.pdf"

        nis2_output_path = os.path.join(
            history_dir,
            nis2_output_file
        )

        create_nis2_pdf_report(
            nis2_mapping,
            nis2_statistics,
            target_info,
            nis2_output_path
        )

        print(f"[+] NIS2 PDF Report erstellt: {nis2_output_path}")


if __name__ == "__main__":
    main()