def detect_asset_role(services, versions):
    roles = []

    service_names = [service.lower() for service in services]
    version_text = " ".join(versions).lower()

    if "http" in service_names or "https" in service_names:
        roles.append("Webserver")

    if "mysql" in service_names or "postgresql" in service_names:
        roles.append("Datenbankserver")

    if "microsoft-ds" in service_names or "netbios-ssn" in service_names:
        roles.append("SMB/File-Server")

    if "ssh" in service_names:
        roles.append("Linux-/Remote-System")

    if "rdp" in version_text or "microsoft" in version_text:
        roles.append("Windows-System")

    if "domain" in version_text or "kerberos" in version_text:
        roles.append("Möglicher Domain Controller")

    if not roles:
        roles.append("Unbekannte Rolle")

    return roles


def discover_assets(findings, target_info):
    assets = []

    services = []
    versions = []

    for finding in findings:
        services.append(finding.get("service", "unknown"))
        versions.append(finding.get("version", "unknown"))

    asset = {
        "hostname": target_info.get("hostname", "Unbekannt"),
        "ip": target_info.get("ip", "Unbekannt"),
        "os": target_info.get("os", "Unbekannt"),
        "services": services,
        "roles": detect_asset_role(services, versions)
    }

    assets.append(asset)

    return assets