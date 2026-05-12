import ipaddress


def analyze_network(target_info):
    results = []

    ip = target_info.get("ip", "")

    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            results.append("Privates Netzwerk erkannt")

        if ip.startswith("192.168."):
            results.append("Typisches Heim- oder Homelab-Netz erkannt")

        if ip.startswith("10."):
            results.append("10er Netzwerk erkannt (internes Netzwerk möglich)")

        if ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.18."):
            results.append("172er privates Netzwerk erkannt")

        results.append("Weitere interne Systeme im gleichen Netzwerk möglich")

    except Exception:
        results.append("Netzwerk-Analyse nicht möglich")

    return results