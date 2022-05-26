def adding(self):
    total_sum = 0
    for l in self.strbases:
        if l == "A":
            total_sum += 3
        elif l == "C":
            total_sum -= 2
        elif l == "G":
            total_sum += 4
        elif l == "T":
            total_sum += 6
    return total_sum

   def mult(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            mult_result = "We could not multiply the bases since the sequence is not correct"
        else:
            mult_result = 1
            for e in self.strbases:
                if e == "A":
                    mult_result = mult_result * 2
                elif e == "T":
                    mult_result = mult_result * 5
                elif e == "C":
                    mult_result = mult_result * (-1)
                else:
                    mult_result = mult_result * 3
        return mult_result

elif cmd == "ADD":
print(Fore.LIGHTYELLOW_EX + "ADD command!!")
seq = Seq(arg)
# now i create a method in Seq1 in order to perform the adding operations and then use that
# function

# we also use the valid sequence command in Seq1

if seq.valid_sequence() != True:
    print("The client has not introduced a valid sequence...")
    response = "We could not multiply the bases since the sequence is not correct."
    cs.send(response.encode())
elif seq.valid_sequence() == True:
    print(f"Sequence: {seq}, adding: {seq.adding()}")
    response = f"Sequence: {seq}" + f"\nAdding: {seq.adding()}"
    cs.send(response.encode())


