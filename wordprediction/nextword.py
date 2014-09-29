from nltk.util import bigrams
from nltk import word_tokenize
import nltk.data
from nltk.probability import ConditionalFreqDist
from nltk.collocations import (
    BigramAssocMeasures,
    BigramCollocationFinder,
)


def bi_grams(text):
    ngram = []
    for sentence in sentences(text):
        words = [word.lower()
                 for word in word_tokenize(sentence)
                 if word != '.']
        grams = bigrams(words)
        ngram.extend(grams)
    return ngram


def top_ten_bigrams(words):
    bigram_measures = BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(words)
    finder.apply_freq_filter(3)
    return finder.nbest(bigram_measures.pmi, 10)


def frequency_distribution(text):
    cfdist = ConditionalFreqDist()
    for sentence in sentences(text):
        for word in word_tokenize(sentence):
            if len(word) > 1:
                cfdist[len(word)][word] += 1
    return cfdist


def sentences(text):
    sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    return sentence_detector.tokenize(text.strip())
