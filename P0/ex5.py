import seq0

print("-----| Exercise 5 |------")
exit = False
while not exit:
    filename = seq0.valid_filename()
    if filename == "exit":
        exit = True
    else:
        seq = seq0.seq_read_fasta(filename)
        d = seq0.total_base(seq)
        print("Gene", filename + ":", d)
        exit = True