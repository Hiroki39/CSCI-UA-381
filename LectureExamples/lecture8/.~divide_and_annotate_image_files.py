import os
import re
import random
import skimage_process

## There are 34 students
## Each student should annotate 29 files that will be duplicated
## Each student will also annotate the same 14 files as everyone else
## for a total of 43 files each

def initialize_students_and_files (students,files):
    students = []
    files = []    
    with open('student.list') as instream:
        for line in instream:
            line = line.strip(os.linesep)
            if re.search('[a-z]',line):
                students.append(line)    
    with open('open_jpg.list') as instream:
        for line in instream:
            line = line.strip(os.linesep)
            if re.search('[a-z]',line):
                files.append(line)
    return(students,files)

def choose_students_for_files(infile,students,total,student_dict,each):
    checked = []
    so_far = 0
    while (len(checked)<len(students)) and (so_far < total):
        student = random.choice(students)
        if student in checked:
            pass
        elif not student in student_dict:
            student_dict[student]= [infile]
            checked.append(student)
            so_far += 1
        elif len(student_dict[student]) >= each:
            pass
        elif not infile in student_dict[student]:
            student_dict[student].append(infile)
            checked.append(student)
            so_far += 1

def divide_files(student_list,file_list,common,each,out_dir,maxn=2):
    students,files = initialize_students_and_files(student_list,file_list)
    common_files = []
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    for num in range(common):
        common_files.append(pick_a_file(files))
    counts = {}
    student_dict = {}
    for infile in files:
        choose_students_for_files(infile,students,2,student_dict,each)
    for student in students:
        outfiles = student_dict[student][:] ## outfiles is a copy of the dictionary entry
        student_file_list = out_dir+os.sep+student+'.list'
        outfiles.extend(common_files)
        with open(student_file_list,'w') as outstream:
            for outfile in outfiles:
                outstream.write(outfile+'\n')

def divide_data_spring_2021():
    divide_files("student.list","open_jpg.list",14,29,"annotation_tasks")

def choose_one_color(choices,colors):
    more_colors = set(colors)-set(choices)
    print('Possible additional colors include:', more_colors)
    print('So far you have chosen these colors:',choices)
    print('''Add any color that is featured in the picture. 
For most pictures, this is one, two or three colors total.''')
    answer = input('Which color do you choose?')
    answer = answer.lower()
    if not answer in more_colors:
        print(answer,'is not a member of ',more_colors,'Please try again')
        print('''Choose  the closest color, e.g., we will assume that "gold"
 is "yellow", "silver or light gray" is "white", and "dark gray" is a shade of "black"''')
        return(choose_one_color(choices,colors))
        ## recursive call
    else:
        return(answer)

def are_you_finished():
    answer = input('Are you finished classifying this image? ')
    answer = answer.lower()
    if answer[0] == 'y':
        return(True)
    else:
        return(False)

def choose_about_3_colors(): 
    colors = ['black', 'blue', 'brown', 'green', 'orange', 'red', 'violet', 'white', 'yellow']
    done = False
    choices = []
    while (not done):
        color = choose_one_color(choices,colors)
        choices.append(color)
        done = are_you_finished()
    return(choices)

def one_more_time():
    print('Please answer "yes" or "no" to the following question.')
    answer = input('Would you like to add more colors')
    answer = answer.lower()
    if answer[0] == 'y':
        return(True)
    elif answer[0] == 'n':
        return(False)
    else:
        print('Your answer:',answer,'is neither "yes" nor "no". Please try again.')
        ## recursive call
        return(one_more_time())
    
def do_over():
    answer = input('Would you like to erase the annotation for the last image and redo it?')
    answer = answer.lower()
    if answer[0] == 'y':
        return(True)
    else:
        return(False)
    
def annotate_files(infile,outfile):
    color_choices = []
    with open(infile) as instream,open(outfile,'w') as outstream:
        for image_file in instream:
            image_file = image_file.strip(os.linesep)
            print('''The image file will now be displayed. Kill the file and 
choose up to three colors as annotation.''')
            print('''You will be given the opportunity to see the picture again
and change the annotation''')
            skimage_process.display_image(image_file)
            three_colors = choose_about_3_colors()
            while one_more_time():
                skimage_process.display_image(image_file)
                print('You previously chose:',three_colors)
                print('Enter 3 new colors')
                three_colors = choose_about_3_colors()
            redo = do_over()
            if redo:
                skimage_process.display_image(image_file)
                three_colors = choose_about_3_colors()
                while one_more_time():
                    skimage_process.display_image(image_file)
                    print('You previously chose:',three_colors)
                    print('Enter 3 new colors')
                    three_colors = choose_about_3_colors()
            output_line = image_file
            for color in three_colors:
                output_line = output_line + "," + color
            output_line += '\n'
            outstream.write(output_line)
            
def adam_test():
    annotate_files('annotation_tasks/adam_meyers.list','meyers_out.csv')
