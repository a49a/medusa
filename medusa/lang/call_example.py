class CountMissing:

    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

c = CountMissing()
c()
c()
print(c.added)