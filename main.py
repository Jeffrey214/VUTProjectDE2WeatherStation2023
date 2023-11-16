from machine import I2C
from machine import Pin
<<<<<<< HEAD
from SH1106.sh1106 import SH1106_I2C
=======
from sh1106 import SH1106_I2C
import bme280
>>>>>>> 0dc0aec78a885d36b682d52b730cf910701d2de3
import time

# Sensors list
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)

#display device
display = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
display.contrast(50)  # Set contrast to 50 %

#sensor temp addresses 
SENSOR_ADDR = 0x5c
SENSOR_HUMI_REG = 0
SENSOR_TEMP_REG = 2
SENSOR_CHECKSUM = 4

#bme280 sensor address and initalization 
adrbme = 0x76
bus = smbus2.SMBus(1)
bmeparams = bme280.load_calibration_params(bus, adrbme)



print("Stop the code execution by pressing `Ctrl+C` key.")
print("")
print("Scanning I2C... ", end="")
addrs = i2c.scan()
if SENSOR_ADDR in addrs:
    print(f"{hex(SENSOR_ADDR)} detected")
else:
    print("[ERROR] Sensor is not detected")

try:
    while True:
        # readfrom_mem(addr, memaddr, nbytes)
        val = i2c.readfrom_mem(SENSOR_ADDR, SENSOR_TEMP_REG, 2)
        display.fill(0)
        display.text(f"T [*C]: {val[0]}.{val[1]}", x=0, y=0)
        display.show()
        time.sleep(5)

        humidity = bme280.sample(bus, adrbme, bmeparamas).humidity
        
        display.fill(0)
        display.text("HUMIDITY: ", x=0, y=0)
        display.text("{:.2f} g %".format(humidity), x=0, y=10)
        display.show()
        time.sleep(5)
        
        pressure = bme280.sample(bus, adrbme, bmeparamas).pressure
        display.fill(0)
        display.text("PRESSURE : ", x=0, y=0)
        display.text("{:.2f} Pascal %".format(humidity), x=0, y=10)
        display.show()
        time.sleep(5)


except KeyboardInterrupt:
    print("Ctrl+C Pressed. Exiting...")
