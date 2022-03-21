import seq0

print("-----| Exercise 3 |------")

list_genes = ["U5", "FRAT1", "ADA", "FXN"]
for l in list_genes:
    print(l, "length --->", len(seq0.seq_read_fasta(l + ".txt")))