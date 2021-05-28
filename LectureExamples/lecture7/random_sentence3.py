import random
import math
import re
from words3 import *

rules = [['S',['NP','VP']],\
         ['NP',['DetP','ADJ_SEQ','NOUN_SEQ'],['DetP','NOUN_SEQ'],
          ['ADJ_SEQ','plural_noun'],['proper_noun'],['plural_noun']],\
         ['DetP',['NP','pos'],['determiner']],\
         ['pos',["'s"]],\
         ['PP',['preposition','NP']],\
         ['NOUN_SEQ',['plural_noun'],['singular_noun']],\
         ['ADJ_SEQ',['adjective','ADJ_SEQ'],['adjective'],['adjective']],\
         ## fudge to make multiple adj less likely
         ['VP',['verb'],['verb','NP'],['verb','NP','PP'],['adverb','verb'],\
          ['adverb','verb','NP'],['adverb','verb','NP','PP']]]

##longer_rule_set = [['S',['NP','VP']],\
##         ['NP',['DetP','ADJ_SEQ','NOUN_SEQ'],['DetP','NOUN_SEQ'],['NP','PP'],\
##          ['ADJ_SEQ','plural_noun'],['proper_noun'],['plural_noun']],\
##         ['DetP',['NP','pos'],['determiner']],\
##         ['pos',["'s"]],\
##         ['PP',['preposition','NP']],\
##         ['NOUN_SEQ',['plural_noun'],['Sing_seq'],['Sing_seq','plural_noun']],\
##         ['ADJ_SEQ',['adjective','ADJ_SEQ'],['adjective']],\
##         ['Sing_seq',['Sing_seq','singular_noun'],['singular_noun']],\
##         ['VP',['verb'],['verb','NP'],['verb','NP','PP'],['adverb','verb'],\
##          ['adverb','verb','NP'],['adverb','verb','NP','PP']]]

rule_look_up_table = {}

def fill_table():
    rule_look_up_table['singular_noun'] = nouns
    rule_look_up_table['plural_noun'] = plural_nouns
    rule_look_up_table['proper_noun'] = proper_nouns
    rule_look_up_table['verb'] = verbs
    rule_look_up_table['adjective'] = adjectives
    rule_look_up_table['adverb'] = adverbs
    rule_look_up_table['determiner'] = dets
    rule_look_up_table['preposition'] = preps
    for item in rules:
        first = item[0]
        rest = item[1:]
        rule_look_up_table[first]=rest

fill_table()
    
def choose_symbol_expansion (nonterm_symbol):
    if nonterm_symbol in rule_look_up_table:
        choices = rule_look_up_table[nonterm_symbol]
        choice = random.choice(choices)
        return(choice)
    else:
        return(False)

def generate_random_phrase(symbol,maximum=1000,full_trace=True):
    done = False
    iterations = 0
    stack = [symbol]
    result = []
    while ((len(stack)>0) and (iterations < maximum)):
        next = stack.pop()
        lookup = choose_symbol_expansion(next)
        if type(lookup) == list:
            ## print(lookup)
            if full_trace:
                print(next,'expands to:',lookup)
            lookup = lookup[:] 
            ## make copy of list before reversing
            ## -- due to ideosyncracy of the way python handles lists
            lookup.reverse()
            ## we reverse the order due to the way stacks work in python
            ## python pops stacks off the end 
            ## by reversing, we are simulating left to right processing
            stack.extend(lookup)
        elif lookup:
            if full_trace:
                print(next,'expands to:',lookup)
            ## string symbols are nonterminals -- next iteration is word
            stack.append(lookup)
        else:
            ## random_choice fails on strings
            result.append(next)
    return(result)

def print_list_of_words_in_sentence_style(word_list):
    print(word_list[0].title(),end='')
    for word in word_list[1:]:
        if word == "'s":
            print(word,end='')
        else:
            print(' '+word,end='')
    print('.')

def random_sentence(full_trace=False):
    output = generate_random_phrase('S',full_trace=full_trace)
    print_list_of_words_in_sentence_style(output)
    answer = input('Type "Yes" or "yes" or "Y" if you want another random sentence. Otherwise, type anything else: ')
    if answer.lower() in ['yes','y']:
        random_sentence(full_trace=full_trace)

    
