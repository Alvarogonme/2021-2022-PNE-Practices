import seq0

FOLDER = "../Session-04/"

list_genes = ["U5", "FRAT1", "ADA", "FXN"]
for l in list_genes:
    print(len(seq0.seq_read_fasta(FOLDER + l + ".txt")))