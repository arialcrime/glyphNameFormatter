from glyphNameFormatter.scriptPrefixes import scriptPrefixes


def process(self):
    if self.has("LATIN"):
        self.scriptTag = scriptPrefixes['latin']
    elif self.has("ARMENIAN"):
        self.scriptTag = scriptPrefixes['armenian']
        from glyphNameFormatter.rangeProcessors.armenian import process as processArmenian
        processArmenian(self)
    elif self.has("HEBREW"):
        self.scriptTag = scriptPrefixes['hebrew']
        from glyphNameFormatter.rangeProcessors.hebrew import process as processHebrew
        processHebrew(self)
    
    self.edit("LATIN SMALL LIGATURE FF", "f_f")
    self.edit("LATIN SMALL LIGATURE FI", "fi")
    self.edit("LATIN SMALL LIGATURE FL", "fl")
    self.edit("LATIN SMALL LIGATURE FFI", "f_f_i")
    self.edit("LATIN SMALL LIGATURE FFL", "f_f_l")
    self.edit("LATIN SMALL LIGATURE LONG S T", "longs_t")
    self.edit("LATIN SMALL LIGATURE ST", "s_t")

    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Alphabetic Presentation Forms")
