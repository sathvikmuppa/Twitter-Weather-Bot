import requests
import json
import math
import tweepy
from keys import keys
from bs4 import BeautifulSoup

#reads twitter tokens from a separate file
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]
consumer_key = keys["consumer_key"]
consumer_key_secret = keys["consumer_key_secret"]

#autorizes tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  # initializes the tweepy api


def getForecast():
    URL = 'https://weather.com/weather/hourbyhour/l/d59023ba8b860e35a273fd420925961b98fe02814fbf6e68c001099248f87ba5' #the url that beautiful soup accesses
    headers = {
        'Users-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml') #initializes beautiful soup
    hour = soup.findAll('h2', attrs={'data-testid': 'daypartName'}) #finds all elements with the time
    temperature = soup.findAll(
        'span', attrs={'data-testid': 'TemperatureValue'}) #finds all elements with the temperature
    hours = [] #empty list which the selected values will be added to
    temperatures = [] #empty list which the selected values will be added to
    for time in hour:
        x = time.get_text() #gets the time text from each element and adds it to the empty array
        hours.append(x)

    for temp in temperature:
        x = temp.get_text()
        temperatures.append(x) #gets the temperature text from each element and adds it to the empty array

    hours = hours[:16] #removes all the times from other days
    hours2 = []
    temperatures = temperatures[:32] #removes all the temperatures from other days
    
    temperatures2 = []

    for index, temp in enumerate(temperatures):
        if index % 8 == 0:
            temperatures2.append(temp)

    for index, time in enumerate(hours):
        if index % 4 == 0:
            hours2.append(time)

    api.update_status(f'''Today's forecast:
Morning: {temperatures2[0]}
Noon: {temperatures2[1]}
Afternoon: {temperatures2[2]}
Evening: {temperatures2[3]}
    ''')
