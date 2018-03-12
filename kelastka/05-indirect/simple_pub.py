#Import library paho mqtt
import paho.mqtt.client as mqtt

# Inisiasi mqtt client dengan id random
mqtt_client = mqtt.Client("tes")

# Koneksikan ke broker
mqtt_client.connect("127.0.0.1", 1883)

# Publish sebuah message
mqtt_client.publish("/sensor/suhu/1", "20")
mqtt_client.publish("/sensor/suhu/2", "30")
mqtt_client.publish("/sensor/kelembaban/1", "80%")
mqtt_client.publish("/sensor/kelembaban/2", "90%")


