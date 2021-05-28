from skimage_process import *
import os
import shutil

def filter_pixel(number,binary_filter):
    if binary_filter:
        if number >= 128:
            return(255)
        else:
            return(0)
    else:
        return(number)

 ## green + blue --> cyan (light-blue)
## red + green --> yellow
## red + blue --> magenta (purple)

def classify_one_image(image_matrix,strategy,binary_filter=False,secondary_margin=50,combo_percent = 0):
    global debug_line
    if strategy in  ['majority','plurality']:
        red = 0
        green = 0
        blue = 0
        cyan = 0
        yellow = 0
        magenta = 0
        other = 0
        black_and_white = 0
        for line in image_matrix:
            debug_line = line
            dimensions = line.ndim
            if dimensions == 1:
                for pixel in line:
                    if type(pixel) == int:
                        black_and_white += 1
            else:
                for pixel in line:
                    red_pixel = int(pixel[0])
                    green_pixel = int(pixel[1])
                    blue_pixel = int(pixel[2])
                    if (green_pixel >= ((combo_percent/100) * blue_pixel))  and \
                        (blue_pixel >=((combo_percent/100) * green_pixel)):
                        cyan_pixel = (green_pixel+blue_pixel)/2
                    else:
                        cyan_pixel = 0
                    if (red_pixel >= ((combo_percent/100) * green_pixel))  and \
                        (green_pixel >=((combo_percent/100) * red_pixel)):
                        yellow_pixel = (red_pixel+green_pixel)/2
                    else:
                        yellow_pixel = 0
                    if (red_pixel >= ((combo_percent/100) * blue))  and \
                        (blue_pixel >=((combo_percent/100) * red_pixel)):
                        magenta_pixel = (red_pixel+blue_pixel)/2
                    else:
                        magenta_pixel = 0
                    if strategy == 'majority':
                        if (red_pixel == green_pixel) and (red_pixel == blue_pixel):
                            black_and_white += 1
                        elif red_pixel > (green_pixel + blue_pixel):
                            red +=1
                        elif blue_pixel > (red_pixel + green_pixel):
                            blue +=1
                        elif green_pixel > (red_pixel + blue_pixel):
                            green +=1
                        elif (green_pixel > red_pixel) and (blue_pixel > red_pixel):
                            cyan +=1
                        elif (red_pixel > blue_pixel) and (green_pixel > blue_pixel):
                            yellow +=1
                        elif (red_pixel > green_pixel) and (blue_pixel > green_pixel):
                            magenta +=1
                        else:
                            other +=1
                    else:
                        if (red_pixel == green_pixel) and (red_pixel == blue_pixel):
                            black_and_white += 1
                        elif (red_pixel > green_pixel) and (red_pixel > blue_pixel) and \
                          (red_pixel > (cyan_pixel+secondary_margin)):
                            red +=1
                        elif (blue_pixel > red_pixel) and (blue_pixel > green_pixel) and \
                          (blue_pixel >  (yellow_pixel+secondary_margin)):
                            blue +=1
                        elif (green_pixel > red_pixel) and (green_pixel > blue_pixel) and \
                        (green_pixel > (magenta_pixel+secondary_margin)):
                            green +=1
                        elif (cyan_pixel > yellow_pixel) and   (cyan_pixel >  magenta_pixel):
                            cyan +=1
                        elif (yellow_pixel > magenta_pixel) and  (yellow_pixel > cyan_pixel):
                              yellow +=1
                        elif (magenta_pixel > yellow_pixel) and \
                            (magenta_pixel > cyan_pixel):
                              magenta +=1                            
                        else:
                            other +=1
        maximum = max([red,blue,green,magenta,yellow,cyan,black_and_white])
        total = sum([red,blue,green,magenta,yellow,cyan,black_and_white])
        if ((strategy == 'majority') and  (maximum > (total-maximum))) \
          or (strategy != 'majority'):
            if maximum == 0:
                output = 'other'
            elif (black_and_white == maximum) and (total == black_and_white):
                output = 'black_and_white'
            elif red == maximum:
                output = 'red'
            elif blue == maximum:
                output = 'blue'
            elif green == maximum:
                output = 'green'
            elif magenta == maximum:
                output = 'magenta'
            elif yellow == maximum:
                output = 'yellow'
            elif cyan == maximum:
                output = 'cyan'
            else:
                output = 'other'
        else:
            output = 'other'
    else:
        print('Strategy is unknown')
        output='other'
    if binary_filter:
        output = output + '_binary'
    return(output)

