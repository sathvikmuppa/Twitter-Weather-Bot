import requests
import json
import math
import tweepy
from keys import keys
from bs4 import BeautifulSoup
from datetime import datetime


class Weather:
    # reads twitter tokens from a separate file
    access_token = keys["access_token"]
    access_token_secret = keys["access_token_secret"]
    consumer_key = keys["consumer_key"]
    consumer_key_secret = keys["consumer_key_secret"]

    # autorizes tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # initializes the tweepy api

    def get(self):
        api_key = keys["openweathermap_api"]  # open weather map api key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = 'Sugar Land'
        complete_url = base_url + 'appid=' + api_key + '&q=' + city_name + \
            '&units=imperial'  # temperature unit is originally kelvin
        response = requests.get(complete_url)
        x = response.json()

        if x['cod'] != '404':  # reads the city name
            y = x["main"]
            # stores the needed information
            current_temperature = math.ceil(y['temp'])
            current_humidity = y['humidity']
            z = x['weather']
            weather_description = z[0]['description'].capitalize()

            #stores output
            output = f'''Temperature (Fahrenheit): {current_temperature}
Humidity: {current_humidity}%
{weather_description}'''
        else:
            print('City not found')

        return output

    def tweet(self):
        self.api.update_status(self.get())

        # logs the tweet
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        print('Tweeted Weather | ' + current_time)
