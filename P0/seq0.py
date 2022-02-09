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
