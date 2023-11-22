from machine import Pin, ADC, I2C
import weatherboard
import time

# Network settings
WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PSWD = "TomFryza"
THINGSPEAK_API_KEY = "7A960DRYABVC0FGR"
# Initialize board class
wb = weatherboard.WeatherBoard(WIFI_SSID, WIFI_PSWD, i2c_scl=22, i2c_sda=21, photoresistor_pin=36)
#display device
display = SH1106_I2C(128, 64, i2c, addr=0x3c, rotate=180)
display.contrast(50)  # Set contrast to 50 %


# Create Station interface
wb.connect_wifi()
print("Stop the code execution by pressing `Ctrl+C` key.")

try:
    while True:
        display.fill(0)
        h, t, p, l = wb.getSensorValues()
        display.text(f"Tempr: {t}*C", x=0, y=0)
        display.text(f"Humdt: {h} %", x=0, y=10)
        display.text(f"Atm.p: {p} kPa", x=0, y=20)
        display.text(f"Light: {l} %", x=0, y=30)
        display.show()

        # Send data using a POST request
        request = urequests.post(
        'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_API_KEY,
        json={"field1":{vali2c[0]}.{vali2c[1]}, "field2": humidity,"field3": pressure},
        headers={"Content-Type": "application/json"})
        print(f"Request #{request.text} sent")
        request.close()
        
        time.sleep(5)


except KeyboardInterrupt:
    wb.disconnect_wifi()
    print("Ctrl+C Pressed. Exiting...")
