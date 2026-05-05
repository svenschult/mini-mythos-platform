def analyze_findings(findings):
    analyzed = []

    high_risk_services = ["ftp", "mysql", "telnet", "vnc"]
    medium_risk_services = ["ssh", "http", "smb"]

    for finding in findings:
        service = finding["service"].lower()

        risk = "Low"
        recommendation = "Dokumentieren und bei Bedarf weiter prüfen."

        if service in high_risk_services:
            risk = "High"
            recommendation = "Dienst genauer prüfen. Version, Standardzugänge und bekannte Schwachstellen kontrollieren."

        elif service in medium_risk_services:
            risk = "Medium"
            recommendation = "Konfiguration, Version und mögliche Fehlkonfigurationen prüfen."

        finding["risk"] = risk
        finding["recommendation"] = recommendation

        analyzed.append(finding)

    return analyzed