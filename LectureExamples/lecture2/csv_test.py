import csv

input_file = "/home/meyers/DataScienceTools/pydata-book-2nd-edition/datasets/haiti/Haiti.csv"

with open(input_file) as instream:
    for line in instream:
        for row in csv.reader(instream):
            for column in row:
                print(column+'\t|||\t',end='')
            print()
            input('pause')
