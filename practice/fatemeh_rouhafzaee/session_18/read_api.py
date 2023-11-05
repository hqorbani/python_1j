import schedule
import time
from def_joke import get_joke
url= "https://api.chucknorris.io/jokes/random"

print("hi...")
print(f"This program shows you a joke of {url} link every 5 seconds")
print()
specific_link = str(input("Do you want to get the jock from a specific link? (yes/no)")).lower()
if specific_link == "yes" :  
   url = input(" enter that link in full :").lower()


schedule.every(5).seconds.do(get_joke , url)    

while True:
    schedule.run_pending()
    time.sleep(1)