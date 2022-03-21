from seq1 import Seq

def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter a filename: ")
        try:
            f = open(filename + ".txt", "r")
            exit = True
            return filename + ".txt"
        except FileNotFoundError:
            print("File was not found. Try again.")

PRACTICE = 1
EXERCISE = 9

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s_2 = Seq()
filename = valid_filename()
s_2.seq_read_fasta(filename)

print(f"Sequence:  (Length: {s_2.len_sequence()})  {s_2}")
print("Bases:")
d = s_2.total_count_base()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nRev:", s_2.seq_reverse())
print("Comp:", s_2.seq_complement())