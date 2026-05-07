from datetime import datetime
from core.ai_assistant import generate_ai_explanation


def count_risks(findings):
    risk_count = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    for finding in findings:
        risk = finding.get("risk", "Low")
        if risk in risk_count:
            risk_count[risk] += 1

    return risk_count


def create_markdown_report(findings, output_path, target_info, attack_paths, network_analysis):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    risk_count = count_risks(findings)

    content = "# Mini Mythos Security Assessment Report\n\n"
    content += f"Erstellt am: {now}\n\n"

    content += "---\n\n"

    content += "## 1. Executive Summary\n\n"
    content += (
        "Dieser Bericht basiert auf einem Nmap-Service-Scan und bewertet "
        "offene Dienste, mögliche Angriffspfade, Infrastruktur-Kontext "
        "und defensive Maßnahmen.\n\n"
    )
    content += f"- Gefundene offene Dienste: {len(findings)}\n"
    content += f"- Critical Findings: {risk_count['Critical']}\n"
    content += f"- High Findings: {risk_count['High']}\n"
    content += f"- Medium Findings: {risk_count['Medium']}\n"
    content += f"- Low Findings: {risk_count['Low']}\n\n"

    content += "---\n\n"

    content += "## 2. Infrastructure Overview\n\n"
    content += f"- Hostname: {target_info['hostname']}\n"
    content += f"- IP-Adresse: {target_info['ip']}\n"
    content += f"- Betriebssystem: {target_info['os']}\n"
    content += f"- MAC/Hersteller: {target_info['mac']}\n\n"

    content += "### Netzwerk-Analyse\n\n"

    if network_analysis:
        for item in network_analysis:
            content += f"- {item}\n"
    else:
        content += "- Keine Netzwerk-Analyse verfügbar\n"

    content += "\n---\n\n"

    content += "## 3. Top Priorities\n\n"

    top_targets_found = False

    for finding in findings:
        if finding.get("priority") in ["High", "Critical"]:
            top_targets_found = True
            content += f"- Port {finding['port']} ({finding['service']}) → {finding['priority']}\n"

    if not top_targets_found:
        content += "Keine High- oder Critical-Prioritäten erkannt.\n"

    content += "\n---\n\n"

    content += "## 4. Security Findings\n\n"

    for finding in findings:
        content += f"### Port {finding['port']} - {finding['service']}\n\n"
        content += f"- Status: {finding['state']}\n"
        content += f"- Version: {finding['version']}\n"
        content += f"- Risiko: {finding['risk']}\n"
        content += f"- Priorität: {finding['priority']}\n"
        content += f"- Empfehlung: {finding['recommendation']}\n"
        content += f"- Pentest-Hinweis: {finding['pentest_hint']}\n"
        content += f"- KI-Erklärung: {generate_ai_explanation(finding)}\n"

        if finding.get("notes"):
            content += "- Hinweise:\n"
            for note in finding["notes"]:
                content += f"  - {note}\n"

        content += "\n"

    content += "---\n\n"

    content += "## 5. Attack Path Simulation\n\n"

    if attack_paths:
        for path in attack_paths:
            content += f"### {path['service']}\n\n"
            content += "Möglicher Angreiferpfad:\n\n"

            for step in path["attack_path"]:
                content += f"- {step}\n"

            content += "\n"
    else:
        content += "Keine spezifischen Angriffspfade erkannt.\n\n"

    content += "---\n\n"

    content += "## 6. Defensive Recommendations\n\n"

    if attack_paths:
        for path in attack_paths:
            content += f"### {path['service']}\n\n"

            for defense in path["defense"]:
                content += f"- {defense}\n"

            content += "\n"
    else:
        content += "Keine spezifischen defensiven Maßnahmen abgeleitet.\n\n"

    content += "---\n\n"

    content += "## 7. Next Steps\n\n"
    content += "- Ergebnisse manuell validieren\n"
    content += "- Kritische Dienste priorisiert prüfen\n"
    content += "- Nicht benötigte Dienste deaktivieren\n"
    content += "- Netzwerksegmentierung bewerten\n"
    content += "- Hardening-Maßnahmen dokumentieren\n"
    content += "- Nach Änderungen erneuten Scan durchführen\n\n"

    content += "---\n\n"

    content += "## Hinweis\n\n"
    content += (
        "Dieser Bericht dient ausschließlich der Analyse in einer kontrollierten "
        "Homelab- oder autorisierten Umgebung.\n"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)