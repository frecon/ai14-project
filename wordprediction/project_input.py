import nltk
from nltk import bigrams
import sys
import inspect
import os

"""
project_input.py: Reads an input file, creates a corpus and ngrams.

"""

def get_ngrams(n, filename):
    words = input_text(filename)
    lowerWords = []
    for word in words:
        lowerWords.append(word.lower())
    ngrams = nltk.ngrams(lowerWords, n)
    return ngrams

def get_trigrams(words):
    """From a list of words, trigrams are constructed and returned"""
    lowerWords = []
    for word in words:
        lowerWords.append(word.lower())
    ngrams = nltk.ngrams(lowerWords, 3)
    return ngrams

def get_bigrams(words):
    """From a list of words, bigrams are constructed and returned"""
    lowerWords = []
    for word in words:
        lowerWords.append(word.lower())
    ngrams = bigrams(lowerWords)
    return ngrams

def get_words(filename):
    """Creates a corpus from a text file"""
    words = nltk.corpus.genesis.words(filename)
    return words


def input_text(filename):
    """Takes a file name from the user and creates a corpus from the text the file contains"""
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    filepath = path +"/"+ filename
    words = get_words(filepath)
    return words


def main():
    filename = sys.argv[-1]
    bigrams = get_ngrams(2, filename)
    for gram in bigrams:
        print (gram)


if __name__ == "__main__": main()