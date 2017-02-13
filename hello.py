from gopigo import *
import time

def shimmy():
    for x in range(2):
        right()
        time.sleep(.5)
        left()
        time.sleep(.5)

shimmy()
stop()
