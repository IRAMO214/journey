import socket


def http_banner(target, port=80):
    try:
        with socket.create_connection((target, port), timeout=3) as sock:
            sock.settimeout(3)
            request = f"GET / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
            sock.sendall(request.encode())
            banner = sock.recv(1024)
            return banner.decode("latin-1", errors="ignore").strip() or "No response received."
    except OSError as exc:
        return f"Error: {exc}"