def copy_file_to_group(outdirectory,filename,group_name):
    if not(os.path.isdir(outdirectory)):
        os.mkdir(outdirectory)
    subdirectory = outdirectory+os.sep+group_name
    leaf_file = filename.split(os.sep)[-1]
    if not (os.path.isdir(subdirectory)):
        os.mkdir(subdirectory)
    shutil.copyfile(filename,subdirectory+os.sep+leaf_file)

def sort_image_files(file_list,strategy,outdirectory,binary_filter=False,secondary_margin=50,combo_percent=0):
    with open(file_list) as instream:
        for filename in instream:
            filename = filename.strip(os.linesep)
            line_list = skimage.io.imread(fname=filename)
            group_name = classify_one_image(line_list,strategy,\
                                                binary_filter=binary_filter,secondary_margin=secondary_margin,\
                                                combo_percent=combo_percent)
            copy_file_to_group(outdirectory,filename,group_name)

def test1():
    sort_image_files('open_jpg.list','majority','open_image_sort_majority')

def test1a():
    sort_image_files('open_jpg.list','majority','open_image_sort_majority_75',combo_percent=75)

def test2():
    sort_image_files('open_jpg.list','plurality','open_image_sort_plurality_0',secondary_margin=0)

def test3():
    sort_image_files('open_jpg.list','plurality','open_image_sort_plurality_50')

def test3a():
    sort_image_files('open_jpg.list','plurality','open_image_sort_plurality_50_75',combo_percent=75)

def test4():
    sort_image_files('open_jpg.list','plurality','open_image_sort_plurality_25',secondary_margin=0)

def kaggle_4_tests():
    for strategy,outdir,margin in [['majority','kaggle_color_majority',0],\
                                       ['plurality','kaggle_color_plurality_0',0],\
                                       ['plurality','kaggle_color_plurality_25',25],\
                                       ['plurality','kaggle_color_plurality_50',50]]:
        sort_image_files('kaggle_training_colors.list',strategy,outdir,secondary_margin=margin)

def kaggle_test_2():
    strategy='plurality'
    margin=50
    combo_percent=75
    outdir ='kaggle_color_plurality_50_75'
    sort_image_files('kaggle_training_colors.list',strategy,outdir,secondary_margin=margin,combo_percent=combo_percent)

def display_sample_images(directory,sample_size):
    import random
    for subdirectory in os.listdir(directory):
        print(subdirectory)
        path = directory+os.sep+subdirectory
        if os.path.isdir(path):
            files = os.listdir(path)
            short_list = []
            if len(files) > sample_size:
                for n in range(sample_size):
                    done = False
                    while not done:
                        next_file = random.choice(files)
                        if next_file in short_list:
                            pass
                        else:
                            short_list.append(next_file)
                            done =True
            else:
                short_list = files
            print(len(short_list),short_list)
            for image_file in short_list:
                full_file = path+os.sep+image_file
                display_image(full_file)

def display_test1():
    display_sample_images('open_image_sort_majority',5)
    ## same for plurality_0, 25 and 50

def display_test2():
    for dir in ['kaggle_color_majority',	 'kaggle_color_plurality_0',\
                    'kaggle_color_plurality_25', 'kaggle_color_plurality_50']:
                    print('****',dir,'****')
                    display_sample_images(dir,5)
                    
def display_test3():
    dir = 'kaggle_color_plurality_50_75'
         display_sample_images(dir,5)
