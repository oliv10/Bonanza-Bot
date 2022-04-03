from opensky.opensky_api import OpenSkyApi
import time
import geocode

# Strip all strings in this list
config = open("config/config.txt", "r").readlines()

api = OpenSkyApi(config[1].strip(), config[2].strip())

# keys = api.get_states().states[0].keys

# print(keys)

print(config[4])

while True:
    curr_state = api.get_states(icao24=config[4].strip()) # Change the 4 back to zero for final product
    
    # print(curr_state)
    
    print(curr_state.states[0])
    
    dic = curr_state.states[0].__dict__
    
    # print(type(dic))
    
    lon = dic.get("longitude")
    lat = dic.get("latitude")
    
    # print(lon, lat)
    
    locat = geocode.reverse(str(lon), str(lat))
    
    print(locat)
    
    for i in locat:
        print(i)
    
    break
    
    time.sleep(10)