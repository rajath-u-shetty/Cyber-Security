import socket
target = input("Enter IP address or domain to scan: ")
def scan_ports(target):
    print(f"Scanning target: {target}")
    for port in range(1, 1025):  # Common port range
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Set timeout for connection
            result = s.connect_ex((target, port))  # Try to connect
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break
scan_ports(target)
