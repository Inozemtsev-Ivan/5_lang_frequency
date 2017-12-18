import sys
import string

DELIMITERS = set(''.join([string.punctuation, string.whitespace]))


def load_data(filepath):
    with open(filepath, 'r') as file_descriptor:
        for word in next_word(file_descriptor):
            yield word


def next_word(file_descriptor):
    new_word = ''
    while True:
        new_symbol = file_descriptor.read(1)
        if len(new_symbol) > 0:
            if new_symbol not in DELIMITERS:
                new_word += new_symbol
            elif len(new_word) > 0:
                result, new_word = new_word, ''
                yield result
        else:
            raise StopIteration


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
