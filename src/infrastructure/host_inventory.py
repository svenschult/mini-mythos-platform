def detect_host_role(target_info, findings):
    os_info = target_info.get("os", "").lower()
    hostname = target_info.get("hostname", "").lower()

    services = [finding["service"].lower() for finding in findings]
    versions = [finding["version"].lower() for finding in findings]

    roles = []

    if "windows" in os_info or "microsoft" in " ".join(versions):
        roles.append("Windows-System")

    if "linux" in os_info or "ubuntu" in " ".join(versions) or "debian" in " ".join(versions):
        roles.append("Linux-System")

    if "http" in services or "https" in services:
        roles.append("Webserver")

    if "mysql" in services or "postgresql" in services or "ms-sql-s" in services:
        roles.append("Datenbankserver")

    if "microsoft-ds" in services or "netbios-ssn" in services:
        roles.append("File-/SMB-Server")

    if "ssh" in services:
        roles.append("Remote-Management-System")

    if "dc" in hostname or "domain" in hostname:
        roles.append("Möglicher Domain Controller")

    if not roles:
        roles.append("Rolle nicht eindeutig erkannt")

    return roles


def create_host_inventory(target_info, findings):
    inventory = {
        "hostname": target_info.get("hostname", "Unbekannt"),
        "ip": target_info.get("ip", "Unbekannt"),
        "os": target_info.get("os", "Unbekannt"),
        "mac": target_info.get("mac", "Unbekannt"),
        "roles": detect_host_role(target_info, findings),
        "open_services": []
    }

    for finding in findings:
        inventory["open_services"].append({
            "port": finding.get("port", "Unbekannt"),
            "service": finding.get("service", "Unbekannt"),
            "version": finding.get("version", "Unbekannt"),
            "risk": finding.get("risk", "Unbekannt")
        })

    return inventory