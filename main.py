import time
<<<<<<< Updated upstream
import geocode

a = Aircraft("abeb31")
=======
from aircraft import Aircraft
from geocode import Geocoode

with open("config/config.txt") as file:
    config = file.readlines()

a = Aircraft("a0cffe")
>>>>>>> Stashed changes
a.start()

g = Geocoode(config[1])

time.sleep(3)


while True:
    curr = a.currentAirData
<<<<<<< Updated upstream
    if curr != prev:
        print(curr)
        prev = curr
        if curr.getLanded():
            loc = geocode.reverse(curr.getLongitude(), curr.getLatitude())
            print("Landed Near " + loc.get("display_name"))
            print("LANDED!")
        else:
            print("FLYING @ " + str(curr.getVelocity()) + " Knots @ " + str(curr.getVerticalRate()) + " Ft/Min")
=======
    if curr.getLanded():
        print("landed")
        loc = g.getReverse(curr.getLongitude(), curr.getLatitude())
        print("Landed Near " + loc.get("display_name"))
        print("LANDED!")
        exit()
    elif curr.last_contact == None:
        print("data lost")
        prev = a.previousAirData
        loc = g.getReverse(prev.getLongitude(), prev.getLatitude())
        print("Landed Near " + loc.get("display_name"))
        print("LANDED!")
        exit()
    else:
        print("FLYING @ " + str(curr.getVelocity()) + " Knots " + str(curr.getVerticalRate()) + " Ft/Min")
>>>>>>> Stashed changes
