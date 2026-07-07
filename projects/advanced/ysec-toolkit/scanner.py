import json
import socket
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from banner import grab_banner

REPORTS_DIR = Path(__file__).resolve().parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


def sanitize_filename(value):
    cleaned = []
    for char in value:
        if char.isalnum() or char in {".", "_", "-"}:
            cleaned.append(char)
        else:
            cleaned.append("_")
    return "".join(cleaned) or "target"


def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return target


def scan_port(target_ip, port, timeout=1):
    try:
        with socket.create_connection((target_ip, port), timeout=timeout):
            banner = grab_banner(target_ip, port)
            return {"port": port, "open": True, "banner": banner}
    except OSError:
        return {"port": port, "open": False}


def threaded_scan(target, start_port=1, end_port=1024):
    if not target:
        print("Target is required.")
        return

    target_ip = resolve_target(target)
    print(f"Scanning {target} ({target_ip})...")

    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in range(start_port, end_port + 1)]
        for future in as_completed(futures):
            result = future.result()
            if result["open"]:
                results.append(result)

    results.sort(key=lambda item: item["port"])

    report = {
        "target": target,
        "resolved_ip": target_ip,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "open_ports": results,
    }

    report_path = REPORTS_DIR / f"{sanitize_filename(target)}.json"
    with report_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)

    print(f"Report saved to: {report_path}")

    if results:
        print("Open ports:")
        for item in results:
            print(f"- {item['port']} -> {item['banner']}")
    else:
        print("No open ports found.")


