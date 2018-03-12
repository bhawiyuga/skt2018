# Import library paho mqtt
import paho.mqtt.client as mqtt

# Inisiasi mqtt
mqtt_client = mqtt.Client()

# Koneksikan ke broker
mqtt_client.connect("127.0.0.1", 1883)

# Definisikan fungsi untuk handle message
def handle_message(mqttc, obj, msg):
    print("Datanya adalah "+str(msg.payload)+" topik "+msg.topic)

# Daftarkan fungsi handle_message
mqtt_client.on_message = handle_message

# Subscribe
mqtt_client.subscribe("/sensor/+/1")
# Buat subsriber jalan terus
mqtt_client.loop_forever()