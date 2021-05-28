import sys
import os
import skimage
import skimage.io
import skimage.viewer
from skimage_process import *
import time

def display_images_for_n_seconds(file_list,seconds):
    with open(file_list) as instream:
        for filename in instream:
            filename = filename.strip(os.linesep)
            display_image(filename)
        time.sleep(seconds)

def main(args):
    display_images_for_n_seconds(args[1],int(args[2]))
sys.exit(main(sys.argv))
