# Import paho mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi mqtt client
sub = mqtt_client.Client()

# Koneksikan ke broker
sub.connect("127.0.0.1", 1883)

# Subscribe ke salah satu topik
sub.subscribe("/sensor/#")

# Buat fungsi untuk handle ketika ada message masuk
def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode('ascii')
    print("Topik : "+topic+" Payload : "+payload)

# Daftarkan fungsi untuk handle message masuk
sub.on_message = handle_message

# Looping supaya subscribernya tetap jalan
sub.loop_forever()
