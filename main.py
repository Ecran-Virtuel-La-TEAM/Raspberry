from serial import Serial

# Settings
RECORDING_TIME = 10 # s
FILE = "/home/groupe11/Documents/Raspberry/data/A0_data.bin"

BAUDS = 921600  # Same value as in the Arduino : Serial.begin()
BUFFER_SIZE = 1000

# Constants
buffer = bytearray()
file_size_kb = 0

SAMPLING_FREQUENCY = 8000
MAX_FILE_SIZE_KB = round(RECORDING_TIME * SAMPLING_FREQUENCY / BUFFER_SIZE) 

print(f"file {FILE} will take {MAX_FILE_SIZE_KB} kB, do you want to continue ?", end=" ")
if input() not in ("y", "yes", ""):
    exit("Bye")

with Serial("/dev/ttyACM0", BAUDS, timeout=5) as serial, open(FILE, "wb") as file:
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
