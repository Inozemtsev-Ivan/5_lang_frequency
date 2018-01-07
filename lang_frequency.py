import sys
from string import punctuation
from collections import Counter

TOP = 10


def load_data(filepath):
    with open(filepath, 'r') as file:
        for text_string in file:
            yield text_string


def get_words(string_generator):
    replace_delimiters_by_space = str.maketrans(
        dict.fromkeys(punctuation, ' '))
    for text_string in string_generator:
        for word in text_string.translate(replace_delimiters_by_space).split():
            if not word.islower():
                word = word.lower()
            yield word


def get_most_frequent_words(word_generator, top):
    return Counter(word_generator).most_common(top)


def prettify_output(sorted_data, begin_from_zero=False, indentation=2):
    starting_number = 0 if begin_from_zero else 1
    for number, value in enumerate(sorted_data, starting_number):
        print(''.join(['{num}:',
                       ' ' * (indentation + len(str(TOP)) - len(str(number))),
                       '"{word}" ',
                       ' - {occurrence} times'])
              .format(num=number,
                      word=value[0],
                      occurrence=value[1]))


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        string_generator = load_data(filepath)
        most_frequent_words = get_most_frequent_words(get_words(string_generator), TOP)
        prettify_output(most_frequent_words)
    except IndexError:
        exit('Please specify filepath!')
    except IOError as ex:
        exit(ex)
