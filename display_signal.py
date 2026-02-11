import matplotlib.pyplot as plt

FILE = "/mnt/c/Users/liver/Downloads/A0_data.bin"

with open(FILE, "rb") as f:
    data = f.read()

samples = tuple(data)

plt.figure()
plt.plot(samples)
plt.xlabel("Sample Number")
plt.ylabel("A0 Value (8-bit)")
plt.title(f"Signal from {FILE}")
plt.grid(True)
plt.show()
