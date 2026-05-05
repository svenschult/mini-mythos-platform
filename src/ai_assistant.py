def generate_ai_explanation(finding):
    service = finding["service"].lower()
    risk = finding["risk"]
    priority = finding["priority"]

    explanation = f"Der Dienst {service} wurde als Risiko {risk} mit Priorität {priority} bewertet. "

    if service == "ftp":
        explanation += (
            "FTP ist häufig kritisch, weil Zugangsdaten im Klartext übertragen werden können. "
            "In einem Lab sollte geprüft werden, ob anonymer Zugriff oder schwache Zugangsdaten möglich sind."
        )

    elif service == "ssh":
        explanation += (
            "SSH ist grundsätzlich legitim, sollte aber gehärtet sein. "
            "Wichtig sind starke Passwörter, deaktivierter Root-Login und aktuelle Versionen."
        )

    elif service in ["http", "https"]:
        explanation += (
            "Webdienste sind oft ein guter Einstiegspunkt für weitere Prüfungen. "
            "Typische nächste Schritte sind Verzeichnisprüfung, Login-Bereiche und Versionsanalyse."
        )

    elif service in ["mysql", "postgresql"]:
        explanation += (
            "Ein offen erreichbarer Datenbankdienst ist sicherheitsrelevant. "
            "Es sollte geprüft werden, ob der Zugriff eingeschränkt und sauber authentifiziert ist."
        )

    elif service in ["netbios-ssn", "microsoft-ds"]:
        explanation += (
            "SMB-Dienste können Informationen über Freigaben und Benutzer preisgeben. "
            "Im Lab sollte geprüft werden, ob Gastzugriff oder offene Shares vorhanden sind."
        )

    else:
        explanation += (
            "Der Dienst sollte dokumentiert und bei Bedarf manuell weiter untersucht werden."
        )

    return explanation