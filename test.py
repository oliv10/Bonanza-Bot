# import requests
# import json

# url = "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=37.42159&longitude=-122.0837&localityLanguage=en"

# resp = requests.get(url)

# code = resp.encoding

# raw = resp.content.decode(code)

# data = json.loads(raw)

# print(data)

import geocode

resp = geocode.reverse("40.0035044", "-85.96460575167049")

print(resp)

for i in resp:
    print(i)