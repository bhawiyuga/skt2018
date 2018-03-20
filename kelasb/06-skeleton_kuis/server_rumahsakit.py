import socket
import threading
from flask import Flask, request
import paho.mqtt.client as mqtt_client

app = Flask("Web App Mahasiswa")

@app.route('/', methods=['GET'])
def hello():
    return "Hello"

def handle_message(client, object, msg):
    print("Topik : "+msg.topic+" Message : "+msg.payload.decode('ascii'))

def handle_server():
    print("Bagian Subscriber")
    # To Do : Bagian subscriber
    sub = mqtt_client.Client()
    sub.connect("127.0.0.1", 1883)
    sub.on_message = handle_message
    sub.subscribe("/sensor/1")
    sub.loop_forever()


t = threading.Thread(target=handle_server)
t.start()

print("Server HTTP run di port 7777")
app.run(port=7777)

# To Do : Bagian Subscriber