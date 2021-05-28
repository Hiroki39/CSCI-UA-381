import os
import sys
import string
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
sys.path.append(sys.path[0] + "/../../LectureExamples/lecture2")
from blanks_globals import stop_words, pos_categories, \
    basic_wikipedia_search_url
from reading_from_wikipedia import replace_spaces_with_underscores


search_term = input("Enter the search term: ")
print("------------------------------------------")
search_term = replace_spaces_with_underscores(search_term)

url = basic_wikipedia_search_url + search_term
try:
    output = urlopen(url)
except HTTPError:
    print("Term not found on Wikipedia")
    sys.exit(1)

soup = BeautifulSoup(output, 'lxml')
paragraphs = soup.find_all('p')

text = ""

for paragraph in paragraphs:
    text += paragraph.text
    if len(text.split()) > 100:
        break

processed_text = text.translate(str.maketrans(
    "", "", string.punctuation + string.digits + '–'))

word_set = set(processed_text.lower().split())
word_set.difference_update(stop_words)

words_to_be_replaced = random.sample(list(word_set), 10)

print("You are going to choose a category for each word, \
       there are 10 words in total")
print(f"Possible categories include: {', '.join(pos_categories)}")
print("------------------------------------------")

categories = []
for word in words_to_be_replaced:
    categories.append(input(f"Choose a category for the word '{word}': "))

if os.name == 'nt':  # for windows
    os.system('cls')
else:  # for mac and linux
    os.system('clear')

print("You are going to replace 10 words in total: ")
for word, category in zip(words_to_be_replaced, categories):
    replace_word = input(f"Enter a(an) {category}: ").lower()
    text = text.replace(word, replace_word)
    text = text.replace(word.capitalize(), replace_word.capitalize())
print("------------------------------------------")
print(f"Text after replacement: \n{text}")
