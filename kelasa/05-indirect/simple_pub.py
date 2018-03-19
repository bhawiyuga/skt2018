# Import library mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi client sebagai publisher
pub = mqtt_client.Client()

# Koneksikan ke broker
pub.connect("127.0.0.1", 1883)

# Publish message
pub.publish("/sensor/suhu/1", "30")
pub.publish("/sensor/suhu/2", "25")
pub.publish("/sensor/co/1", "20%")
pub.publish("/sensor/co/2", "5%")




