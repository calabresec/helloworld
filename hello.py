from gopigo import *
import time

def shimmy():
    for x in range(2):
        right()
        time.sleep(.5)
        left()
        time.sleep(.5)

    def twirl():
        right_rot()
        time.sleep(2)

while True:

shimmy()
twirl()
stop()
