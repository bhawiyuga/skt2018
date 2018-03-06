import socket

# Inisiasi socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koneksikan client ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim string ke server
data = "Selamat Pagi"
tcp_sock.send( data.encode('ascii') )

# Baca kembalian dari server
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

# Tutup koneksi
tcp_sock.close()
