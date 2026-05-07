def generate_attack_paths(findings):
    attack_paths = []

    for finding in findings:
        service = finding["service"].lower()
        version = finding["version"].lower()

        # FTP
        if service == "ftp":
            attack_paths.append({
                "service": "FTP",
                "attack_path": [
                    "Anonymous Login testen",
                    "schwache Zugangsdaten prüfen",
                    "Dateizugriff analysieren",
                    "mögliche Credential Exposure",
                    "laterale Bewegung"
                ],
                "defense": [
                    "FTP deaktivieren wenn nicht benötigt",
                    "SFTP statt FTP verwenden",
                    "anonyme Zugriffe deaktivieren",
                    "starke Passwörter erzwingen"
                ]
            })

        # SMB
        elif service in ["netbios-ssn", "microsoft-ds"]:
            attack_paths.append({
                "service": "SMB",
                "attack_path": [
                    "offene Shares identifizieren",
                    "Gastzugriff prüfen",
                    "Benutzerinformationen sammeln",
                    "Credential Reuse testen",
                    "laterale Bewegung im Netzwerk"
                ],
                "defense": [
                    "SMB nur intern erlauben",
                    "Gastzugriffe deaktivieren",
                    "SMB Signierung aktivieren",
                    "Netzwerk segmentieren"
                ]
            })

        # HTTP
        elif service in ["http", "https"]:
            attack_paths.append({
                "service": "HTTP",
                "attack_path": [
                    "Verzeichnisse enumerieren",
                    "Login-Bereiche identifizieren",
                    "Version analysieren",
                    "bekannte Schwachstellen prüfen",
                    "mögliche Remote Code Execution"
                ],
                "defense": [
                    "Webserver aktuell halten",
                    "unnötige Dienste deaktivieren",
                    "WAF einsetzen",
                    "Verzeichnislisting deaktivieren"
                ]
            })

        # SSH
        elif service == "ssh":
            attack_paths.append({
                "service": "SSH",
                "attack_path": [
                    "Benutzer identifizieren",
                    "Passwort-Authentifizierung prüfen",
                    "Credential Stuffing",
                    "privilegierte Zugänge suchen"
                ],
                "defense": [
                    "Root Login deaktivieren",
                    "SSH Keys verwenden",
                    "Fail2Ban einsetzen",
                    "starke Passwörter erzwingen"
                ]
            })

        # Datenbanken
        elif service in ["mysql", "postgresql"]:
            attack_paths.append({
                "service": "Database",
                "attack_path": [
                    "offene Datenbankzugriffe prüfen",
                    "schwache Credentials testen",
                    "Datenbankstruktur analysieren",
                    "sensible Informationen identifizieren"
                ],
                "defense": [
                    "Zugriff einschränken",
                    "nur interne Erreichbarkeit",
                    "starke Passwörter",
                    "Monitoring aktivieren"
                ]
            })

    return attack_paths