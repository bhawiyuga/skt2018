#Import xmlrpc client
import xmlrpc.client

# Koneksikan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

# Panggil fungsinya
hasil = proxy.penjumlahan(20, 10)
print(hasil)