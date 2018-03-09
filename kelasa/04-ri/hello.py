# Import library flask
from flask import Flask, request

# Inisiasi app flask sebagai server
app = Flask("Hello App")

# Mendefinisikan fungsi yang akan menghandle method GET dengan URL '/'
@app.route('/', methods=['GET'])
def handle_get():
    return "Hello World"

# Jalankan server Flask
app.run(port=7777)