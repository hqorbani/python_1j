# https://schedule.readthedocs.io/en/stable/
import schedule
import time

def say_hello():
    print("Hello!")

schedule.every(3).seconds.do(say_hello)    

while True:
    schedule.run_pending()
    time.sleep(1)