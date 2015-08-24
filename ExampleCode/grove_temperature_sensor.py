#   The argument in the read_temperature() method defines which Grove board(Grove Temperature Sensor) version you have connected.
#   Defaults to 'v1.2'. eg.
#       temp = read_temperature('v1.0')          # B value = 3975
#       temp = read_temperature('v1.1')          # B value = 4250
#       temp = read_temperature('v1.2')          # B value = 4250


#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import math
from logo import print_seeedstudio
import grove_i2c_adc
import Adafruit_BBIO.GPIO as GPIO

# Connect the Grove Buzzer to GPIO P9_22
BUZZER = "P9_22"            # GPIO P9_22
GPIO.setup(BUZZER, GPIO.OUT)

# The threshold to turn the buzzer on 28 Celsius
THRESHOLD_TEMPERATURE = 28

adc = grove_i2c_adc.I2cAdc()

def read_temperature(model = 'v1.2'):
    "Read temperature values in Celsius from Grove Temperature Sensor"
    # each of the sensor revisions use different thermistors, each with their own B value constant
    if model == 'v1.2':
        bValue = 4250  # sensor v1.2 uses thermistor ??? (assuming NCP18WF104F03RC until SeeedStudio clarifies)
    elif model == 'v1.1':
        bValue = 4250  # sensor v1.1 uses thermistor NCP18WF104F03RC
    else:
        bValue = 3975  # sensor v1.0 uses thermistor TTC3A103*39H

    total_value = 0
    for index in range(20):
        sensor_value = adc.read_adc()
        total_value += sensor_value
        time.sleep(0.05)
    average_value = float(total_value / 20)

    sensor_value_tmp = (float)(average_value / 3.214)
    resistance = (float)(1023 - sensor_value_tmp) * 10000 / sensor_value_tmp
    temperature = round((float)(1 / (math.log(resistance / 10000) / bValue + 1 / 298.15) - 273.15), 2)
    return temperature

# Function: If the temperature sensor senses the temperature that is up to the threshold you set in the code, the buzzer is ringing for 1s.
# Hardware: Grove - Temperature Sensor, Grove - Buzzer
if __name__== '__main__':
    print_seeedstudio()

    while True:
        try:
            # Read sensor value from Grove Sound Sensor
            temperature = read_temperature('v1.2')
            
            # When the temperature reached predetermined value, buzzer is ringing.
            if temperature > THRESHOLD_TEMPERATURE:
                # Send HIGH to switch on BUZZER
                GPIO.output(BUZZER, GPIO.HIGH)
            else:
                # Send LOW to switch off BUZZER
                GPIO.output(BUZZER, GPIO.LOW)
            
            print "temperature = ", temperature
            
        except KeyboardInterrupt:
            GPIO.output(BUZZER, GPIO.LOW)
            break

        except IOError:
            print "Error"

