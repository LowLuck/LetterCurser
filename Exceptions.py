class LetterFileReadError(Exception):
    def __init__(self, message="Error while reading Letters.txt. Wrong formatting?"):
        self.message = message
        super().__init__(self.message)
