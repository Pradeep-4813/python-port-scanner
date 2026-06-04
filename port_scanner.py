# Import socket library
import socket

# Get target from user
target = input("Enter target IP or website: ")

print(f"\nScanning target: {target}\n")

found = False

try:
    # Convert website name to IP
    target_ip = socket.gethostbyname(target)

    # Scan ports 1 to 1000
    for port in range(1, 1001):

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(0.1)

        result = scanner.connect_ex((target_ip, port))

        if result == 0:
            found = True
            print(f"Port {port} is OPEN")

        scanner.close()

    if not found:
        print("No open ports found in the scanned range.")

    print("\nScan completed.")

except socket.gaierror:
    print("Hostname could not be resolved.")

except Exception as e:
    print(f"Error: {e}")