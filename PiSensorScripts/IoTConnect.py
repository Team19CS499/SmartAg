# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#Import datetime
from datetime import datetime
import time

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("austin_pi")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a1fkyjx4vhssyi.iot.us-east-2.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("/home/pi/.local/lib/python2.7/site-packages/AWSIoTPythonSDK/certs/rootCA.crt", "/home/pi/.local/lib/python2.7/site-packages/AWSIoTPythonSDK/certs/0520a951e6-private.pem.key", "/home/pi/.local/lib/python2.7/site-packages/AWSIoTPythonSDK/certs/0520a951e6-certificate.pem.crt.txt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

while(True):
        myMQTTClient.connect()
        msg = '"DateTime": "{}","Date_Time": "{}", "Temperature": "{}", "Moisture": "{}", "Humidity": "{}", "Light": "{}"'.format(str(datetime.now()),str(datetime.now()),22,10,5,15)
        msg = '{'+msg+'}'
        myMQTTClient.publish("$aws/things/austin_pi/shadow/update", msg, 1)
        myMQTTClient.disconnect()
        time.sleep(10)