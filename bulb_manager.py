import time

from yeelight import Bulb, BulbException


class BulbManager(object):

    def __init__(self, bulb_ips, effect="smooth", duration=300):
        """
        bulb_ips - List of IP addresses
        effect - How the colour change transitions (smooth/sudden)
        duration - How long a `smooth` transition takes (ignored if `sudden`)
        """
        self.bulbs = [Bulb(bulb_ip, effect=effect,
                           duration=duration, auto_on=True)
                      for bulb_ip in bulb_ips]

    def update_colour(self, r,g,b):
        """
        Updates all of the bulbs with the given RGB values
        r - red value
        g - green value
        b - blue value
        """
        for bulb in self.bulbs:
            try:
                bulb.set_rgb(r,g,b)
            except BulbException:
                pass
        time.sleep(0.1)
