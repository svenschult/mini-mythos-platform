def map_findings_to_nis2(findings, attack_paths, network_analysis, host_inventory):
    nis2_mapping = {
        "Risk Management": [],
        "Access Control": [],
        "Cyber Hygiene": [],
        "Incident Handling": [],
        "Business Continuity": [],
        "Supply Chain / System Security": [],
        "Secure Communication": []
    }

    for finding in findings:
        service = finding.get("service", "").lower()
        risk = finding.get("risk", "Low")
        port = finding.get("port", "Unbekannt")
        version = finding.get("version", "Unbekannt")

        finding_text = f"Port {port} / {service} / Risiko: {risk} / Version: {version}"

        if risk in ["Critical", "High"]:
            nis2_mapping["Risk Management"].append(finding_text)

        if service in ["ssh", "ftp", "telnet", "netbios-ssn", "microsoft-ds"]:
            nis2_mapping["Access Control"].append(finding_text)

        if service in ["ftp", "telnet"] or "old" in version.lower():
            nis2_mapping["Cyber Hygiene"].append(finding_text)

        if service in ["http", "https"]:
            nis2_mapping["Supply Chain / System Security"].append(finding_text)

        if service in ["http", "https", "ssh"]:
            nis2_mapping["Secure Communication"].append(finding_text)

        if service in ["mysql", "postgresql", "ms-sql-s"]:
            nis2_mapping["Business Continuity"].append(finding_text)

    if attack_paths:
        nis2_mapping["Incident Handling"].append(
            "Angriffspfade erkannt: Incident-Response-Prozesse und Monitoring sollten geprüft werden."
        )

    for item in network_analysis:
        if "privates netzwerk" in item.lower() or "intern" in item.lower():
            nis2_mapping["Risk Management"].append(
                f"Netzwerk-Kontext: {item}"
            )

    roles = host_inventory.get("roles", [])
    for role in roles:
        if "Server" in role or "System" in role:
            nis2_mapping["Risk Management"].append(
                f"Erkannte Host-Rolle: {role}"
            )

    return nis2_mapping


def calculate_nis2_statistics(nis2_mapping):
    total_items = sum(len(items) for items in nis2_mapping.values())

    statistics = {}

    for category, items in nis2_mapping.items():
        count = len(items)

        if total_items == 0:
            percentage = 0
        else:
            percentage = round((count / total_items) * 100, 2)

        statistics[category] = {
            "count": count,
            "percentage": percentage
        }

    return statistics