from getWeather import getWeather
from getForecast import getForecast
import schedule
import time
from datetime import datetime

# tweets the daily forecast at 7am cst as well as the weather every 4 hours throughout the day
schedule.every().day.at('07:00').do(
    getForecast, schedule.every(4).hours.do(getWeather))

while 1:
    schedule.run_pending()
    time.sleep(1)

