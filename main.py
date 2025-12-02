from zero_hid import Mouse
from time import sleep


m = Mouse()

SCREEN_WIDTH = 2**15
SCREEN_HEIGHT = 2**15

with Mouse(absolute = True) as mouse:
    while True:
        for pos in (
            (  0,   0),
            (100,   0),
            (100, 100),
            (  0, 100),
        ):
            mouse.move(*pos)
            sleep(0.5)
