from client0 import Client
from seq import Seq
import colorama

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 20500
c = Client(IP, PORT)
print(c)

seq = "U5.txt"
seq_1 = "ADA.txt"
seq_2 = "FRAT1.txt"

list_sequences = [seq, seq_1, seq_2]
for b in list_sequences:
    s = Seq()
    s.seq_read_fasta(b)
    print(f"To server: {colorama.Fore.BLUE + b} gene to the server..." + colorama.Fore.RESET)
    response = c.talk(f"Sending {b} gene to server" + colorama.Fore.RESET)
    print(f"From server: \n{colorama.Fore.YELLOW + response + colorama.Fore.RESET}")

    print(f"To server {colorama.Fore.BLUE + str(s)} gene to the server..." + colorama.Fore.RESET)
    response = c.talk(s.strbases)
    print(f"From server: \n{colorama.Fore.YELLOW + response + colorama.Fore.RESET}")
