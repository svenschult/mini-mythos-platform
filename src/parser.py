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