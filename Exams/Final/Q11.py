import math
import os
import string


def calculate_idf_score(directory):
    files = os.listdir(directory)
    num_files = len(files)
    idf_score = {}
    for curr_file in files:
        with open(directory + os.sep + curr_file) as f:
            text = f.read().replace('\n', ' ').translate(
                str.maketrans('', '', string.punctuation)).lower()
            word_set = set(text.split(' '))
            for word in word_set:
                if word in idf_score:
                    idf_score[word] += 1
                else:
                    idf_score[word] = 1

    for key in idf_score:
        idf_score[key] = math.log(num_files / idf_score[key])

    return idf_score
