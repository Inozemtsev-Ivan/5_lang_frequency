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
usage: lang_frequency.py [-h] <filename>
lang_frequency.py: error: the following arguments are required: <filename>
```
_OR_

```shell
python3 lang_frequency.py example.txt
usage: lang_frequency.py [-h] <filename>
lang_frequency.py: error: argument <filename>: can't open 'example.txt': [Errno 2] No such file or directory: 'example.txt'
```

This script supports `--help` and `-h` arguments as shown:
```shell
python3 lang_frequency.py --help
usage: lang_frequency.py [-h] <filename>

Counts words frequency in text file.

positional arguments:
  <filename>  Name or path (absolute or relative) of file to process. One file
              at a time, please.

optional arguments:
  -h, --help  show this help message and exit
```

Script utilise some small optimisation to improve performance like usage of generators instead of plain lists. However, performance completely depends on optimization of corresponding CPython functions responsible for build-in text file I/O and string translations.   

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
