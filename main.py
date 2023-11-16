from machine import I2C
from machine import Pin, ADC
from SH1106.sh1106 import SH1106_I2C
import BMP280.bmp280 as bmp280
import time

# Sensors list
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100_000)
photoresistor = ADC(Pin(36))
photoresistor.atten(ADC.ATTN_11DB)
#display device
display = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
display.contrast(50)  # Set contrast to 50 %

#sensor temp addresses 
SENSOR_ADDR = 0x5c
SENSOR_HUMI_REG = 0
SENSOR_TEMP_REG = 2
SENSOR_CHECKSUM = 4

#bme280 sensor address and initalization 
<<<<<<< HEAD
bmp = bmp280.BMP280(i2c)
bmp.use_case(bmp280.BMP280_CASE_WEATHER)
bmp.oversample(bmp280.BMP280_OS_HIGH)
bmp.temp_os = bmp280.BMP280_TEMP_OS_8
bmp.press_os = bmp280.BMP280_PRES_OS_4
bmp.standby = bmp280.BMP280_STANDBY_250
bmp.iir = bmp280.BMP280_IIR_FILTER_2
=======
adrbme = 0x76
bus = smbus2.SMBus(1)
bmeparams = bme280.load_calibration_params(bus, adrbme)

# Network settings
WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PSWD = "TomFryza"
THINGSPEAK_API_KEY = "7A960DRYABVC0FGR"

# Create Station interface
sta_if = network.WLAN(network.STA_IF)
>>>>>>> 853263a064a5ba6408f76570075ac5ce34ff0f44

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
        display.fill(0)
        # readfrom_mem(addr, memaddr, nbytes)
        temp_val = i2c.readfrom_mem(SENSOR_ADDR, SENSOR_TEMP_REG, 4)
        display.text(f"Tempr: {temp_val[0]}.{temp_val[1]}{chr(176)}C", x=0, y=0)
        display.text(f"Humdt: {temp_val[2]}.{temp_val[3]} %", x=0, y=10)
        
        bmp.force_measure()
        display.text(f"Atm.p: {bmp.pressure/1000:2.1f} kPa", x=0, y=20)
        
        # the maximum with this voltage divider seems to be 45 so 
        display.text(f"Light: {photoresistor.read()/4096*100:3.1f} %", x=0, y=30)
        display.show()
<<<<<<< HEAD
        #time.sleep(5)
=======
        time.sleep(5)
        
        pressure = bme280.sample(bus, adrbme, bmeparamas).pressure
        display.fill(0)
        display.text("PRESSURE : ", x=0, y=0)
        display.text("{:.2f} Pascal %".format(humidity), x=0, y=10)
        display.show()
        time.sleep(5)
        
        connect_wifi()

        # Send data using a POST request
        request = urequests.post(
        'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_API_KEY,
        json={"field1":{vali2c[0]}.{vali2c[1]}, "field2": humidity,"field3": pressure},
        headers={"Content-Type": "application/json"})
        print(f"Request #{request.text} sent")
        request.close()

        disconnect_wifi()
>>>>>>> 853263a064a5ba6408f76570075ac5ce34ff0f44


except KeyboardInterrupt:
    print("Ctrl+C Pressed. Exiting...")
