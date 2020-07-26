# Twitter-Weather-Bot
A bot that tweets the temperature, humidity, and weather. Runs at 7:00AM everyday using windows task scheduler.

This bot uses tweepy as well as openweathermap.org in order to tweet the weather of my city whenever run, currently I am running it everyday using windows task scheduler though i plan to add a timer and run it at all times on a raspberry pi.

The access tokens and consumer keys were generated at developer.twitter.com and are in a dictionary in a seperate file.

The bot tweets on the account @SLANDWeather on twitter.
