from client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "0.0.0.0"
PORT = 20500

c = Client(IP, PORT)
print(c)