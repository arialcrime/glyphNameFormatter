from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.edit("GREEK PERISPOMENI", "perispomeni")
    self.edit("GREEK KORONIS", "koronis")
    self.edit("GREEK DIALYTIKA TONOS", "dialytikatonos")
    self.edit("GREEK YPOGEGRAMMENI", "iotasubscript")

    self.edit("INVERTED DOUBLE ARCH", 'dblarchinverted')
    self.edit("COMBINING RIGHT ARROWHEAD AND UP ARROWHEAD", "arrowheadrightarrowheadup")

    self.edit("DOUBLE RING", 'doublering')
    self.edit("DOUBLE VERTICAL LINE", 'dblverticalline')
    self.edit("DOUBLE OVERLINE", "dbloverline")
    self.edit("LOW LINE", "lowline")

    self.edit("PLUS SIGN", "plus")
    self.edit("MINUS SIGN", "minus")
    self.edit("LONG SOLIDUS", "soliduslong")
    self.edit("SHORT SOLIDUS", "solidusshort")

    self.edit("HOOK ABOVE", "hoi")
    self.edit("PALATALIZED HOOK", "palatalizedhook")
    self.edit("RETROFLEX HOOK", "retroflexhook")
    self.edit("LEFT ANGLE", "leftangle")
    self.edit("LEFT TACK", 'lefttack')
    self.edit("DOWN TACK", 'downtack')
    self.edit("UP TACK", 'uptack')
    self.edit("RIGHT TACK", 'righttack')
    self.edit("REVERSED COMMA", 'reversedcomma')
    self.edit("TURNED COMMA", "commaturned")
    self.edit("COMMA", "turned")
    self.edit("DOT ABOVE RIGHT", "dotrightabove")
    self.edit("CANDRABINDU", "candrabindu")
    self.edit("EQUALS SIGN", "equal")
    self.edit("ALMOST EQUAL TO ABOVE", "almostequalabove")
    self.edit("GRAVE ACCENT", 'grave')
    self.edit("ACUTE ACCENT", 'acute')
    self.edit("GRAVE TONE MARK", 'gravetone')
    self.edit("ACUTE TONE MARK", 'acutetone')
    self.edit("CIRCUMFLEX ACCENT", 'circumflex')
    self.edit("SEAGULL", "seagull")
    self.edit("SQUARE", "square")
    self.edit("MACRON", "macron")
    self.edit("CARON", "caron")
    self.edit("NOT", "not")
    self.edit("HORN", "horn")
    self.edit("TILDE", "tilde")
    self.edit("CEDILLA", "cedilla")
    self.edit("OGONEK", "ogonek")
    self.edit("LEFT HALF", "halfleft")
    self.edit("RIGHT HALF", "halfright")
    self.edit("RING", "ring")
    self.edit("HOMOTHETIC", "homothetic")
    self.edit("DIAERESIS", self.prefSpelling_dieresis)
    self.edit("INVERTED", "inverted")
    self.edit("OVERLINE", "overline")
    self.edit("LINE", "line")
    self.edit("DOT ABOVE", "dotaccent")
    self.edit("VERTICAL", "vertical")
    self.edit('BRIDGE', "bridge")
    self.edit('ASTERISK', "asterisk")
    self.edit('FERMATA', "fermata")
    self.edit('ZIGZAG', "zigzag")

    self.edit("OVERLAY", "overlay")
    self.edit("SHORT STROKE", "strokeshort")
    self.edit("LONG STROKE", "strokelong")

    self.edit("DOUBLE RIGHTWARDS ARROW", "arrowrightdouble")
    self.edit("UPWARDS ARROW", "arrowup")
    self.edit("LEFT RIGHT ARROW", "arrowleftright")
    self.edit("LEFT ARROWHEAD", "arrowheadleft")
    self.edit("RIGHT ARROWHEAD", "arrowheadright")

    self.edit("DOUBLE", "double")
    self.edit("ABOVE", "above")
    self.edit("BELOW", "below")

    self.edit("BREVE", "breve")

    self.edit("COMBINING", "cmb")
    self.replace("X", "x")

    # oddballs
    self.edit("GRAPHEME JOINER", "graphemejoiner")

    self.edit("LATIN")
    self.handleCase()
    # self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Combining Diacritical Marks")
