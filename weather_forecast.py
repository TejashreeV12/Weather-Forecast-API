
import requests

url="https://api.openweathermap.org/data/2.5/weather?"
api_key=6c39e031731482654b04f2f44db4217c
city=input("Enter the city name:")

#to convert from kelvin to celsius and fahrenheit
def kelvin_to_celsius_fahrenheit(kelvin):
  celsius=kelvin-273.15
  fahrenheit=celsius*(9/5)+32
  return celsius,fahrenheit


final_url=url+"appid="+api_key+"&q="+city
response=requests.get(url).json()

kelvin_temp=response['main']['temp']
celsius_temp, fahrenheit_temp=kelvin_to_celsius_fahrenheit(kelvin_temp)
humidity=response['main']['humidity']
wind_speed=response['wind']['speed']
description=response['weather'][0]['description']

print(f"Temperature in {city}:{celsius_temp:.2f}°C or {fahrenheit_temp:.2f}°F")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {wind_speed}m/s")
