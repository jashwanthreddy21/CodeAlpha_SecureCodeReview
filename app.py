from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    if not host:
        return jsonify({'status': 'error', 'message': 'Host not provided'}), 400

    try:
        print(f"[+] Pinging: {host}")
        r = requests.get(host, timeout=3)
        return jsonify({'status': 'success', 'host': host, 'response_code': r.status_code})
    except requests.exceptions.RequestException as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)