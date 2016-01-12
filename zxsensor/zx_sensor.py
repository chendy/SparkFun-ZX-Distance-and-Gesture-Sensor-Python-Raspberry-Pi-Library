
# standard
from __future__ import division, print_function
# external
from Adafruit_I2C import Adafruit_I2C
# project
from i2c_registers import *


class ZxSensor:
    """ Main class for interfacing with the zx_sensor
    """
    def __init__(self, address=0x10):
        self.i2c = Adafruit_I2C(address)

        print("model version", self.get_model_version())
        print(self.get_reg_map_version())
        print(self.position_available())

    def get_model_version(self):
        return self.i2c.readU8(ZX_MODEL)

    def get_reg_map_version(self):
        return self.i2c.readU8(ZX_REGVER)

    def position_available(self):
        # read STATUS register
        status = self.i2c.readU8(ZX_STATUS)
        # extract DAV bit and return
        return status & 1

    def read_x(self):
        x_pos = self.i2c.readU8(ZX_XPOS)
        if (not x_pos) or (x_pos > MAX_X):
            return ZX_ERROR
        return x_pos

    def read_z(self):
        z_pos = self.i2c.readU8(ZX_ZPOS)
        if (not z_pos) or (z_pos > MAX_Z):
            return ZX_ERROR
        return z_pos

if __name__ == '__main__':
    pass
