import time

import fire
from screen import Screen
from bulb_manager import BulbManager

def run(monitor, *args):
    """
    Begins the tracking

    monitor - integer representing the monitor ID
    args - a list of IP addresses of bulbs to control
    """
    monitor = int(monitor)
    bulb_ips = [str(bulb_ip) for bulb_ip in args]

    bm = BulbManager(bulb_ips)
    screen = Screen(monitor)

    while True:
        r,g,b = screen.get_dominant_colour()
        bm.update_colour(r,g,b)

if __name__ == "__main__":
    fire.Fire()
