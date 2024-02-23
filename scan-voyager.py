import sys
import socket
from datetime import datetime
import concurrent.futures

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguments")
    print("Syntax: python3 scan-voyager.py <ip>")
    sys.exit()

print("*" * 100)
print("Scanning target " + target)
print("Time started:  " + str(datetime.now()))
print("*" * 100)

try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: scan_port(target, port), range(1, 65535))
except KeyboardInterrupt:
    print('\nExiting program')
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
