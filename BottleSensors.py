import RPi.GPIO as GPIO
import time
import Nanoleaf as nls
import json

# each sensor is a GPIO pin so it can be diffrent(in this case buttons where used).
try:
    with open("config.json", "r") as file:
        config = json.load(file)
    sensors = {}
    for x in range(1, 17):
        sensors[f"sensor{x}"] = config[f"sensor{x}"]
        print(sensors[f"sensor{x}"])
except Exception as e:
    print(e)

def setup_GPIO() -> None:
    """setup the GPIO pins."""
    try:
        GPIO.setwarnings(False) #Disable warnings
        GPIO.setmode(GPIO.BCM) #Set GPIO pin numbering
        GPIO.setup(sensor1, GPIO.IN) #Sensor 1
        GPIO.setup(sensor2, GPIO.IN) #Sensor 2
        GPIO.setup(sensor3, GPIO.IN) #Sensor 3
        GPIO.setup(sensor4, GPIO.IN) #Sensor 4
        #GPIO.setup(sensor5, GPIO.IN) #Sensor 5
        #GPIO.setup(sensor6, GPIO.IN) #Sensor 6
        #GPIO.setup(sensor7, GPIO.IN) #Sensor 7
        #GPIO.setup(sensor8, GPIO.IN) #Sensor 8
        #GPIO.setup(sensor9, GPIO.IN) #Sensor 9
        #GPIO.setup(sensor10, GPIO.IN) #Sensor 10
        #GPIO.setup(sensor11, GPIO.IN) #Sensor 11
        #GPIO.setup(sensor12, GPIO.IN) #Sensor 12
        #GPIO.setup(sensor13, GPIO.IN) #Sensor 13
        #GPIO.setup(sensor14, GPIO.IN) #Sensor 14
        #GPIO.setup(sensor15, GPIO.IN) #Sensor 15
        #GPIO.setup(sensor16, GPIO.IN) #Sensor 16
    except Exception as e:
        print(e)

def button_state(input_pin: int) -> bool:
    """returns the state of the sensor so you know if it is occupied or empty."""
    try:
        if GPIO.input(input_pin): 
            return True
        else:
            return False
    except Exception as e:
        print(e)
    
def bottle_counter() -> int:
    """counts how many bottles are in the fridge."""
    all_sensors = [sensor1, sensor2, sensor3, sensor4] #, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10, sensor11, sensor12, sensor13, sensor14, sensor15, sensor16]
    occupied_sensors = []
    try:
        for sensor in all_sensors:
            if button_state(sensor):
                if sensor not in occupied_sensors:
                    occupied_sensors.append(sensor)
            else:
                if sensor in occupied_sensors:
                    occupied_sensors.remove(sensor)
        return len(occupied_sensors)
    except Exception as e:
        print(e)