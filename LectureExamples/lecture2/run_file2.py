#!/usr/bin/env python3

## arg1 and arg2 should be words
## arg3 should be a filename
## and arg4 should be your name

import sys

def main(args):
    import os
    ## args is a list of arguments such that,
    ## 0 is the function, 1 is the 1st argument, 2 is the 2nd and so on
    print(1, args[1], 2, args[2])
    file_to_read = args[3]
    your_name = args[4]
    outlines = []
    with open(file_to_read) as instream:
        for line in instream:
            print(line)
            outlines.append(line)
    print('Writing to your version of the file.')
    with open(your_name+'_'+file_to_read,'w') as outstream:
        for line in outlines:
            line = line.strip(os.linesep)
            outstream.write(your_name+': '+line + '\n')

sys.exit(main(sys.argv))
