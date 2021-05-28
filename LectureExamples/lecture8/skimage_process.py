import skimage.io
import skimage
import skimage.viewer
import time

def make_table_of_pixels(infile,outfile):
    line_list = skimage.io.imread(fname=infile)
    with open(outfile,'w') as outstream:
        for line in line_list:
            for pixel in line:
                outstream.write(str(pixel)+'\t')
            outstream.write('\n')

def display_image(infile):
    instream = skimage.io.imread(fname=infile)
    viewer = skimage.viewer.ImageViewer(instream)
    viewer.show()

def test1():
    ## display_image('chessboard.png')
    make_table_of_pixels('chessboard.png', 'chessboard.tsv')

def test2():
    display_image('marble24.png')
    make_table_of_pixels('marble24.png', 'marble24.tsv')

def test3():
    ## infile = "lego/LEGO brick images v1/3003 Brick 2x2/0050"
    ## infile = "lego/LEGO brick images v1/3003 Brick 2x2/0060"
    infile = "lego/dataset/99301 roof tile inside 3x3 397R"
    ## display_image(infile+".png")
    make_table_of_pixels(infile+'.png',infile+'.tsv')

def test4():
    infile = "open_images/000002b66c9c498e"
    make_table_of_pixels(infile+'.jpg',infile+'.tsv')

def test5():
    infile = "open_images/00004fd8760d4346"
    make_table_of_pixels(infile+'.jpg',infile+'.tsv')

