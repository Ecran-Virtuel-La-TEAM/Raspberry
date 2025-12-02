from zero_hid import Mouse
from time import sleep


m = Mouse()

while True:
    for pos in (
        ( 100,  100),
        ( 100, -100),
        (-100, -100),
        (-100,  100),
    ):
        m.move(*pos)
        sleep(0.5)
