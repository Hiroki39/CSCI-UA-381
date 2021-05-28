import re
import sys
import random
import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from blanks_globals import stop_words, basic_wikipedia_search_url
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

text = text.replace('\n', '')
text = re.sub(r'\[\d+\]', '', text)  # remove wikipedia references
sentences = []
start = 0

for i in range(len(text)):  # break text into sentences
    if text[i] in "?!":
        if i + 1 >= len(text) or text[i + 1] not in "\"\'":
            end = i + 1
        else:
            end = i + 2
        sentences.append(text[start:end])
        start = end + 1
    if text[i] == ".":
        if i + 2 > len(text):
            end = i + 1
            sentences.append(text[start:end])
            start = end
        elif text[i + 1] in "\"\'":
            end = i + 2
            sentences.append(text[start:end])
            start = end + 1
        elif text[i + 1] == " " and (text[i + 2].isupper() or
                                     text[i + 2].isdigit()):
            end = i + 1
            sentences.append(text[start:end])
            start = end + 1

pair_set = set()
categories = ["JJ", "JJR", "JJS", "NN", "NNS", "NNP", "RB",
              "RBR", "RBS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

for sentence in sentences:
    pairs = nltk.pos_tag(nltk.word_tokenize(sentence))
    for pair in pairs:
        if pair[0] not in stop_words and pair[1] in categories:
            pair_set.add(pair)


words_to_be_replaced = random.sample(list(pair_set), 10)

category_map = {
    "NNP": "name",
    "NN": "singular noun",
    "NNS": "plural noun",
    "VB": "simple verb",
    "VBD": "past tense",
    "VBG": "-ing verb",
    "VBN": "past participle verb",
    "VBP": "simple verb",
    "VBZ": "-s verb",
    "JJ": "adjective",
    "JJR": "comparative adjective",
    "JJS": "superlative adjective",
    "RB": "adverb",
    "RBR": "comparative adverb",
    "RBS": "superlative adverb"
}

print("You are going to replace 10 words in total: ")
for word, category in words_to_be_replaced:
    replace_word = input(f"Enter a(an) {category_map[category]}: ").lower()
    text = text.replace(word, replace_word)
    text = text.replace(word.capitalize(), replace_word.capitalize())
print("------------------------------------------")
print(f"Text after replacement: \n{text}")
