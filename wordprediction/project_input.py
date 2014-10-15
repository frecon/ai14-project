import nltk
from nltk import bigrams
import sys
import inspect
import os

"""
project_input.py: Reads an input file, creates a corpus and ngrams.

"""

def get_trigrams(words):
    """From a list of words, trigrams are constructed and returned"""
    lowerWords = []
    for word in words:
        lowerWords.append(word.lower())
    ngrams = nltk.ngrams(lowerWords, 3)
    return ngrams

def get_bigrams(words):
    """From a list of words, bigrams are constructed and returned"""
    return bigrams(words)


def get_words(filename):
    """Creates a corpus from a text file"""
    words = nltk.corpus.genesis.words(filename)
    return words


def input_text():
    """Takes a file name from the user and creates a corpus from the text the file contains"""
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    filename = sys.argv[-1]
    filepath = path +"/"+ filename
    words = get_words(filepath)
    return words


def main():
    words = input_text()
    bigrams = get_bigrams(words)
    for gram in bigrams:
        print (gram)


if __name__ == "__main__": main()