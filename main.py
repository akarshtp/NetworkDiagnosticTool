import subprocess
from datetime import datetime
from net_utils.port_check import check_port
from net_utils.traceroute_check import traceroute

# Log writer
def write_log(message):
    filename = f"results/log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, 'a') as f:
        f.write(message + "\n")

# Ping function with log
def ping_host(host):
    try:
        output = subprocess.check_output(["ping", "-n", "4", host], universal_newlines=True)
        message = f"Ping success to {host}:\n{output}"
    except subprocess.CalledProcessError:
        message = f"Ping failed for {host}"
    
    print(message)
    write_log(message)

# ---- MAIN EXECUTION ----
if __name__ == "__main__":
    # Run diagnostics
    ping_host("google.com")

    port_result = check_port("google.com", 443)
    print(port_result)
    write_log(port_result)

    trace_result = traceroute("google.com")
    print(trace_result)
    write_log(trace_result)
