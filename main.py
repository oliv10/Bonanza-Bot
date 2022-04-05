from aircraft import Aircraft
import time

a = Aircraft("a20d77")
a.start()

prev = None
curr = None

while True:
    curr = a.currentAirData
    if curr != prev:
        print(curr)
        prev = curr
        if curr.getLanded():
            print("LANDED!")
        else:
            print("FLYING @ " + str(curr.getVelocity()) + " Knots")