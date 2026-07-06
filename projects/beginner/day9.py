import socket

target = input("Enter target:")


try:
    target_ip = socket.gethostbyname(target)
    print(f"Resolved IP: {target_ip}")
except socket.gaierror:
    print("invalid host.")
ports = [21,22,25,53,80,110,143,443]


printf("Scanning..")
open_ports = []
print("Open PORTS:")
for port in ports:
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        open_ports.append(port)
        print("PORT " +str(port)+ " is open.")
    sock.close()
    
print(f"Total open ports: {len(open_ports)}")
