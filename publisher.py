import paho.mqtt.client as mqtt
import json

from config import BROKER, PORT, INTERVAL, TOPIC

# Define Variables
# MQTT_HOST = "localhost"
# MQTT_PORT = 1883
# MQTT_KEEPALIVE_INTERVAL = 45
# MQTT_TOPIC = "Voltage"
 
DATA=json.dumps({"smoke": "7.3","temp":  "","light": ""});
# Define on_publish event function
def on_publish(client, userdata, mid):
    print("Message Published...")
 
def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)
    client.publish(TOPIC, DATA)
 
def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    print(payload) # then you can check the value
    client.disconnect() # Got message then disconnect
 
# Initiate MQTT Client
mqttc = mqtt.Client()
 
# Register publish callback function
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message
 
# Connect with MQTT Broker
mqttc.connect(BROKER, PORT, INTERVAL)
 
# Loop forever
mqttc.loop_forever()