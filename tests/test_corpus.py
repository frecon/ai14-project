import os
import unittest

from wordprediction.corpus import (
    generate_words,
    Corpus,
    get_bigrams,
)


class TestCorpus(unittest.TestCase):
    def setUp(self):
        current_directory = os.path.dirname(__file__)
        self.corpus_one = os.path.join(current_directory, 'corpus', 'one.txt')
        self.corpus_two = os.path.join(current_directory, 'corpus', 'two.txt')
        self.corpus = Corpus()

    def test_bigram_score(self):
        bigram = (b'I', b'like')
        corpus = Corpus(self.corpus_one)
        actual = corpus.bigram_score(bigram)
        self.assertEqual(0.14285714285714285, actual)

    def test_bigram_score_for_nonexisting_bigram(self):
        bigram = (b'Maja', b'like')
        corpus = Corpus(self.corpus_one)
        actual = corpus.bigram_score(bigram)
        self.assertEqual(None, actual)

    def test_bigram_score_multiple_corpus(self):
        bigram = (b'I', b'like')
        files = [self.corpus_one, self.corpus_two]
        corpus = Corpus(files)
        actual = corpus.bigram_score(bigram)
        self.assertEqual(0.06666666666666667, actual)

    def test_generate_words_from_one_corpus(self):
        expected = [
            b'I',
            b'like',
            b'AI',
            b'.',
            b'It',
            b"'",
            b's',
            b'the',
            b'ever',
            b'.',
            b'I',
            b'like',
            b'AI',
            b'.',
        ]
        actual = generate_words(self.corpus_one)
        self.assertEqual(expected, list(actual))

    def test_generate_words_from_multiple_corpus(self):
        expected = [
            b'I',
            b'like',
            b'AI',
            b'.',
            b'It',
            b"'",
            b's',
            b'the',
            b'ever',
            b'.',
            b'I',
            b'like',
            b'AI',
            b'.',
            b'Duckhunt',
            b'is',
            b'the',
            b'best',
            b'assignment',
            b'.',
            b'I',
            b'really',
            b'enjoy',
            b'shooting',
            b'ducks',
            b'.',
            b'Especially',
            b'with',
            b'hmm',
            b'.'
        ]
        files = [self.corpus_one, self.corpus_two]
        actual = generate_words(files)
        self.assertEqual(expected, list(actual))

    def test_get_bigrams(self):
        current_directory = os.path.dirname(__file__)
        bigram_source = os.path.join(
            current_directory,
            'corpus',
            'count_2w_subset.txt')
        bigrams = get_bigrams(bigram_source)
        expected = [
            ('crib', 'bedding'),
            ('cried', 'and'),
            ('cried', 'for'),
        ]
        self.assertEqual(expected, bigrams)

    def test_bigram_exits(self):
        bigram = ('crib', 'bedding')
        self.assertEqual(True, self.corpus.bigram_exists(bigram))

    def test_bigram_exits_nonexisting_bigram(self):
        bigram = ('maja', 'frej')
        self.assertEqual(False, self.corpus.bigram_exists(bigram))

    def test_bigram_exists_multiple_corpus(self):
        corpus = Corpus(self.corpus_one)
        bigram = (b'like', b'ai')
        actual = corpus.bigram_exists(bigram)
        self.assertEqual(True, actual)

    def test_bigram_exists_multiple_corpus_hela_skiten(self):
        #  Daniel/np personally/rb led/vbd the/at fight/nn for/in the/at measure/
        bigram = (b'personally', b'led')
        actual = self.corpus.bigram_exists(bigram)
        self.assertEqual(True, actual)
