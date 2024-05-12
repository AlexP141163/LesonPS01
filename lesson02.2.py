import requests
import pprint

param = {'userId' : 1}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, params=param)

posts = response.json()
for post in posts:
    print(post)


# pprint.pprint(response.json())
# print(response.status_code)
# print(response.text)
