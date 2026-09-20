import socket
import ipaddress


def scan_ports(target):

    # ==========================================
    # VALIDATE IP ADDRESS
    # ==========================================

    try:
        ipaddress.ip_address(target)

    except ValueError:
        print("\n[ERROR] Invalid IP address.")
        print("Please enter a valid IPv4 address.")
        print("Example: 192.168.1.10\n")

        return None


    # ==========================================
    # PORTS TO SCAN
    # ==========================================

    ports = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS",
        445: "SMB",
        3389: "RDP"
    }

    print(f"\nScanning {target}...\n")

    results = {}


    # ==========================================
    # PORT SCANNING
    # ==========================================

    for port, service in ports.items():

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(1)

        try:

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:
                status = "OPEN"

            else:
                status = "CLOSED"

        except socket.error:
            status = "ERROR"

        finally:
            sock.close()


        results[port] = {
            "service": service,
            "status": status
        }

        print(
            f"Port {port:<5} "
            f"({service:<6}) -> {status}"
        )


    print("\nScan completed.")

    return results


# ==========================================
# DIRECT TESTING
# ==========================================

if __name__ == "__main__":

    print("=== PySec Network Scanner ===")

    target = input(
        "Enter target IP address: "
    ).strip()

    scan_ports(target)