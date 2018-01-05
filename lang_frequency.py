import sys
from string import punctuation

REPLACE_DELIMITERS_BY_SPACE = str.maketrans(dict.fromkeys(punctuation, ' '))
TOP_FREQUENCY = 10


def load_data(filepath):
    with open(filepath, 'r') as file:
        for text_string in file:
            yield text_string


def get_most_frequent_words(string_generator, top_amount):
    words_rating = {}
    for text_string in string_generator:
        for word in text_string.translate(REPLACE_DELIMITERS_BY_SPACE).split():
            words_rating[word.lower()] = words_rating.setdefault(word, 0) + 1
    return sorted(words_rating, key=words_rating.get, reverse=True)[:top_amount]


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        exit('Please specify filepath!')
    try:
        for word in get_most_frequent_words(load_data(filepath), TOP_FREQUENCY):
            print(word)
    except IOError as ex:
        print(ex)
