#!/usr/bin/env python3

## This program takes 2 arguments: a text file and a letter
## It will print out character information for each line in the text file
## If the second argument is "p", it will pause between lines,
## proceeding when you it enter. Otherwise, it will print out the information
## continuously

import sys
    
def display_characters_line(line,number,pause_between_lines):
    print('Line Number:',number,end="\t")
    for character in line:
        number = ord(character)
        triple = [number]
        if character == ' ':
            triple.append('SPC')
        elif character == '\n':
            triple.append('NEWLINE')
        elif character =='\t':
            triple.append('TAB')
        elif character.isprintable():
            triple.append(character)
        else:
            triple.append ('UNPRINTABLE')
        print(triple,end='\t')
    print()
    if pause_between_lines:
        input('pause until next return')

def main(args):
    import os
    line_number = 0
    with open(args[1]) as instream:
        if 'p' in args[2].lower():
            pause_between_lines = True
        else:
            pause_between_lines = False
        for line in instream:
            line_number += 1
            display_characters_line(line,line_number,pause_between_lines)

sys.exit(main(sys.argv))

