# Import library/API socket
import socket

# Inisiasi objek socket UDP/IPv4
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ikat server ke alamat IP dan port tertentu
udp_sock.bind( ("0.0.0.0", 6666) )

while True :
    # Terima data dari client
    data, client_addr = udp_sock.recvfrom(1000)
    # Decode bytes jadi string
    data = data.decode('ascii')
    # Tambah string "OK" di depan data yang diterima
    data = "OK "+data

    # Kirim balik ke client
    udp_sock.sendto( data.encode('ascii'), client_addr )




