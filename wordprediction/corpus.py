import nltk
from nltk.collocations import (
    BigramCollocationFinder,
    BigramAssocMeasures,
)


class Corpus(object):
    def __init__(self, files):
        self.words = generate_words(files)
        self.finder = BigramCollocationFinder.from_words(self.words)


    def bigram_score(self, bigram):
        word1, word2 = bigram
        return self.finder.score_ngram(
            BigramAssocMeasures.raw_freq,
            word1,
            word2)


def generate_words(files):
    return nltk.corpus.genesis.words(files)
