import paho.mqtt.client as mqtt


broker_address="138.36.239.25" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF") #publish





