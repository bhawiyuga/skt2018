# Import library http client
import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

 # Kirim request GET dengan URL "/mahasiswa"
# Inisiasi koneksi ke server
conn = http.client.HTTPConnection(ip_server, port=port_server)

def get_mahasiswa():   
    # Kirim request ke server
    conn.request('GET', '/mahasiswa')
    # Baca response nya
    response = conn.getresponse().read()
    print( response.decode('ascii') )

def tambah_mahasiswa():    
    # Definisikan headernya
    headers = {"Content-type": "application/json"}
    # Definisikan bodynya
    mahasiswa_baru = {"nim": 210, "nama": "Joni"}
    # Kirim request POST /mahasiswa
    conn.request('POST', '/mahasiswa', json.dumps(mahasiswa_baru), headers)
    # Dapatkan responsenya
    resp = conn.getresponse().read()
    print(resp)

tambah_mahasiswa()

