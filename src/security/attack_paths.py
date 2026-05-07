from security.defensive_recommendations import get_defensive_recommendations


def generate_attack_paths(findings):
    attack_paths = []

    for finding in findings:
        service = finding["service"].lower()

        if service == "ftp":
            steps = [
                "Anonymous Login testen",
                "schwache Zugangsdaten prüfen",
                "Dateizugriff analysieren",
                "mögliche Credential Exposure",
                "laterale Bewegung vorbereiten"
            ]

        elif service in ["netbios-ssn", "microsoft-ds"]:
            steps = [
                "offene Shares identifizieren",
                "Gastzugriff prüfen",
                "Benutzerinformationen sammeln",
                "Credential Reuse prüfen",
                "laterale Bewegung im Netzwerk bewerten"
            ]

        elif service in ["http", "https"]:
            steps = [
                "Verzeichnisse enumerieren",
                "Login-Bereiche identifizieren",
                "Version analysieren",
                "bekannte Schwachstellen prüfen",
                "mögliche Einstiegspunkte bewerten"
            ]

        elif service == "ssh":
            steps = [
                "Benutzer identifizieren",
                "Passwort-Authentifizierung prüfen",
                "Credential Reuse bewerten",
                "privilegierte Zugänge prüfen"
            ]

        elif service in ["mysql", "postgresql"]:
            steps = [
                "offene Datenbankzugriffe prüfen",
                "schwache Credentials bewerten",
                "Datenbankstruktur analysieren",
                "sensible Informationen identifizieren"
            ]

        else:
            continue

        attack_paths.append({
            "service": service.upper(),
            "attack_path": steps,
            "defense": get_defensive_recommendations(service)
        })

    return attack_paths