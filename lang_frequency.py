import sys
import string

REPLACE_DELIMITERS_BY_SPACE = str.maketrans(dict.fromkeys(string.punctuation, ' '))


def load_data(filepath):
    with open(filepath, 'r') as file:
        for string in file:
            for word in string.translate(REPLACE_DELIMITERS_BY_SPACE).split():
                yield word


def get_most_frequent_words(words_generator, top_amount):
    words_rating = {}
    for word in words_generator:
        words_rating[word] = words_rating.setdefault(word, 0) + 1
    return sorted(words_rating, key=words_rating.get, reverse=True)[:top_amount]


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        exit('Please specify filepath!')
    try:
        for word in get_most_frequent_words(load_data(filepath), 10):
            print(word)
    except IOError as ex:
        print(ex)
