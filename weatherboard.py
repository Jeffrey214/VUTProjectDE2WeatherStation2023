from machine import Pin, ADC, I2C
from SH1106.sh1106 import SH1106_I2C
import BMP280.bmp280 as bmp280
import network

class WeatherBoard:
    i2c = None
    bmp = None
    dht12_sensor_addr = None
    photoresistor = None
    sta_if = None
    ssid = None
    pasw = None
    def __init__(self, wifi_ssid, wifi_pasw, i2c_scl, i2c_sda, photoresistor_pin, dht12_sensor_addr=0x5c):
        # setup wifi
        self.sta_if = network.WLAN(network.STA_IF)
        self.sta_if.active(True)
        self.ssid = wifi_ssid
        self.pasw = wifi_pasw
        # setup i2c
        self.i2c = I2C(0, scl=Pin(i2c_scl), sda=Pin(i2c_sda), freq=100_000)
        self.dht12_sensor_addr = dht12_sensor_addr
        # setup bmp280
        self.bmp = bmp280.BMP280(self.i2c)
        self.bmp.use_case(bmp280.BMP280_CASE_WEATHER)
        self.bmp.oversample(bmp280.BMP280_OS_HIGH)
        self.bmp.temp_os = bmp280.BMP280_TEMP_OS_8
        self.bmp.press_os = bmp280.BMP280_PRES_OS_4
        self.bmp.standby = bmp280.BMP280_STANDBY_250
        self.bmp.iir = bmp280.BMP280_IIR_FILTER_2
        # setup photoresistor
        self.photoresistor = ADC(Pin(photoresistor_pin))
        self.photoresistor.atten(ADC.ATTN_11DB)

    def connect_wifi(self):
        self.sta_if.connect(self.ssid, self.pasw)
    def disconnect_wifi(self):
        self.sta_if.disconnect()

    def getSensorValues(self):
        # read humidity and temperature from DHT12
        temp_val = self.i2c.readfrom_mem(self.dht12_sensor_addr, 0, 4)
        humidity = f"{temp_val[0]}.{temp_val[1]}"
        temperature = f"{temp_val[2]}.{temp_val[3]}"
        # take emasurement from BMP280 and format it
        self.bmp.force_measure()
        pressure = f"{self.bmp.pressure/1000:2.1f}"
        # take readings from photoresistor based voltage divider, process and format
        light = f"{self.photoresistor.read()/4096*100:3.1f}"
        return [humidity, temperature, pressure, light]
