# Import library paho mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi client mqtt sebagai subscriber
sub = mqtt_client.Client()

# Koneksikan ke broker
sub.connect("127.0.0.1", 1883)

# Fungsi untuk handle message yang masuk
def handle_message(mqttc, obj, msg):
    # Dapatkan topik dan payloadnya
    topic = msg.topic
    payload = msg.payload
    payload = payload.decode('ascii')
    # Cetak ke layar
    print("Topik : "+topic+" Payload "+payload)

# Daftarkan fungsinya untuk event on_message
sub.on_message = handle_message

# Subscribe ke sebuah topik
sub.subscribe("/sensor/#")

# Loop forever
sub.loop_forever()