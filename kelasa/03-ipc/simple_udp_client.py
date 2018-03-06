import socket

# Inisiasi socket UDP/IPv4
udp_sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim string ke server
data = "Selamat Pagi"
server_addr = ("127.0.0.1", 6666)
udp_sock.sendto( data.encode('ascii'), server_addr )

# Baca kembalian dari server
data = udp_sock.recv(100)
# Ubah dari bytes jadi string
data = data.decode('ascii')
# Cetak ke layar
print(data)