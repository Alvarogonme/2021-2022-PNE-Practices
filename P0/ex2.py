import seq0

filename = seq0.valid_filename()
sequence = seq0.seq_read_fasta(filename)
print("DNA file: ", filename)
print("The first 20 bases are:")
print(sequence[0:20])