# Import library mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi sebagai subscriber
sub = mqtt_client.Client()

# Koneksikan ke broker
sub.connect("127.0.0.1", 1883)

# Fungsi untuk handle message yang masuk ke subscriber
def handle_message(client, object, msg):
    print("Topik : "+msg.topic+" Message : "+msg.payload.decode('ascii'))

# Daftarkan fungsi untuk handle message
sub.on_message = handle_message

# Subscribe ke sebuah topik
sub.subscribe("/sensor/#")

# Loop forever agar subscriber jalan terus
sub.loop_forever()
