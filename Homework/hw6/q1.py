from bs4 import BeautifulSoup

target_dir = '../../Datasets/brown_sgml/'
sgml_files = [
    "br-a01.sgml",
    "br-b01.sgml",
    "br-c01.sgml",
    "br-d01.sgml",
    "br-e01.sgml",
    "br-f01.sgml",
    "br-g01.sgml",
    "br-h01.sgml",
    "br-j01.sgml",
    "br-k01.sgml",
    "br-l01.sgml",
    "br-m01.sgml",
    "br-n01.sgml",
    "br-p01.sgml",
    "br-r01.sgml",
    "br-a11.sgml",
    "br-b11.sgml",
    "br-c11.sgml",
    "br-d11.sgml",
    "br-e11.sgml"
]
word_list = ['$', 'dollar', 'dollars', 'money', 'finance', 'fund', 'exchange',
             'savings', 'pension', 'budget']

open('finance.txt', 'w').close()
open('non_finance.txt', 'w').close()

for curr_file in sgml_files:
    with open(target_dir + curr_file) as f:
        soup = BeautifulSoup(f, 'lxml')
        text = soup.get_text().replace('\n', ' ').lower()

    count = 0
    for word in word_list:
        count += text.count(word)
        if count >= 5:
            curr_list = "finance.txt"
        else:
            curr_list = "non_finance.txt"

    with open(curr_list, "a") as f:
        f.write(curr_file + "\n")
