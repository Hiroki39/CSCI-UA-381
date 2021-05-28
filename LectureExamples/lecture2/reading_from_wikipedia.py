import requests
import re
basic_wikipedia_search_url = "https://en.wikipedia.org/wiki/"
xml_pattern = re.compile(r'<([/!?]?)([a-z?\-]+)[^>]*>', re.I)


def replace_spaces_with_underscores(search_term):
    output = search_term.replace(' ', '_')
    return(output)


def non_match(entry):
    if re.search('<b>Wikipedia does not have an article with this exact name.</b>', entry, re.I):
        return(True)
    else:
        return(False)


def remove_xml(string):
    global xml_pattern
    output = xml_pattern.sub('', string)
    return(output)


def look_up_wikipedia_page_from_internet(search_term):
    global basic_wikipedia_search_url
    search_term = replace_spaces_with_underscores(search_term)
    url = basic_wikipedia_search_url + search_term
    response = requests.get(url).text
    return(response)


def print_paragraphs_from_wikipedia_entry(entry):
    paragraph_start = re.compile('<p[^>]*>')
    paragraph_end = re.compile('</p>')
    done = False
    start = 0
    while not done:
        next_paragraph_start = paragraph_start.search(entry, start)
        if next_paragraph_start:
            start = next_paragraph_start.end()
            next_paragraph_end = paragraph_end.search(entry, start)
            if next_paragraph_end:
                end = next_paragraph_end.start()
                text = remove_xml(entry[start:end])
                if re.search('[a-z]{3}', text):
                    print(text)
                start = next_paragraph_end.end()
            else:
                done = True
        else:
            done = True
    return(False)


def print_out_all_paragraphs_from_wikipedia_online(search_term):
    # using online wikipedia instead of shelved wikipedia
    full_page = look_up_wikipedia_page_from_internet(search_term)
    if non_match(full_page):
        return(False)
    print_paragraphs_from_wikipedia_entry(full_page)
