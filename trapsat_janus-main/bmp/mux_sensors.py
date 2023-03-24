import board
import busio

import Adafruit_BMP.BMP085 as BMP085
import smbus2

rpi_bus_number = 1
multiplexer_address = 0x70

I2C_ch_0 = 0B00000001
I2C_ch_1 = 0B00000010
I2C_ch_2 = 0B00000100
I2C_ch_3 = 0B00001000
I2C_ch_4 = 0B00010000
I2C_ch_5 = 0B00100000
I2C_ch_6 = 0B01000000
I2C_ch_7 = 0B10000000

bus = smbus2.SMBus(rpi_bus_number)
i2c = busio.I2C(board.SCL,board.SDA)
sensor = BMP085.BMP085()

bus.write_byte(multiplexer_address, I2C_ch_0)
print("Sensor 1: ")
print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))


bus.write_byte(multiplexer_address, I2C_ch_1)
print("Sensor 2: ")
print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))


