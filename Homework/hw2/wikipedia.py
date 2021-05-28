import sys
import os
sys.path.append(sys.path[0] + "/../../LectureExamples/lecture2")
from reading_from_wikipedia import *

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

if not os.path.isdir(sys.argv[2]):
    os.mkdir(sys.argv[2])

for line in lines:
    if not line:  # prevent empty line
        continue
    search_term = replace_spaces_with_underscores(line)
    full_page = look_up_wikipedia_page_from_internet(search_term)
    if non_match(full_page):
        with open(sys.argv[2] + os.sep + line, "w") as f:
            f.write("*** No Wikipedia Entry Found ***")
    else:
        paragraph_start = re.compile('<p[^>]*>')
        paragraph_end = re.compile('</p>')
        done = False
        start = 0
        with open(sys.argv[2] + os.sep + line, "w") as f:
            while not done:
                next_paragraph_start = paragraph_start.search(full_page, start)
                if next_paragraph_start:
                    start = next_paragraph_start.end()
                    next_paragraph_end = paragraph_end.search(full_page, start)
                    if next_paragraph_end:
                        end = next_paragraph_end.start()
                        text = remove_xml(full_page[start:end])
                        if re.search('[a-z]{3}', text):
                            f.write(text)
                        start = next_paragraph_end.end()
                    else:
                        done = True
                else:
                    done = True
