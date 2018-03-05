import socket

# Inisiasi objek socket UDP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim data
data = "Hello"
server_addr = ("127.0.0.1", 6667)
#Koneksi ke server
tcp_sock.connect(server_addr)
tcp_sock.sendto( data.encode('ascii'), server_addr )
# Terima data dari server
data = tcp_sock.recv(100)
data = data.decode('ascii')
# Cetak data
print(data)