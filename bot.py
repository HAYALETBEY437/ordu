import socket
import time

# BU AYARLARI MILIMETRIK KONTROL ET
HOST = "usb-metallic.gl.joinmc.link"
PORT = 22250  # nslookup ile bulduğumuz gerçek port

def mars_bas():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"[*] Kışlaya bağlanılıyor... {HOST}:{PORT}")
            s.connect((HOST, PORT))
            print("[+] KISLAYA GIRILDI! Emir bekleniyor...")
            
            # Bağlantı kopmasın diye bekliyoruz
            while True:
                data = s.recv(1024)
                if not data: break
                print(f"[*] CNC'den mesaj: {data.decode()}")
        except Exception as e:
            # Hata neyse onu görelim: Connection Refused mı, Timeout mu?
            print(f"[-] Giriş Başarısız: {e}")
            time.sleep(5)

if __name__ == "__main__":
    mars_bas()
