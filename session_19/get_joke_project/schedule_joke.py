import schedule
import time
from task import get_joke
url = "https://api.chucknorris.io/jokes/random"

print("hello , please waite for joke...")

schedule.every(7).seconds.do(get_joke , url)    

while True:
    schedule.run_pending()
    time.sleep(1)