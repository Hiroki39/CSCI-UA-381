from skimage_process import *
import os
import shutil
import re

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
    out_vector = [0,0,0]
    length = len(vector_list)
    for vector in vector_list:
        red,green,blue = vector
        out_vector[0]+=red
        out_vector[1]+=green
        out_vector[2]+=blue
    out_vector[0] = round(out_vector[0]/length)
    out_vector[1] = round(out_vector[1]/length)
    out_vector[2] = round(out_vector[2]/length)
    return(out_vector)

def get_vector_from_file(infile):
    print (infile)
    line_list = skimage.io.imread(fname=infile)
    print(line_list)
    input('pause')
    pixel_list = []
    for line in line_list:
        dimensions = line.ndim
        if dimensions == 1:
            for pixel in line:
                if type(pixel) == int:
                    pixel_list.append([pixel,pixel,pixel])
        else:
           for pixel in line:
               pixel_list.append([int(pixel[0]),int(pixel[1]),int(pixel[2])])
    return(merge_vectors(pixel_list))


def get_color_vector_from_filelist(filelist):
    vectors = []
    for infile in filelist:
        vector = get_vector_from_file(infile)
        vectors.append(vector)
    return(merge_vectors(vectors))

def train_nearest_neighbor(training_list_file,outputfile):
    file_dictionary = {}
    color_dictionary = {}
    with open(training_list_file) as instream:
        for filename in instream:
            filename = filename.strip(os.sep)
            color = find_color_from_file_name(filename)
            if color in file_dictionary:
                file_dictionary[color].append(filename)
            else:
                file_dictionary[color] = [filename]
    for color in file_dictionary:
        vector = get_color_vector_from_filelist(file_dictionary[color])
        color_dictionary[color]=vector
    with open(output_file,'w') as outstream:
        outstream.write('Color,red,green,blue\n')
        for color in file_dictionary:
            red,green,blue = file_dictionary[color]
            line = color+','+str(red)+','+str(green)+','+str(blue)+'\n'
            outstream.write(line)
    
        

