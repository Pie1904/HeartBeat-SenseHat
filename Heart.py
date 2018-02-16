from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255,0,0]
w = [255,255,255]
e = [0,0,0]

image = [
    e,e,e,e,e,e,e,e,
    e,r,r,e,e,r,r,e,
    r,r,w,w,r,r,r,r,
    r,w,r,r,r,r,r,r,
    e,r,r,r,r,r,r,e,
    e,e,r,r,r,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

image2 = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,r,e,e,r,e,e,
    e,r,r,w,r,r,r,e,
    e,e,r,r,r,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

while True:
    sense.set_pixels(image)
    time.sleep(0.45)
    sense.set_pixels(image2)
    time.sleep(0.40)
    
