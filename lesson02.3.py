import requests
#import pprint

url = "https://jsonplaceholder.typicode.com/posts"

data = {'title': 'foo',
         'body': 'bar',
         'userId': 1
        }

response = requests.post(url, data=data)

print(f"Status code: {response.status_code}")
print(f"Response text: {response.json()}")



