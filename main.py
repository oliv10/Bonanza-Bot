import time
from aircraft import Aircraft
from geocode import Geocoode

with open("config/config.txt") as file:
    config_data = file.readlines()

config = []

for i in config_data:
    config.append(i.strip())

a = Aircraft("a769d9")
a.start()

g = Geocoode(config[1])

time.sleep(3)


while True:
    curr = a.currentAirData
    if curr.getLanded():
        print("on ground")
        loc = g.getReverse(curr.getLongitude(), curr.getLatitude())
        print("Landed Near " + loc.display_name)
        print("LANDED!")
        exit()
    elif curr.getLastContact() == None:
        print("data signal lost")
        prev = a.previousAirData
        loc = g.getReverse(prev.getLongitude(), prev.getLatitude())
        print("Landed Near " + loc.display_name)
        print("LANDED!")
        exit()
    else:
        print("FLYING @ " + str(curr.getVelocity()) + " Knots " + str(curr.getVerticalRate()) + " Ft/Min")
