import socket

# Inisiasi objek socket UDP/IPv4
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Ikat di sebuah IP dan port
udp_sock.bind( ("0.0.0.0", 6666) )

while True :
    # Baca data dari client
    data, client_addr = udp_sock.recvfrom(100)
    # Konversi dari bytes menjadi string
    data = data.decode('ascii')
    data = "OK "+data
    # Kirim balik ke client
    udp_sock.sendto( data.encode('ascii'), client_addr )