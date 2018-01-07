# Frequency Analysis of Words

This is a pretty simple Python script for word frequency analysis in plain text files. Script removes punctuation from text, lowercases words and print ten most frequent words (in sorted way).

Script has extremely simple command-line user interface: `python3 lang_frequency.py <filename>`. Example of usage:
```shell
python3 lang_frequency.py README.md
1:   "of"  - 6 times
2:   "frequency"  - 5 times
3:   "script"  - 5 times
4:   "for"  - 5 times
5:   "words"  - 4 times
6:   "in"  - 4 times
7:   "text"  - 4 times
8:   "analysis"  - 3 times
9:   "is"  - 3 times
10:  "a"  - 3 times
```

Correct `filename` _must_ be referenced during execution, otherwise it will raise exceptions:
 ```shell
python3 lang_frequency.py
Please specify filepath!
```
_OR_

```shell
python3 lang_frequency.py filename.txt
[Errno 2] No such file or directory: 'filename.txt'
```

Script utilise some small optimisation to improve performance like usage of generators instead of plain lists. However, performance completely depends on optimization of corresponding CPython functions responsible for build-in text file I/O and string translations.   

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
