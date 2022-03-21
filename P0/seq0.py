def seq_ping():
    print("OK")

def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter a filename: ")
        try:
            f = open("../Session-04/" + filename + ".txt", "r")
            exit = True
            return "../Session-04/" + filename + ".txt"
        except FileNotFoundError:
            print("File was not found. Try again.")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_bases(seq):
    bases_a = 0
    bases_c = 0
    bases_g = 0
    bases_t = 0
    for i in seq:
        if i == "A":
            bases_a += 1
        elif i == "C":
            bases_c += 1
        elif i == "G":
            bases_g += 1
        elif i == "T":
            bases_t += 1
    return bases_a, bases_c, bases_g_g, bases_t

def total_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d

def seq_complement(seq):
    frag = seq[0:20]
    complementary = ""
    for i in frag:
        if i == "A":
            complementary += "T"
        elif i == "T":
            complementary += "A"
        elif i == "C":
            complementary += "G"
        elif i == "G":
            complementary += "C"
    return complementary

def processing_genes(d):
    highest_value = 0
    for k, v in d.items():
        if int(v) > highest_value:
            highest_value = int(v)
            base = k
    return base