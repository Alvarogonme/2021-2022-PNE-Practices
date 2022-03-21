from seq1 import Seq

PRACTICE = 1
EXERCISE = 10

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

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

s = Seq()
filename = valid_filename()
s.seq_read_fasta(filename)

d = s.total_count_base()
base = s.genes(d)
print(f"Gene {filename}: \nMost frequent value base: {base}")