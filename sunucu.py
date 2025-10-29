import socket

HOST = '0.0.0.0'  
PORT = 8888       

print(f"Sunucu {HOST}:{PORT} adresinde başlatılıyor...")
print("Çıkmak için CTRL+C tuşlarına basın.")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    
    while True: 
        print("\nESP32'den yeni bir bağlantı bekleniyor...")
        
        conn, addr = s.accept() 
        
        with conn:
            print(f"{addr} adresinden bağlantı kabul edildi.")
            
       
            while True:
                try:
                    data = conn.recv(1024) 
                    if not data:
                        
                        break 
                    
                    gelen_mesaj = data.decode('utf-8').strip()
                    print(f"ESP32'den 'PING' alındı: {gelen_mesaj}")
                    
                    yanit = "PONG! Sunucudan yanıt alındı."
                    conn.sendall(yanit.encode('utf-8'))
                
                except ConnectionResetError:
                    
                    break

        print(f"{addr} ile bağlantı kapatıldı.")
        