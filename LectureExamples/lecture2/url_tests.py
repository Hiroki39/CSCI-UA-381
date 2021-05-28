from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

## The above two lines are needed to read in wikipedia pages smoothly
## Some instructions follow in order to make this work properly

## urlib is a standard library
## BeautifulSoup needs to be installed
## See https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm
## You may have to install pip (or Conda) first
##
## Installing on an Apple computer (command line):
## curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
## python3 get-pip.py
## pip install BeautifulSoup
## or if this does not work
## pip install beautifulsoup4

## Windows
## Install pip
## 1) download get-pip.py
## 2) load this file from idle
## 3) In my windows system I got an error:
##  WARNING: The scripts pip.exe, pip3.9.exe and pip3.exe are installed in
## 'C:\Users\AdamMeyers\AppData\Local\Programs\Python\Python39\Scripts'
## 
## 4) If you get the same error, you will need to add the indicated path to your "path"
##     A) search for the environmental variable from the Windows Prompt
##     B) click on your "path" variable and "edit text"
##     C) at the end of the current value add the equivalent of
##     "C:\Users\AdamMeyers\AppData\Local\Programs\Python\Python39\Scripts "
##     to the end of the path after the semicolon (;) and then add a semicolon after this path as well.
##  5) Then I loaded the power shell and typed the following:
##       pip install BeautifulSoup
##   -- if you get an error message because it cannot find BeautifulSoup, try
##       pip install beautifulsoup4
##

def test_yahoo_paragraph():
    yahoo_search_test = 'https://search.yahoo.com/search?p=blah_blah'
    output = urlopen(yahoo_search_test)
    soup = BeautifulSoup(output,'lxml')
    paragraphs = soup.find_all('p')
    
    for paragraph in paragraphs:
        print('Unedited:',paragraph)
        input('pause')
        print('Just text:',paragraph.text)
        input('pause')
    
