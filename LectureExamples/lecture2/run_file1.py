#!/usr/bin/env python3
def main():
    import os
    print('This is a print statement')
    human_answer = input('Write a sentence and then hit return')
    print('Repeating what you said:',human_answer)
    file_to_read = input('What file should I read in? ')
    print('That file has the following lines in it:')
    outlines = []
    with open(file_to_read) as instream:
        for line in instream:
            print(line)
            outlines.append(line)
    your_name = input('What is your name? ')
    print('Writing to your version of the file.')
    with open(your_name+'_'+file_to_read,'w') as outstream:
        for line in outlines:
            line = line.strip(os.linesep)
            outstream.write(your_name+': '+line + '\n')

main()
