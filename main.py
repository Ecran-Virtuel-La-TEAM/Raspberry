from serial import Serial

BAUDS = 921600  # Same value as in the Arduino : Serial.begin()

buffer = bytearray()
BUFFER_SIZE = 1000
file_size_kb = 0
MAX_FILE_SIZE_KB = 5 * 1024 # 5 MB

with Serial("/dev/serial0", BAUDS, timeout=1) as serial, open("A0_data.bin", "wb") as file:
    while True:
        a0, a1, a2, a3 = serial.read(4)

        buffer.append(a0)
        if len(buffer) >= BUFFER_SIZE:
            file.write(buffer)
            buffer.clear()
            file_size_kb += 1

        if file_size_kb > MAX_FILE_SIZE_KB:
            break

# from zero_hid import Mouse
# from time import sleep

# m = Mouse()

# SCREEN_WIDTH = 2**15
# SCREEN_HEIGHT = 2**15

# with Mouse(absolute = True) as mouse:
#     while True:
#         for pos in (
#             (  0,   0),
#             (100,   0),
#             (100, 100),
#             (  0, 100),
#         ):
#             mouse.move(*pos)
#             sleep(0.5)
