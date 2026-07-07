import socket


def grab_banner(host, port):
    try:
        with socket.create_connection((host, port), timeout=3) as sock:
            sock.settimeout(3)
            sock.sendall(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\nConnection: close\r\n\r\n")
            banner = sock.recv(1024)
            return banner.decode("latin-1", errors="ignore").strip() or "No banner returned."
    except OSError as exc:
        return f"Error: {exc}"