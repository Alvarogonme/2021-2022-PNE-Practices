from client0 import Client
from seq import Seq
import colorama

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 20500
c = Client(IP, PORT)
print(c)

seq = "FRAT1.txt"
s = Seq()
s.seq_read_fasta(seq)
fg_0 = str(s)[:10]
fg_1 = str(s)[11:20]
fg_2 = str(s)[21:30]
fg_3 = str(s)[31:40]
fg_4 = str(s)[41:50]

list_fragments = [fg_0, fg_1, fg_2, fg_3, fg_4]

print(f"Gene FRAT1: {colorama.Fore.BLUE + str(s) }" + colorama.Fore.RESET)
response = c.talk(f"Sending {seq} Gene to server, in fragments of 10 bases..." + colorama.Fore.RESET)

i = 1
for b in list_fragments:
    print(f"Fragment", str(i) + f":{colorama.Fore.BLUE + b}" + colorama.Fore.RESET)
    response = c.talk("Fragment" + str(i) + f": {b}" + colorama.Fore.RESET)
    i = i + 1