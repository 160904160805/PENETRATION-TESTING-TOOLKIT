import socket

# Common ports & protocols
COMMON_PORTS = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3389: 'RDP',
    3306: 'MySQL',
    8080: 'HTTP-Alt',
}

def scan_ports_web(target, start_port=21, end_port=1024):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            service = COMMON_PORTS.get(port, "Unknown")
            open_ports.append(f"✅ Port {port} is OPEN ({service})")
        except:
            continue
        finally:
            s.close()
    if not open_ports:
        open_ports.append("[No open ports found]")
    return open_ports
