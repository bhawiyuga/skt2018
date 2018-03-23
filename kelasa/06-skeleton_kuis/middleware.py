import socket
import threading
from flask import Flask, request
import paho.mqtt.client as mqtt_client

app = Flask("Web App Mahasiswa")

def handle_server():
    print("Bagian Subscriber")
    # To Do : Bagian subscriber


t = threading.Thread(target=handle_server)
t.start()

print("Server HTTP run di port 7777")
app.run(port=7777)
# To Do : Bagian Subscriber