# import requests
# import json

# url = "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=37.42159&longitude=-122.0837&localityLanguage=en"

# resp = requests.get(url)

# code = resp.encoding

# raw = resp.content.decode(code)

# data = json.loads(raw)

# print(data)

# import geocode

# resp = geocode.reverse("40.0035044", "-85.96460575167049")

# print(resp)

# for i in resp:
#     print(i)


import requests
import json

"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.712784,-74.005941&rankby=distance&type=airport&key=<Your API Key>"

# Try the google places API to find nearest airport once plane has landed or is no longer detected


from geocode import Geocoode

with open("config/config.txt") as file:
    data = file.readlines()
    
config = []

for i in data:
    config.append(i.strip())

g = Geocoode(config[1]).getReverse(-87.6478464, 41.926656)

print(g.display_name)

# data = g.getReverse(-87.6478464, 41.926656)

# print(data.keys())
# print(data)

# with open("keys3.txt", "w") as file:
    
#     for i in data.keys():
#         print(i)
#         file.write(i + ' = location.get("' + i + '"), ')

# locData = g.getLocationData(data)

# add = locData.getAddress()

# print(locData.display_name)

# print(add)
        
# print(g.getLocationData(data))