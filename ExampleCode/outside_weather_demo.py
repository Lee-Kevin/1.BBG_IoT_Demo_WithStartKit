#This is a demo to get your city/town weather from http://openweathermap.org/ to display on Grove OLED
#by Carmelito Andrade
#sudo pip install pyowm
#Create an account on http://openweathermap.org/ and get the API key
import time
import grove_oled
import pyowm
APIKey = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
placeName = 'Toronto,CA' #change this to your city name

owm = pyowm.OWM(APIKey)

grove_oled.oled_init()
grove_oled.oled_setNormalDisplay()
grove_oled.oled_clearDisplay()

while True:
	observation = owm.weather_at_place(placeName)	
	weatherData = observation.get_weather()
	temperature = weatherData.get_temperature(unit='celsius')['temp']
	humidity = weatherData.get_humidity()
	weatherCondition = weatherData.get_status()
	#printing weather on the OLED
	grove_oled.oled_setTextXY(0,0)
	grove_oled.oled_putString(placeName)
	grove_oled.oled_setTextXY(2,0)
	grove_oled.oled_putString('Temp :'+ str(temperature) +'C')
	grove_oled.oled_setTextXY(4,0)
	grove_oled.oled_putString('Humid:'+ str(humidity) +'%')
	grove_oled.oled_setTextXY(6,0)
	grove_oled.oled_putString("- Weather -")
	grove_oled.oled_setTextXY(8,0)
	grove_oled.oled_putString(weatherCondition)
	time.sleep(1800) #check weather after every 30 mins
