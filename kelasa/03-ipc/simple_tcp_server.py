import socket

# Inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind di IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )

# Listen sebanyak x permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_addr = tcp_sock.accept()
    # Baca data dari client
    data = conn.recv(100)
    # Ubah string
    data = data.decode('ascii')
    data = "OK "+data
    # Kirim data ke client
    conn.send(data.encode('ascii'))
    # Tutup koneksi
    conn.close()
