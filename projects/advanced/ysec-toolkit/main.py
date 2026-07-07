from dns_lookup import dns_lookup
from scanner import threaded_scan
from banner import grab_banner
from http_header import http_banner

print("========================")
print("YSec Toolkit v1.1")
print("========================")

while True:
    print("\n1. DNS Lookup")
    print("2. Port Scan")
    print("3. Banner Grab")
    print("4. HTTP Headers")
    print("5. Exit")

    choice = input("Choice: ").strip()

    if choice == "1":
        target = input("Enter target: ").strip()
        dns_lookup(target)

    elif choice == "2":
        target = input("Enter target: ").strip()
        threaded_scan(target)

    elif choice == "3":
        host = input("Enter host: ").strip()
        port = int(input("Enter port: ").strip())
        print(grab_banner(host, port))

    elif choice == "4":
        target = input("Enter target: ").strip()
        port = int(input("Enter port (default 80): ").strip() or 80)
        print(http_banner(target, port))

    elif choice == "5":
        break

    else:
        print("Invalid choice.")