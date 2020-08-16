from Weather import Weather
from Forecast import Forecast
import schedule
import time

try:
    print('PROGRAM STARTED')
    f = Forecast()
    w = Weather()

    # tweets the daily forecast at 7am cst as well as the weather every 4 hours throughout the day
    schedule.every().day.at('05:00').do(f.get)
    schedule.every().day.at('07:00').do(f.tweet)
    schedule.every().day.at('08:00').do(w.tweet)
    schedule.every().day.at('14:00').do(w.tweet)
    schedule.every().day.at('18:00').do(w.tweet)
    schedule.every().day.at('22:00').do(w.tweet)

    while 1:
        schedule.run_pending()
        time.sleep(1)
except:
    print('PROGRAM STOPPED')