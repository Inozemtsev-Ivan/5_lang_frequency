from string import punctuation
from collections import Counter
from argparse import ArgumentParser, FileType

TOP = 10


def load_data(infile):
    with infile as file:
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


def get_filename():
    parser = ArgumentParser(description='Counts words frequency in text file.')
    parser.add_argument('filename',
                        metavar='<filename>',
                        type=FileType('r'),
                        help="Name or path (absolute or relative) of file \
                        to process. One file at a time, please.")
    return parser.parse_args().filename


if __name__ == '__main__':
    infile = get_filename()
    string_generator = load_data(infile)
    words = get_words(string_generator)
    most_frequent_words = get_most_frequent_words(words, TOP)
    prettify_output(most_frequent_words)
