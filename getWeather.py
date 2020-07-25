import requests, json, math
import tweepy
from keys import keys

access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
consumer_key = keys["consumer_key"]
consumer_key_secret = keys["consumer_key_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  # initializes the tweepy api

def getWeather():
    api_key =  keys["openweathermap_api"] # open weather map api key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = 'Sugar Land'
    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name
    response = requests.get(complete_url)
    x = response.json()  # reads the json from the api and stores it inside of 'x' as a dict

    if x['cod'] != '404':  # reads the city name
        y = x["main"]
        # converts temperature from kelvin to fahrenheit
        current_temperature = math.ceil((y['temp'] - 273.15) * 9/5 + 32)
        current_humidity = y['humidity']
        z = x['weather']
        weather_description = z[0]['description']
        api.update_status(f'''Temperature (Fahrenheit): {current_temperature}
Humidity: {current_humidity}%
{weather_description}''')
    else:
        print('City not found')


getWeather()
