from flask import Flask
import os

app = Flask(__name__)

# --- AYARLAR ---
# Pinggy'nin verdiği adresi buraya yapıştır (http:// kısmını sil)
# Örnek: xuhba-34-6-91-209.run.pinggy-free.link
TUNNEL_URL = "xuhba-34-6-91-209.run.pinggy-free.link" 
TUNNEL_PORT = 10101
# ---------------

@app.route('/')
def index():
    # Botlar bu adrese gelip TUNNEL_URL ve PORT bilgisini okuyacak
    return f"{TUNNEL_URL}:{TUNNEL_PORT}"

if __name__ == "__main__":
    # Render'ın kendi portu (5000 veya otomatik atanan)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
