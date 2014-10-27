import os

import nltk
from nltk.collocations import (
    BigramCollocationFinder,
    BigramAssocMeasures,
)
from nltk.corpus import brown


class Corpus(object):
    def __init__(self, files=None):
        self._bigrams = []
        if not files:
            files = ['english-web.txt']
            self.words = generate_words(files)
            self.words = [word.lower() for word in self.words]
            self.words.extend([word.lower() for word in brown.words()])
            current_directory = os.path.dirname(__file__)
            bigram_source = os.path.join(current_directory, 'corpus', 'count_2w.txt')
            self._bigrams = get_bigrams(bigram_source)
        else:
            self.words = generate_words(files)
            self.words = [word.lower() for word in self.words]
        self.finder = BigramCollocationFinder.from_words(self.words)

    def bigram_exists(self, bigram):
        bigram = tuple(word.lower() for word in bigram)
        if bigram in self._bigrams or self.bigram_score(bigram):
            return True
        return False

    def bigram_score(self, bigram):
        word1, word2 = tuple(word.lower() for word in bigram)
        return self.finder.score_ngram(
            BigramAssocMeasures.raw_freq,
            word1,
            word2)


def generate_words(files):
    return nltk.corpus.genesis.words(files)


def get_bigrams(bigram_source):
    bigrams = []
    with open(bigram_source, 'r') as f:
        for line in f:
            words = line.split()
            word1 = words[0]
            word2 = words[1]
            bigrams.append((word1, word2))
    return bigrams
