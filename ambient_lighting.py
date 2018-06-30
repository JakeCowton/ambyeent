import time

# from fire import Fire
from grabber import Grabber
from PIL import Image
from yeelight import Bulb, BulbException


def main(monitor, bulb_ip):
    bulb = Bulb(bulb_ip)
    bulb.turn_on()

    grabber = Grabber(monitor)
    while True:
        sct_img = grabber.grab()
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        r,g,b = [round(x) for x in grabber.get_dominant_colour(img)]
        try:
            bulb.set_rgb(r,g,b)
        except BulbException:
            print("sleeping")
            time.sleep(1)

if __name__ == "__main__":
    main(1, "192.168.0.10")