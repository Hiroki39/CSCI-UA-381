import pandas as pd


# it is not possible to tell stress is on the final syllable of a verb that
# ends in vowel + consonant, so I just doubled the last character if the verb
# ends in vowel + consonant

def make_past(word):
    if word[-1] == 'e':
        return word + 'd'
    elif word[-1] == 'y' and word[-2] not in ['a', 'e', 'i', 'o', 'u']:
        return word[:-1] + 'ied'
    elif word[-1] not in ['a', 'e', 'i', 'o', 'u', 'w', 'x', 'y'] and \
            word[-2] in ['a', 'e', 'i', 'o', 'u']:
        return word + word[-1] + 'ed'
    else:
        return word + 'ed'


def make_present_participle(word):
    if word[-1] == 'e':
        return word[:-1] + 'ing'
    elif word[-1] not in ['a', 'e', 'i', 'o', 'u', 'w', 'x', 'y'] and \
            word[-2] in ['a', 'e', 'i', 'o', 'u']:
        return word + word[-1] + 'ing'
    else:
        return word + 'ing'


df = pd.read_csv("verb_irreg.tsv", delimiter="\t")

df.loc[df['PAST'].isnull(), 'PAST'] = df['WORD'].apply(make_past)
df.loc[df['PAST-PARTICIPLE'].isnull(), 'PAST-PARTICIPLE'] = df['WORD'].apply(make_past)
df.loc[df['PRESENT-PARTICIPLE'].isnull(),
       'PRESENT-PARTICIPLE'] = df['WORD'].apply(make_present_participle)

df.to_csv("verb_irreg_filled.tsv", sep="\t")
