# Frequency Analysis of Words

This is a pretty simple Python script for word frequency analysis in plain text files. Script removes punctuation from text, lowercases words and print ten most frequent words (in sorted way).

Script has a command-line user interface. Example of usage:
```shell
python3 lang_frequency.py README.md [enter]
of
frequency
script
for
words
in
text
analysis
is
a
```
Filename _must_ be referenced during execution, otherwise it will raise exception:
 ```shell
python3 lang_frequency.py
Please specify filepath!
```
Script utilise some small optimisation to improve performance like usage of generators instead of plain lists& However, performance completely depends on optimization of corresponding CPython functions responsible for build-in text file I/O and string translations.   

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
