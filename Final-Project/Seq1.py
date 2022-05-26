class Seq:

    BASES = ["A", "C", "G", "T"]
    COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    @staticmethod #funcion o metodo que corresponde a toda la clase en general
    def validate_sequence(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] in Seq.BASES:
                 i += 1
            else:
                valid = False
        return valid

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL sequence created!")
        elif Seq.validate_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT sequence detected!")

    def __str__(self):
        return self.bases

    def seq_read_fasta(self, file_name):
        from pathlib import Path

        file_cont = Path(file_name).read_text()
        lines = file_cont.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def seq_len(self):
        """Calculate the length of the sequence"""
        new_len = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            new_len = 0
            return new_len
        else:
            return len(self.strbases)

    def count(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def base_count(self):
        bases_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return bases_dict
        else:
            for e in self.strbases:
                bases_dict[e] += 1
            return bases_dict

    def base_info(self):
        total = f"Sequence: {self.bases}\n"
        frequent_base = None

        d = self.base_count()
        for base, count in d.items():
            total += f"{base}: {count} ({round((count * 100) / self.seq_len()):.1f}%)\n"
            if frequent_base:
                if count > self.count(frequent_base):
                    frequent_base = base
        return total


    def seq_reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        return self.bases[::-1]

    def seq_complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        total = ""
        for base in self.bases:
            total += Seq.COMPLEMENTS[base]
        return total

    def seq_info(self):
        result = f"Total length: {self.seq_len()}<br><br>"
        d = self.base_count()
        for base, count in d.items():  # es lo mismo que poner self.count().items():
            result += f"{base}: {count} ({(count * 100) / self.seq_len()}%)<br><br>"
        return result

    def frequent_base(self):
        bases = ["A", "T", "C", "G"]
        count_A, count_T, count_C, count_G = self.count_base()
        counts = [count_A, count_T, count_C, count_G]
        zipped = zip(counts, bases)
        maximum = max(zipped)
        return maximum

    def len(self):
        return len(self.bases)

    def mult(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            mult_result = "We could not multiply the bases since the sequence is not correct"
        else:
            mult_result = 1
            for e in self.strbases:
                if e == "A":
                    mult_result = mult_result * 2
                elif e == "T":
                    mult_result = mult_result * 5
                elif e == "C":
                    mult_result = mult_result * (-1)
                else:
                    mult_result = mult_result * 3
        return mult_result
