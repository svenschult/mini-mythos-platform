def parse_nmap_file(file_path):
    findings = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("PORT"):
                continue

            parts = line.split()

            if len(parts) >= 3 and "/tcp" in parts[0]:
                port = parts[0]
                state = parts[1]
                service = parts[2]
                version = " ".join(parts[3:]) if len(parts) > 3 else "unknown"

                findings.append({
                    "port": port,
                    "state": state,
                    "service": service,
                    "version": version
                })

    return findings


def parse_target_info(file_path):
    target_info = {
        "ip": "Unbekannt",
        "hostname": "Unbekannt",
        "os": "Unbekannt",
        "mac": "Unbekannt"
    }

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line.startswith("Nmap scan report for"):
                value = line.replace("Nmap scan report for", "").strip()

                if "(" in value and ")" in value:
                    hostname = value.split("(")[0].strip()
                    ip = value.split("(")[1].replace(")", "").strip()

                    target_info["hostname"] = hostname
                    target_info["ip"] = ip
                else:
                    target_info["ip"] = value

            elif line.startswith("MAC Address:"):
                target_info["mac"] = line.replace("MAC Address:", "").strip()

            elif line.startswith("OS details:"):
                target_info["os"] = line.replace("OS details:", "").strip()

            elif line.startswith("Running:"):
                if target_info["os"] == "Unbekannt":
                    target_info["os"] = line.replace("Running:", "").strip()

    return target_info