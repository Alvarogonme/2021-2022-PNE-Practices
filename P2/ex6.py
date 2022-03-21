from client0 import Client
from seq import Seq
import colorama

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

seq = "FRAT1.txt"
s = Seq()
s.seq_read_fasta(seq)
fg_0 = str(s)[:10]
fg_1 = str(s)[11:20]
fg_2 = str(s)[21:30]
fg_3 = str(s)[31:40]
fg_4 = str(s)[41:50]
fg_5 = str(s)[51:60]
fg_6 = str(s)[61:70]
fg_7 = str(s)[71:80]
fg_8 = str(s)[81:90]
fg_9 = str(s)[91:100]

list_fragments = [fg_0, fg_1, fg_2, fg_3, fg_4, fg_5, fg_6, fg_7, fg_8, fg_9]

i = 1
times = 0
for b in list_fragments:
    if i == 1 or i == 3 or i==5 or i==7 or i== 9:
        IP = "127.0.0.1"
        PORT = 20500
        c = Client(IP, PORT)
        if times < 1:
            print(f"Gene FRAT1 {colorama.Fore.BLUE + str(s)}" + colorama.Fore.RESET)
            response = c.talk(f"Sending {seq} Gene to server, in fragments of 10 bases..." + colorama.Fore.RESET)
            times += 1
        print(f"Fragment", str(i) + f":{colorama.Fore.BLUE + b}" + colorama.Fore.RESET)
        response = c.talk("Fragment " + str(i) + f": {b}" + colorama.Fore.RESET)
        i = i + 1
    elif i != 1 or i != 3 or i != 5 or i != 7 or i != 9:
        IP = "127.0.0.1"
        PORT = 20501
        c = Client(IP, PORT)
        print(f"Fragment", str(i) + f":{colorama.Fore.BLUE + b}" + colorama.Fore.RESET)
        response = c.talk("Fragment " + str(i) + f": {b}" + colorama.Fore.RESET)
        i = i + 1