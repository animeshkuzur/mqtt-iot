import paho.mqtt.client as mqtt
import json
import time

from config import BROKER, PORT, INTERVAL, TOPIC, DATA_PATH
 
DATA_SMOKE = []
DATA_TEMP = []
DATA_LIGHT = []

def on_connect(self,mosq, obj, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)
 
def on_message(mosq, obj, msg):
    print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
    data = msg.payload
    json_data = data.decode('utf-8')
    json_data = json.loads(data)
    epoch_time = int(time.time())
    dat=""
    if(json_data['smoke']):
        dat = json_data['smoke']
        temp = [epoch_time,float(dat)]
        DATA_SMOKE.append(temp)
        with open(DATA_PATH+'/smoke.json', 'w') as outfile:  
            json.dump(DATA_SMOKE, outfile)
    elif(json_data['temp']):
        dat = json_data['temp']
        temp = [epoch_time,float(dat)]
        DATA_TEMP.append(temp)
        with open(DATA_PATH+'/temp.json', 'w') as outfile:  
            json.dump(DATA_TEMP, outfile)
    else:
        dat = json_data['light']
        temp = [epoch_time,float(dat)]
        DATA_LIGHT.append(temp)
        with open(DATA_PATH+'/light.json', 'w') as outfile:  
            json.dump(DATA_LIGHT, outfile)
 
def on_subscribe(mosq, obj, mid, granted_qos):
        pass
 
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe
 
 
client.connect(BROKER, int(PORT), int(INTERVAL))
 
client.loop_forever()