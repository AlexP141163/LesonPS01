import requests
import pprint

param = {'q' : 'html'}

url = "https://api.github.com/search/repositories"

response = requests.get(url, params=param)

print(f"Status code: {response.status_code}")
pprint.pprint(response.json)
print(f"Status text: {response.text}")
