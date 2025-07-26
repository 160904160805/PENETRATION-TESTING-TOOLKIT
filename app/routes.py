import os
import re
from flask import Blueprint, render_template, request, jsonify
from urllib.parse import urlparse
from .modules import port_scanner, brute_forcer

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target', '').strip()
    start_port = int(request.form.get('start_port', 21))
    end_port = int(request.form.get('end_port', 1024))
    
    # Validate IP or domain (simple regex for IPv4)
    ip_pattern = r"^(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    domain_pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$"
    
    if not (re.match(ip_pattern, target) or all(re.match(domain_pattern, part) for part in target.split("."))):
        return jsonify(["[!] Invalid target IP or domain."]), 400
    
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
        return jsonify(["[!] Invalid port range."]), 400

    open_ports = port_scanner.scan_ports_web(target, start_port, end_port)
    return jsonify(open_ports)

@routes.route('/brute', methods=['POST'])
def brute():
    from werkzeug.utils import secure_filename

    url = request.form.get('url', '').strip()
    username = request.form.get('username', '').strip()
    uploaded_file = request.files.get('wordlist')

    # Validate URL
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        return jsonify(["[!] Invalid URL, must start with http:// or https://"]), 400
    
    if not username:
        return jsonify(["[!] Username is required"]), 400

    if uploaded_file and uploaded_file.filename.endswith('.txt'):
        filename = secure_filename(uploaded_file.filename)
        upload_dir = os.path.join("app", "uploads")
        os.makedirs(upload_dir, exist_ok=True)
        wordlist_path = os.path.join(upload_dir, filename)
        uploaded_file.save(wordlist_path)

        result = brute_forcer.brute_force_web(url, username, wordlist_path)

        # Optionally delete after use
        # os.remove(wordlist_path)

        return jsonify(result)
    else:
        return jsonify(["[!] Invalid file format. Please upload a .txt wordlist file."]), 400
