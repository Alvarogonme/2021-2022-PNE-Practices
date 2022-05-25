import seq0
exit = False
while not exit:
    filename = seq0.valid_filename()
    if filename == "none":
        exit = True
    else:
        seq = seq0.seq_read_fasta(filename)
        bases_a, bases_c, bases_g, bases_t = seq0.seq_bases(seq)
        print(count_a, count_c, count_g, count_t)