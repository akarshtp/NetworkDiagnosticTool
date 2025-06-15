import subprocess
import platform

def traceroute(host):
    command = ["tracert", host] if platform.system() == "Windows" else ["traceroute", host]
    try:
        result = subprocess.check_output(command, universal_newlines=True)
        print(result)
    except Exception as e:
        print(f"Traceroute failed: {e}")
