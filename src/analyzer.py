def analyze_findings(findings):
    analyzed = []

    for finding in findings:
        service = finding["service"].lower()
        version = finding["version"].lower()
        port = finding["port"]

        risk = "Low"
        recommendation = "Dienst dokumentieren und nur weiter prüfen, wenn er für das Ziel relevant ist."
        notes = []

        if service in ["ftp", "telnet", "rlogin", "rexec"]:
            risk = "High"
            recommendation = "Unsicheren Dienst prüfen. Klartext-Protokolle sollten in produktiven Umgebungen vermieden werden."
            notes.append("Klartext-Protokoll möglich")

        if service in ["mysql", "postgresql", "ms-sql-s", "mongodb"]:
            risk = "High"
            recommendation = "Datenbankdienst prüfen: Zugriffsbeschränkung, Standardzugänge, Version und Netzwerkfreigabe kontrollieren."
            notes.append("Datenbankdienst von außen erreichbar")

        if service in ["http", "https"]:
            if risk != "High":
                risk = "Medium"
            recommendation = "Webdienst prüfen: Version, Verzeichnisse, Login-Bereiche und bekannte Fehlkonfigurationen kontrollieren."
            notes.append("Webdienst gefunden")

        if service in ["ssh"]:
            if risk == "Low":
                risk = "Medium"
            recommendation = "SSH prüfen: Version, Passwort-Login, Root-Login und Härtung kontrollieren."
            notes.append("Remote-Login-Dienst")

        if service in ["netbios-ssn", "microsoft-ds", "smb"]:
            risk = "High"
            recommendation = "SMB/Samba prüfen: Shares, Gastzugriff, Version und bekannte Schwachstellen kontrollieren."
            notes.append("Dateifreigabe-/SMB-Dienst")

        if "vsftpd 2.3.4" in version:
            risk = "Critical"
            recommendation = "Bekannte verwundbare vsftpd-Version erkannt. In einem Lab gezielt weiter untersuchen und dokumentieren."
            notes.append("Bekannte verwundbare Version: vsftpd 2.3.4")

        if "apache httpd 2.2.8" in version:
            if risk != "Critical":
                risk = "High"
            notes.append("Alte Apache-Version erkannt")

        if "openssh 4.7" in version:
            if risk == "Low":
                risk = "Medium"
            notes.append("Alte OpenSSH-Version erkannt")

        finding["risk"] = risk
        finding["recommendation"] = recommendation
        finding["notes"] = notes

        analyzed.append(finding)

    return analyzed