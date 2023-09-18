class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        if type(text) != str:
            raise TypeError("text must be a string")
        elif not text[0].isupper() or text[-1] not in [".", "?", "!"]:
            return False
        return True

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass