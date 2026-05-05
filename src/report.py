from datetime import datetime


def create_markdown_report(findings, output_path):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    content = "# Mini-Mythos Pentest Report\n\n"
    content += f"Erstellt am: {now}\n\n"

    content += "## Zusammenfassung\n\n"
    content += f"Gefundene offene Dienste: {len(findings)}\n\n"

    content += "## Findings\n\n"

    for finding in findings:
        content += f"### Port {finding['port']} - {finding['service']}\n\n"
        content += f"- Status: {finding['state']}\n"
        content += f"- Version: {finding['version']}\n"
        content += f"- Risiko: {finding['risk']}\n"
        content += f"- Empfehlung: {finding['recommendation']}\n\n"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)