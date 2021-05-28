## morphology commands

def make_english_plural(string):
    if ((string[-1] in ['s','x','z']) or\
        (string[-2:] in ['ch','sh'])):
        return(string+'es')
    elif ((string[-1] == 'y') and \
          (not(string[-2] in ['a','e','i','o','u']))):
        return(string[:-1]+'ies')
    else:
        return(string+'s')

