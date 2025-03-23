from flask import Flask, send_from_directory
import os
import socket

app = Flask(__name__, static_folder='.')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(path):
        return send_from_directory('.', path)
    else:
        return send_from_directory('.', 'index.html')

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    ip_address = get_ip()
    print(f"\n--- Your portfolio is now available at: ---")
    print(f"Local access: http://localhost:8000")
    print(f"Network access: http://{ip_address}:8000")
    print("\nShare the Network access URL with anyone on your local network to view your portfolio.")
    print("Press Ctrl+C to stop the server when you're done.\n")
    app.run(host='0.0.0.0', port=8000, debug=False) 