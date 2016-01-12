
""" Register map and other constaints relating the zx_sensor I2C interface
"""

# Debug
DEBUG = 0

# Acceptable ZX Sensor version
ZX_MODEL_VER = 0x01

# Acceptable ZX Sensor register map
ZX_REG_MAP_VER = 0x01

# ZX Sensor register addresses
ZX_STATUS = 0x00
ZX_DRE = 0x01
ZX_DRCFG = 0x02
ZX_GESTURE = 0x04
ZX_GSPEED = 0x05
ZX_DCM = 0x06
ZX_XPOS = 0x08
ZX_ZPOS = 0x0A
ZX_LRNG = 0x0C
ZX_RRNG = 0x0E
ZX_REGVER = 0xFE
ZX_MODEL = 0xFF

# ZX Sensor bit names
DRE_RNG = 0
DRE_CRD = 1
DRE_SWP = 2
DRE_HOVER = 3
DRE_HVG = 4
DRE_EDGE = 5
DRCFG_POLARITY = 0
DRCFG_EDGE = 1
DRCFG_FORCE = 6
DRCFG_EN = 7

# ZX Sensor UART message headers
ZX_UART_END = 0xFF
ZX_UART_RANGES = 0xFE
ZX_UART_X = 0xFA
ZX_UART_Z = 0xFB
ZX_UART_GESTURE = 0xFC
ZX_UART_ID = 0xF1

# Constants
ZX_ERROR = 0xFF
MAX_X = 240
MAX_Z = 240
SET_ALL_DRE = 0b00111111

# Enumeration for possible gestures
gesture_type = {
    'RIGHT_SWIPE': 0x01,
    'LEFT_SWIPE': 0x02,
    'UP_SWIPE': 0x03,
    'NO_GESTURE': 0xFF,
}

# Enumeration for possible interrupt enables
interrupt_type = {
    'NO_INTERRUPTS': 0x00,
    'POSITION_INTERRUPTS': 0x01,
    'GESTURE_INTERRUPTS': 0x02,
    'ALL_INTERRUPTS': 0x03
}
