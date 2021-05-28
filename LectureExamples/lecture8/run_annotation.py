from divide_and_annotate_image_files import *
import sys


def main(args):
    annotate_files('annotation_tasks/' + args[1], args[2])


sys.exit(main(sys.argv))
