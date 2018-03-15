# Import paho mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi mqtt client
pub = mqtt_client.Client()

# Koneksikan ke broker
pub.connect("127.0.0.1", 1883)

# Publish message
pub.publish("/sensor/suhu/1", "30")
pub.publish("/sensor/suhu/2", "20")
pub.publish("/sensor/humidity/1", "80%")
pub.publish("/sensor/humidity/2", "90%")
pub.publish("/sensor/co2/1", "20%")
pub.publish("/sensor/co2/2", "10%")
