import os
import re
import random

## There are 34 students
## Each student should annotate 29 files that will be duplicated
## Each student will also annotate the same 14 files as everyone else
## for a total of 43 files each

def initialize_students_and_files (students,files)
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

def pick_a_file(file_list):
    number = random.randint(0,len(file_list-1))
    return(file_list.pop(number))
    
def divide_files(student_list,file_list,common,each)
    students,files = initialize_students_and_files(student_list,file_list)
    common_files = []
    for num in range(common):
        common_files.append(pick_a_file(files))
    for student in students:
        outfiles = common_files[:] ## a separate copy of common_files
        for num in range(each):
            outfiles.append(pick_a_file(files))
        student_file_list = student+'.list'
        with open(student_file_list,'w') as outstream:
            for outfile in outfiles:
                outstream.write(outfile+'\n')


