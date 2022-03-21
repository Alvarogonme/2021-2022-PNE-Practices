from seq1 import Seq

PRACTICE = 1
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Seq()
s_2 = Seq("ACTGA")
s_3 = Seq("DGTTRR")


print(f"Sequence 0:  (Length: {s.len_sequence()})  {s}")
print("Bases:")
d = s.total_count_base()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nRev:", s.seq_reverse())

print(f"Sequence 1:  (Length: {s_2.len_sequence()})  {s_2}")
print("Bases:")
d = s_2.total_count_base()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nRev:", s_2.seq_reverse())

print(f"Sequence 2:  (Length: {s_3.len_sequence()})  {s_3}")
print("Bases:")
d = s_3.total_count_base()
for k,v in d.items():
    print(k + ":", str(v), end=" ")
print("\nRev:", s_3.seq_reverse())