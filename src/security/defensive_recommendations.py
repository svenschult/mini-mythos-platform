def get_defensive_recommendations(service):
    service = service.lower()

    recommendations = {
        "ftp": [
            "FTP deaktivieren, wenn es nicht benötigt wird.",
            "SFTP oder FTPS statt FTP verwenden.",
            "Anonyme Logins deaktivieren.",
            "Starke Passwortrichtlinien erzwingen."
        ],
        "ssh": [
            "Root-Login deaktivieren.",
            "SSH-Key-Authentifizierung verwenden.",
            "Passwort-Login nach Möglichkeit deaktivieren.",
            "Fail2Ban oder ähnliche Schutzmechanismen einsetzen."
        ],
        "http": [
            "Webserver regelmäßig aktualisieren.",
            "Verzeichnislisting deaktivieren.",
            "Unnötige Webdienste entfernen.",
            "Login-Bereiche zusätzlich absichern."
        ],
        "https": [
            "TLS-Konfiguration prüfen.",
            "Zertifikate aktuell halten.",
            "Sichere Cipher Suites verwenden.",
            "Webserver regelmäßig aktualisieren."
        ],
        "mysql": [
            "Datenbank nicht öffentlich erreichbar machen.",
            "Zugriff auf interne Netze beschränken.",
            "Starke Passwörter verwenden.",
            "Datenbank-Berechtigungen regelmäßig prüfen."
        ],
        "postgresql": [
            "Datenbankzugriff einschränken.",
            "Starke Authentifizierung erzwingen.",
            "Nur notwendige Benutzerrechte vergeben.",
            "Logging und Monitoring aktivieren."
        ],
        "netbios-ssn": [
            "SMB-Gastzugriff deaktivieren.",
            "Freigaben regelmäßig prüfen.",
            "SMB-Signierung aktivieren.",
            "Netzwerksegmentierung einsetzen."
        ],
        "microsoft-ds": [
            "SMB-Gastzugriff deaktivieren.",
            "Freigaben regelmäßig prüfen.",
            "SMB-Signierung aktivieren.",
            "Netzwerksegmentierung einsetzen."
        ]
    }

    return recommendations.get(service, [
        "Dienst dokumentieren.",
        "Notwendigkeit des Dienstes prüfen.",
        "Zugriff einschränken.",
        "Version und Konfiguration regelmäßig kontrollieren."
    ])