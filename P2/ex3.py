from client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "0.0.0.0"
PORT = 20500

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: \n {response}")