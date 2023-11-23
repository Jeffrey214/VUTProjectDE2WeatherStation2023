# Digital Electronics 2 F/Z 2023 Semester Project

Multi-Sensor Weather Station Concept
For Brno Institute of Technology (BUT) / Vysoké Učení Technické v Brně (VUT)

<br>

## Team Members:
Owen Braux            | Program Code (Humidity Sensor, Pressure Sensor and OLED Display out)

Jeffrey Dotson        | Device Design and Construction, Readme and Theoretical Assignment

Bogdan Kolendovskyy   | Program Code (General Code, Light Sensor, Polish and Final Debugging of Code)

Wang Oliver           | API Code, Initial Debugging of code

<br>


## Theoretical Description and Explanation:
The assignment as presented is to create a device using a microcontroller and sensor elements that accurately reads the temperature, pressure, light level, and humidity of a given area when the device is run. The device needs to output to a OLED interface panel that is directly connected to the device as well as communicate with an external API for storage of logged data as well as for access to weather and temperature data for forecast. [2]

The primary actions that are required to fulfill the design requirements include:
* To find the required components required to create the device
* Connect the device to the ESP 32 microcontroller as required
* Develop code to run and process data from the sensors, as well as display processed data on an output display
* Develop code to communicate with an external API, it must be capable of receiving as well as sending information
<br>

## Hardware Description of Demo Application
Our device consists of multiple sensors as well as other electrical components that work together.  
<br>

### `ESP 32 Microcontroller`  
* A microcontroller device that is used as a central power and ground source for the electrical components of that are used in the device, including the sensors.  
* It is also used as the processing unit, using analog and digital inputs as well as bus lines we are able to control the sensors as well as read and interpret data that we receive into output data.

![DE2_proj_ESP32](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/c71e93b5-def8-402e-8c24-6815fdd919fb) [3]

<br>

### `Breadboard`
* Used to connect all sensors together using with the help of wires as well.
* Main base of our device

![DE2_proj_Breadboard_rs](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/ec21c630-5968-4fe6-892d-dfb6d86b2570) [4]

<br>

### `1.3 Inch I2C OLED Display Module`
* Primary output module of our device
* Data is printed to the display using SDA and SDL bus lines for communication
* Used icons/pictographs to better present outputted information

![DE2_proj_OLED_rs](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/9f660f3f-1630-4a84-912d-6730e0cb5e4b) [5]

<br>

### `LDR (Light Dependent Resistor) Photoresistor`
* Using the photoresistor we are able approximate light levels
* Photoresistors work on the principle that the more light that they are exposed to the more current they let through. The code is able to interpret the current passthrough and extrapolate the light level from it
* One pin of the photoresistor is tied into the 3v3 and the A0 (Analog 0) pin. This powers and reads the data off the photoresistor. The other pin of the photoresistor is tied into a resistor and the ground.

![DE2_proj_PhotoResistor_rs](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/234253a4-c553-4b82-b93a-df9a2321a036) [6]

<br>

### `DPM280 Preassure (Barometric) Sensor`
* Used to measure the atmospheric preassure of the environment, also has a temperature sensor (this is not used in our device, as temperature data is taken from the humidity sensor)
* Has an SDA and SCL input, as well as a VCC (3V3) input and a ground pin. [1]
* Data is processed and outputted onto the OLED screen

![DE2_proj_PresSens_rs](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/5145a1b5-774d-4bcf-a9d2-38ee1e3cb15a) [7]

<br>

### `DH11 Humidity Sensor`
* Used to measure the humidity of an environment, also has a temperature sensor that is used the measure the temperature of an environment
* Has a SDA and SCL input, as well as a VCC (3V3) input and a ground pin.
* Data is processed and outputted onto the OLED screen

![DE2_proj_Hum_rs](https://github.com/Jeffrey214/VUTProjectDE2WeatherStation2023/assets/50847055/e3e47798-47bb-40cd-b0e8-23508d2002e6) [8]

<br>

## Software Description
Put flowchats of your algorithm(s) and direct links to source files.

## Instructions
Write an instruction manual for your application, including photos and a link to a short app video.

## References:

### `Code/Assignment Works Cited`
[1] “Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout,” Adafruit Learning System. Accessed: Nov. 23, 2023. [Online]. Available: https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/circuitpython-test  

[2] T. Fryza, “MicroPython on ESP32/ESP8266 microcontollers.” Nov. 03, 2023. Accessed: Nov. 23, 2023. [Online]. Available: https://github.com/tomas-fryza/esp-micropython

<brk>

### `Image Credits`

[3] “86.52CZK 25% OFF|BME280 3.3V 5V Digital Sensor Temperature Humidity Barometric Pressure Sensor Module I2C SPI 1.8 5V BME280 Sensor Module| | - AliExpress,” aliexpress.com. Accessed: Nov. 23, 2023. [Online]. Available: //www.aliexpress.com/item/1005005898848756.html?src=ibdm_d03p0558e02r02&sk=&aff_platform=&aff_trace_key=&af=&cv=&cn=&dp=  

[4] “400 Points Solderless Self Adhesive BreadBoard,” indiamart.com. Accessed: Nov. 23, 2023. [Online]. Available: https://m.indiamart.com/proddetail/400-points-solderless-self-adhesive-breadboard-19871496173.html  

[5] “Addicore Photoresistor 5mm Photo Cell,” Addicore. Accessed: Nov. 23, 2023. [Online]. Available: https://www.addicore.com/products/photoresistor-5mm  

[6] “Amazon.com: Stemedu ESP32-S2-Saola-1 Microcontroller Processor Module 4MB Flash + 2MB PSRAM ESP32-S2-WROVER WiFi Development Board for Ardunio IDE : Electronics.” Accessed: Nov. 23, 2023. [Online]. Available: https://www.amazon.com/Stemedu-ESP32-S2-Development-Board-ESP32-S2-Saola-1/dp/B09TVY63FF  

[7] “DHT11 Arduino Modul pro Měření Teploty a Vlhkosti,” robotstore.cz. Accessed: Nov. 23, 2023. [Online]. Available: https://robotstore.cz/produkt/dht11-arduino-modul-pro-mereni-teploty-a-vlhkosti/  

[8] C. spol s r.o, “IIC I2C OLED 1,3" displej 128x64 Bílý | dratek.cz,” dratek.cz. Accessed: Nov. 23, 2023. [Online]. Available: https://dratek.cz/arduino/3181-iic-i2c-oled-1-3-displej-128x64-bily.html

