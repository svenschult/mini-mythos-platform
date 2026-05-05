def analyze_findings(findings):
    analyzed = []

    for finding in findings:
        service = finding["service"].lower()
        version = finding["version"].lower()
        port = finding["port"]

        risk = "Low"
        recommendation = "Dienst dokumentieren."
        pentest_hint = "Keine direkte Priorität."
        priority = "Low"
        notes = []

        # 🚨 KRITISCHE DIENSTE
        if service in ["ftp", "telnet", "rlogin", "rexec"]:
            risk = "High"
            priority = "High"
            recommendation = "Unsicherer Dienst – prüfen."
            pentest_hint = "Versuche Login mit Standard-Credentials oder Anonymous Access."
            notes.append("Klartext-Protokoll möglich")

        if service in ["mysql", "postgresql", "ms-sql-s"]:
            risk = "High"
            priority = "High"
            recommendation = "Datenbank prüfen."
            pentest_hint = "Teste Zugriff ohne Authentifizierung oder schwache Passwörter."
            notes.append("Datenbank von außen erreichbar")

        if service in ["http", "https"]:
            if risk != "High":
                risk = "Medium"
            priority = "High"
            recommendation = "Webdienst prüfen."
            pentest_hint = "Starte mit Directory Brute Force (z. B. /admin, /login)."
            notes.append("Webservice gefunden")

        if service in ["ssh"]:
            if risk == "Low":
                risk = "Medium"
            priority = "Medium"
            recommendation = "SSH prüfen."
            pentest_hint = "Teste schwache Passwörter und Konfiguration."
            notes.append("Remote Login möglich")

        if service in ["netbios-ssn", "microsoft-ds", "smb"]:
            risk = "High"
            priority = "High"
            recommendation = "SMB prüfen."
            pentest_hint = "Suche nach offenen Shares und Gastzugriff."
            notes.append("SMB-Dienst gefunden")

        # 🧨 BEKANNTE VULNERABLE VERSIONEN
        if "vsftpd 2.3.4" in version:
            risk = "Critical"
            priority = "Critical"
            pentest_hint = "Bekannter Backdoor-Exploit vorhanden (nur im Lab testen!)."
            notes.append("Exploit bekannt für diese Version")

        if "apache httpd 2.2" in version:
            if risk != "Critical":
                risk = "High"
            notes.append("Sehr alte Apache-Version")

        if "openssh 4." in version:
            notes.append("Veraltete SSH-Version")

        finding["risk"] = risk
        finding["recommendation"] = recommendation
        finding["pentest_hint"] = pentest_hint
        finding["priority"] = priority
        finding["notes"] = notes

        analyzed.append(finding)

    return analyzed