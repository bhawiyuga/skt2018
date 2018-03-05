import socket

# Inisiasi objek socket UDP/IPv4
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Kirim data
data = "Hello"
server_addr = ("127.0.0.1", 6666)
udp_sock.sendto( data.encode('ascii'), server_addr )
# Terima data dari server
data = udp_sock.recv(100)
data = data.decode('ascii')
# Cetak data
print(data)