import numpy as np
from cluster import Kmeans
import mss
from PIL import Image


class Screen(object):
    """Handles grabbing images of a specific monitor"""

    def __init__(self, monitor):
        """
        monitor - the integer representing the monitor ID
        """
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor]
        self.k_means = Kmeans(k=1)

    def grab(self):
        """Returns a screenshot of the tracked monitor"""
        return self.sct.grab(self.monitor)

    def get_dominant_colour(self):
        """Returns the dominant colour of an image"""
        sct_img = self.grab()
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        colours = self.k_means.run(img)[0]
        r,g,b = [round(x) for x in colours]

        return r,g,b