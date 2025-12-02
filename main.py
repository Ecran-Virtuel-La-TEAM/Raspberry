from zero_hid import Mouse


m = Mouse()

while True:
    for pos in (
        ( 100,  100),
        ( 100, -100),
        (-100, -100),
        (-100,  100),
    ):
        m.move(*pos)
