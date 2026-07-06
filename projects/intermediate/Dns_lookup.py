"""Simple DNS lookup utility for checking a domain and common subdomains."""

import socket


def resolve_domain(domain: str) -> str:
    """Resolve a primary domain to an IP address."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as exc:
        raise ValueError(f"Unable to resolve domain: {domain}") from exc


def scan_subdomains(domain: str, wordlist=None) -> list[tuple[str, str]]:
    """Try common subdomains and return any that resolve successfully."""
    if wordlist is None:
        wordlist = ["www", "mail", "ftp", "api", "dev", "admin", "vpn", "test"]

    found = []
    for word in wordlist:
        subdomain = f"{word}.{domain}"
        try:
            ip_address = socket.gethostbyname(subdomain)
            found.append((subdomain, ip_address))
        except socket.gaierror:
            continue
    return found


def main() -> None:
    print("=======================")
    print("Ysec DNS Lookup v1.1")
    print("=======================")

    domain = input("Enter domain: ").strip()
    if not domain:
        print("A domain name is required.")
        return

    print(f"Target: {domain}")

    try:
        ip_address = resolve_domain(domain)
    except ValueError as exc:
        print(exc)
        return

    print(f"IP address of {domain}: {ip_address}")

    print("Resolving common subdomains...")
    found_subdomains = scan_subdomains(domain)
    if found_subdomains:
        for subdomain, sub_ip in found_subdomains:
            print(f"Found subdomain: {subdomain} -> {sub_ip}")
    else:
        print("No common subdomains were found.")

    try:
        host, aliases, addresses = socket.gethostbyaddr(ip_address)
        print(f"Hostname of {ip_address}: {host} aliases: {aliases} addresses: {addresses}")
    except socket.herror:
        print("No reverse hostname found.")


if __name__ == "__main__":
    main()


