"""
Tool to create all LaTeX math commands on letters in the alphabet
"""

import os
from string import ascii_uppercase

with open('alphabet.tex', 'w') as fp:
    fp.write('% mathrm\n')
    for letter in ascii_uppercase:
        fp.write(f'\\newcommand{{\\r{letter}}}{{\\mathrm{{{letter}}}}}\n')
    fp.write('% mathcal\n')
    for letter in ascii_uppercase:
        fp.write(f'\\newcommand{{\\c{letter}}}{{\\mathcal{{{letter}}}}}\n')
    fp.write('% mathsf\n')
    for letter in ascii_uppercase:
        fp.write(f'\\newcommand{{\\s{letter}}}{{\\mathsf{{{letter}}}}}\n')
    fp.write('% mathbb\n')
    for letter in ascii_uppercase:
        fp.write(f'\\newcommand{{\\b{letter}}}{{\\mathbb{{{letter}}}}}\n')
    fp.write('% mathfrak\n')
    for letter in ascii_uppercase:
        fp.write(f'\\newcommand{{\\f{letter}}}{{\\mathfrak{{{letter}}}}}\n')
