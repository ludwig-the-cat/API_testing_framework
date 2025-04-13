import json

import requests

url = "https://dog.ceo/api/breed/hound/images"

r = requests.get(url).json()
s = 0
for i in r.get('message'):
    if 'hound-english' in i:
        s += 1
print(s)