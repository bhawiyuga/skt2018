# Import library flask
from flask import Flask, request
import json

# Inisiasi app flask sebagai server
app = Flask("Hello App")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi",
        "prodi" : "TIF"
    },
    {
        "nim" : 456,
        "nama" : "Budi",
        "prodi" : "TekKom"
    }
]

# Mendefinisikan fungsi yang akan menghandle method GET dengan URL '/'
@app.route('/mahasiswa', methods=['GET'])
# Kembalikan data seluruh mahasiswa
def handle_get():
    # Konversi dari list/dictionary ke string format JSON
    return json.dumps(data_mahasiswa)

# Fungsi untuk handle tambah data
@app.route('/mahasiswa', methods=['POST'])
def tambah_mahasiswa():
    # Baca body request
    nim = request.json['nim']
    nama = request.json['nama']
    # Buat dictionary baru
    mahasiswa_baru = {
        'nama' : nama,
        'nim' : nim
    }
    #Tambahkan ke list data mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    return "OK"

# Get satu mahasiswa
@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_satu_mahasiswa(id):
    return str(id)

# Jalankan server Flask
app.run(port=7777)