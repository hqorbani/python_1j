# pip install requests
import requests as rq
url = "https://api.coinlore.net/api/global/"
result = rq.get(url)
# print(type(result))
# print(result)
data = result.json()
new_data = data[0]
print()
print(type(new_data))
# print(data)
for key , value in new_data.items():
    if key == "btc_d":
        print(key , value)