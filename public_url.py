from pyngrok import ngrok
import time

# Open a tunnel to the local server
public_url = ngrok.connect(8000)
print(f"\n--- Your portfolio is now available at: ---\n\n{public_url}\n")
print("Share this URL with anyone to view your portfolio.")
print("Press Ctrl+C to stop the tunnel when you're done.\n")

try:
    # Keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Close the tunnel when Ctrl+C is pressed
    ngrok.kill()
    print("\nTunnel closed.") 