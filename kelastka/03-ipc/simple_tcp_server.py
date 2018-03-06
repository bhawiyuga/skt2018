import socket

# Inisiasi objek socket UDP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Ikat di sebuah IP dan port
tcp_sock.bind( ("0.0.0.0", 6667) )
# Listen
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Baca data dari client
    data, client_addr = conn.recvfrom(100)
    # Konversi dari bytes menjadi string
    data = data.decode('ascii')
    data = "OK "+data
    # Kirim balik ke client
    conn.send( data.encode('ascii') )