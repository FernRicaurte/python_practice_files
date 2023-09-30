import requests
city = input("Which city do you live in?\n")
url = "http://api.weatherapi.com/v1/current.json?key=581dcf430a314905b6a00907232209&q="+city+"&aqi=no"
response = requests.get(url)
weather_json = response.json()
temp = weather_json.get("current").get("temp_f")
description = weather_json.get("current").get("condition").get("text")
print("Today's weather in", city, "is", description, "and", temp, "degrees")