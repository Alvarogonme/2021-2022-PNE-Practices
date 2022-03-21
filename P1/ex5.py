from seq1 import Seq

PRACTICE = 1
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Seq()
s_2 = Seq("ACTGA")
s_3 = Seq("DGTTRR")

print(f"Sequence 0:  (Length: {s.len_sequence()})  {s}")
a, c, g, t = s.total_base()
print("A:", a,  "C:", c,  "T:", t,  "G:", g)
print(f"Sequence 1:  (Length: {s_2.len_sequence()})  {s_2}")
a, c, g, t = s_2.total_base()
print("A:", a,  "C:", c,  "T:", t,  "G:", g)
print(f"Sequence 2:  (Length: {s_3.len_sequence()})  {s_3}")
a, c, g, t = s_3.total_base()
print("A:", a,  "C:", c,  "T:", t,  "G:", g)