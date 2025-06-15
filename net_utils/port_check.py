import socket

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"[+] Port {port} on {host} is open.")
    except:
        print(f"[-] Port {port} on {host} is closed or unreachable.")
