import random
import sys
from azure.iot.hub import IoTHubRegistryManager
import BottleSensors as bs
import Temp_sensor as tp
import bottlesSold as bb
import time

MESSAGE_COUNT = 10
AVG_WIND_SPEED = 10.0
MSG_TXT = "{\"service client sent a message\": %.2f}"

CONNECTION_STRING = "HostName=fian23-fridge-hub.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=xa0hFfvdfiVqKWa1V4tFUKDORcu4u10spAIoTO70lmE="
DEVICE_ID = "Raspberry"

def iothub_messaging():
    try:
        while True:
            # Create IoTHubRegistryManager
            registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

            for i in range(0, MESSAGE_COUNT):
                print ( 'Sending message: {0}'.format(i) )
                data = MSG_TXT % (AVG_WIND_SPEED + (random.random() * 4 + 2))

                props={}
                # optional: assign system properties
                props.update(messageId = "message_%d" % i)
                props.update(correlationId = "correlation_%d" % i)
                props.update(contentType = "application/json")
                props.update(bottles = bs.bottle_counter())
                props.update(temp = tp.TempCalc())
                props.update(count = bb.soldIndicator())

                registry_manager.send_c2d_message(DEVICE_ID, data, props)
                time.sleep(30)

    except Exception as ex:
        print ( "Unexpected error {0}", ex )
        return

    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )

if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    iothub_messaging()
