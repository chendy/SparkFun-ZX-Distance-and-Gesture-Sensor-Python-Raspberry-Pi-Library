#!/usr/bin/env python

""" Basic example of retrieving the zx_sensor data, via the I2C interface of
a Rasberry Pi. Tested with Pi2. When run, prints 'x' & 'z' to console
"""

import time
# project
from zx_sensor import ZxSensor

# Initialise the ZxSensor device using the default address
zx_sensor = ZxSensor(0x10)

while (True):
    if zx_sensor.position_available():
        # display raw values:
        # print('x {0} z {1}'.format(zx_sensor.read_x(), zx_sensor.read_z()))

        # display z as console animation:
        z = zx_sensor.read_z()
        z_str = "{0:03d} ".format(int(z))
        line = "." * (int(z / 4) + 1)
        print(z_str + line)

        time.sleep(.07)
