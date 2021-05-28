import sys
import os
import skimage.io
import skimage
from skimage_process import *
import time

def display_image(infile)
    import subprocess
    instream = skimage.io.imread(fname=infile)
    viewer = skimage.viewer.ImageViewer(instream)
    viewer.show()


def display_images_for_n_seconds(file_list,seconds):
    with open(file_list) as instream:
        for filename in instream:
            filename = filename.strip(os.linesep)
            

sys.exit(main(sys.argv))
