# Led Code

import time
import random
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# First val = SCK
# Second val = SDI
dots = dotstar.DotStar(board.A5, board.A4, 48, brightness=0.1) # Can experiment with baud rate later, after 1MHz MOSFETs will perform poorly
# third value denotes number of dotstars
# please set brightness low to not burn board

# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32


# MAIN LOOP
n_dots = len(dots)
while True:
    # Fill each dot with a random color
    for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())

    # make all leds green to test
    # dots.fill((0, 255, 0))
    print(dots)
    time.sleep(0.25)
