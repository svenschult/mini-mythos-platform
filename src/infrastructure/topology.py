import ipaddress


def generate_topology_notes(target_info, host_inventory):
    notes = []

    ip = target_info.get("ip", "")
    roles = host_inventory.get("roles", [])

    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            notes.append("Ziel befindet sich in einem privaten Netzwerkbereich.")

        if ip.startswith("192.168."):
            notes.append("System liegt vermutlich in einem Heimnetz- oder Homelab-Segment.")

        if ip.startswith("10."):
            notes.append("System liegt vermutlich in einem größeren internen Netzwerksegment.")

    except Exception:
        notes.append("IP-Adresse konnte nicht für Topologie-Hinweise ausgewertet werden.")

    if "Windows-System" in roles:
        notes.append("Windows-Systeme können Teil einer Domänen- oder Verwaltungsstruktur sein.")

    if "File-/SMB-Server" in roles:
        notes.append("SMB/File-Server können für laterale Bewegungen besonders relevant sein.")

    if "Webserver" in roles:
        notes.append("Webserver können als Einstiegspunkt in interne Anwendungen dienen.")

    if "Datenbankserver" in roles:
        notes.append("Datenbankserver können sensible Informationen enthalten und sollten segmentiert werden.")

    if not notes:
        notes.append("Keine spezifischen Topologie-Hinweise erkannt.")

    return notes