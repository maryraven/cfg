from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize

with open('input_file.txt') as f:
    raw = f.readlines()
    input = [l.strip().split() for l in raw]
    print(input)

    # http://www.nltk.org/book/ch08.html
    calc_grammar = nltk.CFG.fromstring("""
        S -> N OPP
        OPP -> OP N | OPP OP N
        N -> 'zero' | 'one'| 'two' | 'three' | 'four' | 'five' | 'six' | 'seven' | 'eight' | 'nine'
        OP -> 'plus' | 'minus' | 'times'| 'divide'
        """)

    parser = nltk.ChartParser(calc_grammar)
    for sentence in input:
        for tree in parser.parse(sentence):
            print(tree)
