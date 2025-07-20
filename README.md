# HCO-CAM-Snag

A Termux-based tool that captures webcam images through the browser and sends them to your local server.

## 🔧 Setup in Termux

```bash
pkg update -y
pkg install python -y
pip install flask
git clone https://github.com/hackerscolony/HCO-CAM-Snag
cd HCO-CAM-Snag
python main.py
```

## 📂 Output

Captured images are saved as `captured_image.jpg` in the tool folder.

## 📡 Flask Server

Runs on `http://127.0.0.1:5000` and receives webcam captures via browser.

---

## 📢 Disclaimer

This tool is for **educational purposes only**. Do not use without user consent.

---

**Code by Azhar | Hackers Colony**
