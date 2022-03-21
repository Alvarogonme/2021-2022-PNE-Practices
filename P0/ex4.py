import seq0

exit = False
while not exit:
    filename = seq0.valid_filename()
    if filename == "exit":
        exit = True
    else:
        print("-----| Exercise 4 |------")
        seq = seq0.seq_read_fasta(filename)
        base_a, base_c, base_g, base_t = seq0.count_base(seq)
        print("gene", filename + ":")
        print("A: ", base_a)
        print("C: ", base_c)
        print("G: ", base_g)
        print("T: ", base_t)
        exit = True
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