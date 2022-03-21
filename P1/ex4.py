from seq1 import Seq

PRACTICE = 1
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Seq()
s_1 = Seq("ACTGA")
s_2 = Seq("DGTTRR")

print(f"Sequence 1:  (Length: {s.len_sequence()})  {s}")
print(f"Sequence 2:  (Length: {s_1.len_sequence()})  {s_1}")
print(f"Sequence 3:  (Length: {s_2.len_sequence()})  {s_2}")