import re

with open("all-OANC.txt") as f:
    text = f.read().strip('\n')

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                'eighty', 'ninety', 'hundred', 'thousand', 'million',
                'billion', 'trillion']

number_match = "(?:[0-9]+(?:,(?:[0-9]{3}))*)(?:\.[0-9]+)?"
all_nbr_words = "|".join(number_words) + "|" + number_match
final_pattern = "(?:" + all_nbr_words + \
    ")(?: (?:" + "|".join(number_words) + "))*"

with open('match.txt', 'w') as f:
    f.write("\n".join(re.findall(one_or_more_nbr_words, text)))
