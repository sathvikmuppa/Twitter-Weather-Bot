import requests
import json
import math
import tweepy
from keys import keys
from bs4 import BeautifulSoup
from datetime import datetime


class Forecast:
    # access tokens
    access_token = keys["access_token"]
    access_token_secret = keys["access_token_secret"]
    consumer_key = keys["consumer_key"]
    consumer_key_secret = keys["consumer_key_secret"]

    # autorizes tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)  # initializes the tweepy api

    # the url that beautiful soup accesses and browser specifications
    URL = 'https://weather.com/weather/hourbyhour/l/d59023ba8b860e35a273fd420925961b98fe02814fbf6e68c001099248f87ba5'
    headers = {
        'Users-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page = requests.get(URL, headers=headers)

    def get(self):
        # initializes beautiful soup
        soup = BeautifulSoup(Forecast.page.content, 'lxml')

        soup_hours_elements = list(soup.findAll(
            'h2', attrs={'data-testid': 'daypartName'}))  # finds all elements with the time
        soup_temperatures_elements = list(soup.findAll(
            'span', attrs={'data-testid': 'TemperatureValue'}))  # finds all elements with the temperature

        # empty lists which the html elements will be added to
        soup_hours = []
        soup_temperatures = []

        for time in soup_hours_elements:
            x = time.get_text()  # gets the time text from each element and adds it to the empty array
            soup_hours.append(x)

        for temp in soup_temperatures_elements:
            # gets the temperature text from each element and adds it to the empty array
            x = temp.get_text()
            soup_temperatures.append(x)

        selected_temperatures = []
        for index, temp in enumerate(soup_temperatures):
            if index % 2 == 0:
                # adds every other value to the new list
                selected_temperatures.append(temp)

        # shortens the array to only include elements from the current day
        selected_temperatures = selected_temperatures[:soup_hours.index(
            '1 am')]
        soup_hours = soup_hours[:soup_hours.index('1 am')]

        # output lists
        self.temperatures = []
        self.hours = []

        for soup_hours_elements in soup_hours:
            if soup_hours_elements == '6 am' or soup_hours_elements == '12 pm' or soup_hours_elements == '6 pm' or soup_hours_elements == '12 am':
                self.hours.append(soup_hours_elements)
                self.temperatures.append(
                    selected_temperatures[soup_hours.index(soup_hours_elements)])

        self.output = "Today's Forecast:\n"

        # puts the tweet together
        for hour in self.hours:
            if self.hours.index(hour) == len(self.hours)-1:
                self.output = self.output + hour + ' ' + \
                    self.temperatures[self.hours.index(hour)]
            else:
                self.output = self.output + hour + ' ' + \
                    self.temperatures[self.hours.index(hour)] + '\n'

    def tweet(self):
        Forecast.api.update_status(self.output)

        # logs the tweet
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        print('Tweeted Forecast | ' + current_time)
