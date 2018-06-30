import numpy as np
from cluster import Kmeans
import mss


class Grabber(object):

    def __init__(self, monitor):
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor]
        self.k_means = Kmeans(k=1)

    def grab(self):
        return self.sct.grab(self.monitor)

    def get_dominant_colour(self, img):
        return self.k_means.run(img)[0]
