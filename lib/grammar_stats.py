class GrammarStats:
    def __init__(self):
        self.errors = 0
        self.correct = 0

    def check(self, text):
        if type(text) != str:
            raise TypeError("text must be a string")
        elif not text[0].isupper() or text[-1] not in [".", "?", "!"]:
            self.errors += 1
            return False
        self.correct += 1
        return True

    def percentage_good(self):
        return (self.correct / (self.correct + self.errors)) * 100