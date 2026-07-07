import socket


def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        raise ValueError(f"Cannot resolve {target}.")


def reverse_lookup(target_ip):
    try:
        return socket.gethostbyaddr(target_ip)
    except socket.herror:
        return (f"Unknown {target_ip}", [], [])


def enumerate_subdomains(target, wordlist=None):
    if wordlist is None:
        wordlist = ["www", "mail", "ftp", "api", "dev", "admin", "vpn", "test"]

    found = []
    for word in wordlist:
        subdomain = f"{word}.{target}"
        try:
            ip_address = socket.gethostbyname(subdomain)
            found.append((subdomain, ip_address))
        except socket.gaierror:
            continue
    return found


def dns_lookup(target):
    if not target:
        print("Target is required.")
        return

    try:
        ip_address = resolve_target(target)
    except ValueError as exc:
        print(exc)
        return

    print(f"Resolved IP: {ip_address}")

    subdomains = enumerate_subdomains(target)
    if subdomains:
        print("Discovered subdomains:")
        for subdomain, sub_ip in subdomains:
            print(f"- {subdomain} -> {sub_ip}")
    else:
        print("No common subdomains were found.")

    try:
        host_info = reverse_lookup(ip_address)
        print(f"Reverse lookup: {host_info[0]}")
    except Exception:
        print("Reverse lookup failed.")