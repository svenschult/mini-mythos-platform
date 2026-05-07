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


def create_markdown_report(findings, output_path, target_info, attack_paths):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    risk_count = count_risks(findings)

    content = "# Mini-Mythos Pentest Report\n\n"
    content += f"Erstellt am: {now}\n\n"

    content += "## Zielsystem\n\n"
    content += f"- Hostname: {target_info['hostname']}\n"
    content += f"- IP-Adresse: {target_info['ip']}\n"
    content += f"- Betriebssystem: {target_info['os']}\n"
    content += f"- MAC/Hersteller: {target_info['mac']}\n\n"

    content += "## Zusammenfassung\n\n"
    content += "## Top Ziele (Priorität High/Critical)\n\n"

    for finding in findings:
        if finding.get("priority") in ["High", "Critical"]:
            content += f"- Port {finding['port']} ({finding['service']}) → {finding['priority']}\n"

    content += "\n"
    content += f"- Gefundene offene Dienste: {len(findings)}\n"
    content += f"- Critical: {risk_count['Critical']}\n"
    content += f"- High: {risk_count['High']}\n"
    content += f"- Medium: {risk_count['Medium']}\n"
    content += f"- Low: {risk_count['Low']}\n\n"

    content += "## Bewertung\n\n"
    content += (
        "Dieser Report basiert auf einem Nmap-Service-Scan. "
        "Die Bewertungen sind erste Hinweise und ersetzen keine manuelle Prüfung.\n\n"
    )

    content += "## Findings\n\n"

    for finding in findings:
        content += f"### Port {finding['port']} - {finding['service']}\n\n"
        content += f"- Status: {finding['state']}\n"
        content += f"- Version: {finding['version']}\n"
        content += f"- Risiko: {finding['risk']}\n"

        if finding.get("notes"):
            content += "- Hinweise:\n"
            for note in finding["notes"]:
                content += f"  - {note}\n"

        content += f"- Empfehlung: {finding['recommendation']}\n"
        content += f"- Pentest-Hinweis: {finding['pentest_hint']}\n"
        content += f"- Priorität: {finding['priority']}\n\n"
        content += f"- KI-Erklärung: {generate_ai_explanation(finding)}\n"

    content += "## Angriffspfade & Defensive Empfehlungen\n\n"

    for path in attack_paths:
        content += f"### {path['service']}\n\n"

        content += "#### Möglicher Angreiferpfad\n\n"

    for step in path["attack_path"]:
        content += f"- {step}\n"

        content += "\n#### Defensive Maßnahmen\n\n"

    for defense in path["defense"]:
        content += f"- {defense}\n"

    content += "\n"

    content += "## Nächste sinnvolle Schritte\n\n"
    content += "- Ergebnisse manuell validieren\n"
    content += "- Dienste mit hohem Risiko priorisieren\n"
    content += "- Webdienste separat untersuchen\n"
    content += "- Standardzugänge im Lab prüfen\n"
    content += "- Erkenntnisse sauber dokumentieren\n"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)