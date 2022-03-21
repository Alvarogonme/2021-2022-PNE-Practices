import seq0

exit = False
while not exit:
    filename = seq0.valid_filename()
    if filename == "exit":
        exit = True
    else:
        print("-----| Exercise 8 |------")
        seq = seq0.seq_read_fasta(filename)
        d = seq0.total_base(seq)
        base = seq0.genes(d)
        print("Gene", filename + ": " + "Most frequent base" + ": " + base)
        exit = True