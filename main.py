# by nlleer.guru && intsq.xyz

import logging
from concurrent.futures import ThreadPoolExecutor
from mcstatus import JavaServer

logging.basicConfig(filename='output.txt', level=logging.INFO, format='%(message)s')

def scan_port(ip, port):
    try:
        server = JavaServer.lookup(f"{ip}:{port}")
        
        status = server.status()
        
        motd = status.description if isinstance(status.description, str) else ' '.join(status.description["text"])
        players = f"{status.players.online}/{status.players.max}"
        info = f"{ip}:{port} | {motd} | {players}"


        logging.info(info)
    except Exception:
        pass

def scan_ports(ip_range, port_range):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in ip_range:
            for port in port_range:
                executor.submit(scan_port, ip, port)

ip_range = ["62.122.213.37"]
port_range = range(18000, 30000)

scan_ports(ip_range, port_range)

# by nlleer.guru && intsq.xyz