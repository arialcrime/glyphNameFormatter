
def process(self):
    self.edit("TELUGU")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.edit("VOWEL")
    self.edit("SIGN", "sign")
    self.processAs("Helper Indic")
    self.processAs("Helper Numbers")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Telugu")