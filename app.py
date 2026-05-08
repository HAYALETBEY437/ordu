from flask import Flask
import os

app = Flask(__name__)

# --- AYARLAR ---
# Localtunnel'ın verdiği adresi buraya sabitledik
TUNNEL_URL = "forty-kiwis-cross.loca.lt"
TUNNEL_PORT = 80
# ---------------

@app.route('/')
def index():
    # Botlar Render'a geldiğinde bu adresi okuyup senin panele akacaklar
    return f"{TUNNEL_URL}:{TUNNEL_PORT}"

if __name__ == "__main__":
    # Render'ın otomatik atadığı portu kullanır
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
