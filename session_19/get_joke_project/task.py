import requests as rq


def get_joke(url):
    result = rq.get(url)
    data = result.json()
    print(data['value'])





def say_hello():
    print("Hello!")