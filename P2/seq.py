class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL seq created")
            exit = False
        else:
            if not self.validate_sequence():
                self.strbases = "ERROR"
                print("INVALID seq!")
            else:
                print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def valid_filename(self):
        exit = False
        while not exit:
            folder = "./sequences/"
            filename = input("Enter a filename: ")
            try:
                f = open(folder + filename + ".txt", "r")
                exit = True
                return filename + ".txt"
            except FileNotFoundError:
                print("File was not found. Try again.")

    @staticmethod
    def correct_sequence(sequence):
        valid = True
        i = 0
        while i < len(sequence):
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def validate_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def len_sequence(self):
        """Calculate the length of the sequence"""
        if self.validate_sequence():
            return len(self.strbases)
        else:
            return 0

    def total_base(self):
        base_a = 0
        base_c = 0
        base_g = 0
        base_t = 0
        for i in self.strbases:
            if i == "A":
                base_a += 1
            elif i == "C":
                base_c += 1
            elif i == "G":
                base_g += 1
            elif i == "T":
                base_t += 1
        return base_a, base_c, base_g, base_t

    def total_count_base(self):
        d = {"A": 0, "C": 0, "G": 0, "T": 0}
        for b in self.strbases:
            try:
                d[b] += 1
            except BaseException:
                return d
        return d

    def seq_reverse(self):
        if self.validate_sequence():
            fragment = self.strbases
            reverse = fragment[::-1]
            return reverse
        else:
            return self.strbases

    def seq_complement(self):
        if self.validate_sequence():
            frag = self.strbases
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
        else:
            return self.strbases

    def seq_read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

    def genes(self, d):
        highest_value = 0
        for k, v in d.items():
            if int(v) > highest_value:
                highest_value = int(v)
                base = k
        return base
