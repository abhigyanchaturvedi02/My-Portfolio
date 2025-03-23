from flask import Flask, send_from_directory
import os
import threading
from pyngrok import ngrok
import time

# Set up Flask app
app = Flask(__name__, static_folder='.')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(path):
        return send_from_directory('.', path)
    else:
        return send_from_directory('.', 'index.html')

def run_flask():
    app.run(host='0.0.0.0', port=8000)

def run_ngrok():
    # Wait for Flask to start
    time.sleep(2)
    # Open a tunnel to the Flask server
    public_url = ngrok.connect(8000)
    print(f"\n--- Your portfolio is now available at: ---\n\n{public_url}\n")
    print("Share this URL with anyone to view your portfolio.")
    print("Press Ctrl+C to stop when you're done.\n")

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Starting Flask server...")
    
    # Start ngrok in the main thread
    try:
        run_ngrok()
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Close the tunnel when Ctrl+C is pressed
        ngrok.kill()
        print("\nServer stopped.") 