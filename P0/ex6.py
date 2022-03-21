import seq0

exit = False
while not exit:
    filename = seq0.valid_filename()
    if filename == "exit":
        exit = True
    else:
        print("------| Exercise 6 |------")
        seq = seq0.seq_read_fasta(filename)
        reverse = seq0.reverse(seq)
        print("Gene", filename + ":")
        print("Frag: ", seq[0:20])
        print("Rev: ", reverse)
        exit = True