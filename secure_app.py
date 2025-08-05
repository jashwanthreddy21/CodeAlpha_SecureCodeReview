from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

def is_internal_ip(ip):
    return re.match(r'^(127\.|10\.|192\.168\.|172\.)', ip)

@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host')
    if not host:
        return jsonify({'error': 'Missing host'}), 400

    if is_internal_ip(host):
        return jsonify({'error': 'Access to internal IPs is blocked'}), 403

    try:
        response = requests.get(f"http://{host}")
        return jsonify({
            'host': host,
            'status_code': response.status_code
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)