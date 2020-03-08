file_path = "foo.txt"

with open(file_path) as f:
    contents = f.read()


class CustomOpen:
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with CustomOpen(file_path) as f:
    contents = f.read()