from flask import Flask
import os

app = Flask(__name__)

# --- AYARLAR ---
# Serveo'nun verdiği uzun adresi buraya yapıştır (HTTPS kısmını sil)
TUNNEL_URL = "ddbd18f71e953411-34-6-91-209.serveousercontent.com"
TUNNEL_PORT = 80
# ---------------

@app.route('/')
def index():
    return f"{TUNNEL_URL}:{TUNNEL_PORT}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
