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


    def seq_read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

