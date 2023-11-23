from machine import Pin, ADC, I2C
from SH1106.sh1106 import SH1106_I2C
import weatherboard
import time
import urequests

 # Network settings
WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PSWD = "TomFryza"
THINGSPEAK_API_KEY = "7A960DRYABVC0FGR"
# Initialize the board using WeatherBoard class
wb = weatherboard.WeatherBoard(WIFI_SSID, WIFI_PSWD, i2c_scl=22, i2c_sda=21, photoresistor_pin=36)
#settings of the display device
display = SH1106_I2C(128, 64, wb.i2c, addr=0x3c, rotate=180)
display.contrast(50)  # Set contrast to 50 %


#Connect to the wifi
wb.connect_wifi()

#information to stop the exectuion
print("Stop the code execution by pressing `Ctrl+C` key.")

# Create Station interface and updates it
try:
    while True:
        display.fill(0) #create a blank space
        h, t, p, l = wb.getSensorValues() #get the values from the sensors
        display.text(f"Tempr: {t}*C", x=0, y=0) #Temperature
        display.text(f"Humdt: {h} %", x=0, y=10) #Humidity
        display.text(f"Atm.p: {p} kPa", x=0, y=20) #Atmosphere
        display.text(f"Light: {l} %", x=0, y=30) #Light level
        display.show() #update the display

        # Send data using a POST request
        request = urequests.post('http://api.thingspeak.com/update?api_key=' + THINGSPEAK_API_KEY,json={"field1": {t}, "field2": {h},"field3": {p},"field 4": {l}},headers={"Content-Type": "application/json"})
        print(f"Request #{request.text} sent")
        request.close()
        
        time.sleep(5)


except KeyboardInterrupt: #User can stop the program
    wb.disconnect_wifi()
    print("Ctrl+C Pressed. Exiting...")   
    
