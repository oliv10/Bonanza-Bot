from aircraft import Aircraft
import time
import geocode

a = Aircraft("abeb31")
a.start()

prev = None
curr = None

while True:
    curr = a.currentAirData
    if curr != prev:
        print(curr)
        prev = curr
        if curr.getLanded():
            loc = geocode.reverse(curr.getLongitude(), curr.getLatitude())
            print("Landed Near " + loc.get("display_name"))
            print("LANDED!")
        else:
            print("FLYING @ " + str(curr.getVelocity()) + " Knots @ " + str(curr.getVerticalRate()) + " Ft/Min")