import socket
import time

# BU IKI AYARI MILIMETRIK KONTROL ET
KISLA_HOST = "usb-metallic.gl.joinmc.link"
KISLA_PORT = 22250 # nslookup ile buldugun port

def kislaya_gir():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f"[*] Kislaya mars basiliyor... {KISLA_HOST}:{KISLA_PORT}")
            s.connect((KISLA_HOST, KISLA_PORT))
            print("[+] KISLAYA GIRILDI! Kapıdan geçtik.")
            
            # Baglanti acik kalsin diye bekliyoruz
            while True:
                data = s.recv(1024)
                if not data: break
                print(f"[*] CNC'den mesaj var: {data.decode()}")
        except Exception as e:
            print(f"[-] Kislaya girilemedi: {e}")
            time.sleep(5)

if __name__ == "__main__":
    kislaya_gir()
