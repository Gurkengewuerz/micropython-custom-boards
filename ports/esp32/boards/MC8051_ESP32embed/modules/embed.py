from micropython import const
from machine import Pin, SDCard
import neopixel

# Pin Assignments

# SPI
SPI_MOSI = const(11)
SPI_MISO = const(13)
SPI_CLK = const(12)

# I2C
I2C_SDA = const(3)
I2C_SCL = const(8)

# RGB_LED
RGB_DATA = const(42)
_rgb_led = neopixel.NeoPixel(Pin(RGB_DATA), 1)


def rgb_led(r=0, g=0, b=0):
    _rgb_led[0] = (r, g, b)
    _rgb_led.write()


# BUTTON
BUTTON = const(0)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

RTC_ALERT = const(46)
rtc_alert = Pin(RTC_ALERT, Pin.IN)

MMC_DET = const(1)
mmc_det = Pin(MMC_DET, Pin.IN)

BATT_MON_RESET = const(48)
batt_mon_reset = Pin(BATT_MON_RESET, Pin.OUT)

LDO2 = const(5)
ldo2 = Pin(LDO2, Pin.OUT)

FET = const(4)
fet = Pin(FET, Pin.OUT)

mmc = SDCard(slot=1, width=1)

MOD_AN = const(10)
MOD_RST = const(45)
MOD_CS = const(9)
MOD_RX = const(6)
MOD_TX = const(7)
MOD_INT = const(16)
MOD_PWM = const(39)
