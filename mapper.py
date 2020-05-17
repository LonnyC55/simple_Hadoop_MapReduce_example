#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words
import string

# get all lines from stdin
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # remove punctuation from the current line of text
    line = line.translate(None, string.punctuation)

    # change all uppercase characters to lowercase characters
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # assign the sklearn stop_words set to stops variable
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    # output tuples (word, 1) in tab-delimited format and ignore stop words
    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
