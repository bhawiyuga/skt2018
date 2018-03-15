# Import library paho mqtt
import paho.mqtt.client as mqtt_client

# Inisiasi mqtt client sebagai pub
pub = mqtt_client.Client()

# Koneksikan ke broker
pub.connect("127.0.0.1", port=1883)

# Publish message dengan topik
pub.publish("/sensor/suhu/1", "30")
pub.publish("/sensor/suhu/2", "40")
pub.publish("/sensor/humidity/1", "80%")
pub.publish("/sensor/humidity/2", "90%")