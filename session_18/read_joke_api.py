# pip install requests
import requests as rq
url = "https://api.chucknorris.io/jokes/random"
result = rq.get(url)
print(type(result))
print(result)
data = result.json()
print()
print(type(data))
# print(data)
for key , value in data.items():
    print(key , value)