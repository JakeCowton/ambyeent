import time

import fire
from screen import Screen
from yeelight import Bulb, BulbException

def run(monitor, bulb_ip):
    """
    Begins the tracking

    monitor - integer representing the monitor ID
    bulb_ip - ip address of the bulb to change
    """
    monitor = int(monitor)
    bulb_ip = str(bulb_ip)

    bulb = Bulb(bulb_ip)
    bulb.turn_on()

    screen = Screen(monitor)
    while True:
        r,g,b = screen.get_dominant_colour()

        try:
            bulb.set_rgb(r,g,b)
        except BulbException:
            pass

        time.sleep(0.1)

if __name__ == "__main__":
    fire.Fire()
