from skimage import *
## from skimage.viewer import ImageViewer
from PIL import  Image
import os
import shutil
import re
import matplotlib.pyplot as plt

def display_image(img):
    image = Image.open(img)
    image.show()

def find_color_from_file_name(filename):
    if os.sep in filename:
        start = filename.rindex(os.sep) + 1
    else:
        start = 0
    if "_" in filename:
        end = filename.rindex("_")
    else:
        end = len(filename)
    return(filename[start:end].lower())

def  merge_vectors(vector_list):
    out_vector = [0,0,0,0]
    length = len(vector_list)
    if length == 0:
        return(out_vector)
    for vector in vector_list:
        red,green,blue,intensity = vector
        out_vector[0]+=red
        out_vector[1]+=green
        out_vector[2]+=blue
        out_vector[3]+=intensity
    out_vector[0] = round(out_vector[0]/length,2)
    out_vector[1] = round(out_vector[1]/length,2)
    out_vector[2] = round(out_vector[2]/length,2)
    out_vector[3] = round(out_vector[3]/length,2)
    return(out_vector)

def normalize_vector(vector):
    red,green,blue = vector
    maximum = max(vector)
    if maximum != 0:
        red = round(red/maximum,2)
        green = round(green/maximum,2)
        blue = round(blue/maximum,2)
    if maximum > 122:
        intensity = 1
    else:
        intensity = 0
    return([red,green,blue,intensity])

def get_vector_from_file(infile):
    line_list = skimage.io.imread(fname=infile)
    pixel_list = []
    for line in line_list:
        dimensions = line.ndim
        if dimensions == 1:
            for pixel in line:
                if pixel > 122:
                    intensity = 1
                else:
                    intensity = 0
                if type(pixel) == int:
                    pixel_list.append([pixel,pixel,pixel,intensity])
        else:
           for pixel in line:
               pixel_list.append(normalize_vector([int(pixel[0]),int(pixel[1]),int(pixel[2])]))
    return(merge_vectors(pixel_list))


def get_color_vector_from_filelist(filelist):
    vectors = []
    for infile in filelist:
        vector = get_vector_from_file(infile)
        vectors.append(vector)
    return(merge_vectors(vectors))

def train_nearest_neighbor(training_list_file,output_file):
    file_dictionary = {}
    color_dictionary = {}
    with open(training_list_file) as instream:
        for filename in instream:
            filename = filename.strip(os.linesep)
            color = find_color_from_file_name(filename)
            if color in file_dictionary:
                file_dictionary[color].append(filename)
            else:
                file_dictionary[color] = [filename]
    for color in file_dictionary:
        print(color)
        files = file_dictionary[color]
        vector = get_color_vector_from_filelist(files)
        color_dictionary[color]=vector
    with open(output_file,'w') as outstream:
        outstream.write('Color,Red,Green,Blue,Intensity\n')
        for color in color_dictionary:
            red,green,blue,intensity = color_dictionary[color]
            line = color+','+str(red)+','+str(green)+','+str(blue)+','+str(intensity)+'\n'
            outstream.write(line)
    
def cosine_similarity(vector1,vector2):
    numerator = 0
    denominator_factor1 = 0
    denominator_factor2 = 0
    for num in range(len(vector1)):
        numerator += (vector1[num]*vector2[num])
        denominator_factor1 += (vector1[num]**2)
        denominator_factor2 += (vector2[num]**2)
    denominator = (denominator_factor1 * denominator_factor2)**.5
    if denominator == 0:
        ## don't divide by zero -- if you have to nothing is similar
        return(0)
    else:
        return(numerator/denominator)

def get_color_dictionary(training_file):
    out_dict = {}
    headings = False
    with open(training_file) as instream:
        for line in instream:
            line = line.strip(os.linesep)
            columns = line.split(',')
            if not headings:
                headings = columns
            else:
                color,red,green,blue,intensity = columns
                red = float(red)
                green = float(green)
                blue = float(blue)
                intensity = float(intensity)
                out_dict[color]= [red,green,blue,intensity]
    return(out_dict)

def classify_based_on_training(training_file,test_files,output_file):
    color_dictionary = get_color_dictionary(training_file)
    print('Loaded color dictionary')
    results = []
    with open(test_files) as instream:
        for infile in instream:
            print('Scoring infile',infile)
            infile = infile.strip(os.linesep)
            vector = get_vector_from_file(infile)
            outcomes = []
            for color in color_dictionary:
                color_vector = color_dictionary[color]
                similarity = cosine_similarity(color_vector,vector)
                outcomes.append([similarity,color])
            outcomes.sort(key=lambda pairs: (-1 * pairs[0])) ## sorts in order of similarity (most similar first)
            results.append([infile,outcomes])
            print(infile,'-->',outcomes)
    with open(output_file,'w') as outstream:
        for result in results:
            infile,outcomes = result
            outline = infile
            for outcome in outcomes:
                score,color = outcome
                outline += ','+str(score)+','+color
            print(outline)
            outstream.write(outline+'\n')

def display_results(result_file,sample_size):
    import random
    lines =[]
    with open(result_file) as instream:
        for line in instream:
            line = line.strip(os.linesep)
            pictfile,comma,scores= line.partition(',')
            lines.append([pictfile, scores])
    output = random.sample(lines,sample_size)
    for item in output:
        print(item)
        display_image(item[0])

def score_cutoff(scores,cutoff,maximum=3):
    print('Next picture')
    cutoff_list = scores.split(',')
    first_score = cutoff_list[0:2]
    if cutoff == 'square':
        minimum_score = float(first_score[0]) ** 2
    elif cutoff == 'cube':
        minimum_score = float(first_score[0]) ** 3
    else:
        print('No valid cutoff strategy declared')
        return()
    output = []    
    color_list = [first_score[1]]
    remainder = cutoff_list[2:]
    position = 2
    current_number = float(first_score[0])
    total =1
    while (position < len(cutoff_list)) \
      and ((current_number > minimum_score) or (total < maximum)):
        next_number = float(cutoff_list[position])
        next_color = cutoff_list[position+1]
        print(next_color)
        if (next_number > minimum_score) and (total <  maximum):
            color_list.append(next_color)
            print(current_number, 'greater than',minimum_score)
            print('or',total,'less than', maximum)
        position += 2
        total += 1
        current_number = next_number
        
    return(color_list)

def display_results_with_cutoff(result_file,sample_size,cutoff='square',maximum=3):
    import random
    lines =[]
    with open(result_file) as instream:
        for line in instream:
            line = line.strip(os.linesep)
            pictfile,comma,scores= line.partition(',')
            lines.append([pictfile, score_cutoff(scores,cutoff,maximum=maximum)])
    output = random.sample(lines,sample_size)
    for item in output:
        print(item)
        display_image(item[0])

def train_kaggle ():
    train_nearest_neighbor('kaggle_training_colors.list','kaggle_training_out_2.csv')

def devtest():
    classify_based_on_training('kaggle_training_out_2.csv','open_jpg.list','open_out_trained_2.csv')

# def devtest_mask():
#     ## did not work well
#     train_nearest_neighbor('mask_triaining.list','kaggle_mask_training_out.csv')

def test_display_results():
    display_results('open_out_trained_2.csv',20)

def test_display_results_with_cutoff():
    display_results_with_cutoff('open_out_trained_2.csv',20)

def test_display_results_with_cutoff2():
    display_results_with_cutoff('open_out_trained_2.csv',20,cutoff='cube',maximum=3)


## next idea: normalize all vectors
## divide all values by max of 3 values
