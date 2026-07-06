import socket
import threading
import time

target = input("Enter target: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid target.")
    target = None

open_ports = []
scanned_ports = 0
print("========================")
print("Ysec scanner v1.0")
print("========================")

print(f"target: {target}")
print(f"Resolved IP: {target_ip}")


print("Scanning..")

start = time.time()

def grab_banner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        banner = sock.recv(1024)
        sock.close()
        return banner.decode().strip()
    except:
        return None



def scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    if sock.connect_ex((target_ip, port)) == 0:
        open_ports.append(port)
        banner = grab_banner(target_ip, port)
        if banner:
            print(f"Port {port} is open. Banner: {banner}")
        else:
            print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    sock.close()

threads = []

for port in range(1,101):

    t = threading.Thread(target=scan, args=(port,))

    threads.append(t)

    t.start()
    scanned_ports += 1

for t in threads:
    t.join()

end = time.time()
for port in open_ports:
    print(port)

print(f"Open ports: {len(open_ports)}")
print(f"Scan time: {end - start}")