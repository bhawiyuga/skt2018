# Import library xmlrpc server
import xmlrpc.server

# Inisiasi servernya
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

# Definisikan procedure/fungsi yang akan dipanggil dari client
def penjumlahan(a,b):
    return (a+b)

# Daftarkan fungsi yang akan dipanggil dari client
server.register_function(penjumlahan, 'penjumlahan')
# Jalankan service servernya
server.serve_forever()