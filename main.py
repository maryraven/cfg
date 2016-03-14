from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize

with open('input_file.txt') as f:
    raw = f.readline().strip()
    input = raw.split()
    print(input)

    # http://www.nltk.org/book/ch08.html
    calc_grammar = nltk.CFG.fromstring("""
        S -> SOP | SOP EOP
        SOP -> N OP N
        EOP -> OP N
        N -> 'zero' | 'one'| 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine'
        OP -> 'plus' | 'times'| 'divide' | 'minus'
        """)

    parser = nltk.ChartParser(calc_grammar)
    for tree in parser.parse(input):
        print(tree)
