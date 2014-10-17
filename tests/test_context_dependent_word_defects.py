import unittest
import os
from nltk.corpus import brown
from python_basic_bigquery import easybigquery

from wordprediction.context_dependent_word_defects import get_defects
from wordprediction.corpus import generate_words
from wordprediction.project_input import get_bigrams


class GetDefects(unittest.TestCase):

    def test_get_defects(self):
        current_directory = os.path.dirname(__file__)
        text_directory = 'usertexts'
        usertext = os.path.join(current_directory, text_directory, 'one.txt')
        corpus_one = os.path.join(current_directory, 'corpus', 'one.txt')
        corpus_two = os.path.join(current_directory, 'corpus', 'two.txt')
        corpuses = [corpus_one, corpus_two]
        actual = get_defects(usertext, corpuses)
        expected = [
            (b's', b'whatever'),
            (b'whatever', b'ever'),
        ]
        self.assertEqual(expected, actual)

    def test_get_defects_project(self):
        current_directory = os.path.dirname(__file__)
        text_directory = 'usertexts'
        usertext_filename = 'project.txt'
        usertext = os.path.join(current_directory, text_directory, usertext_filename)
        corpuses = os.path.join(current_directory, text_directory, usertext_filename)
        actual = get_defects(usertext, corpuses)
        expected = []
        self.assertEqual(expected, actual)

    def test_hoho(self):
        bigrams = []
        current_directory = os.path.dirname(__file__)
        bigram_source = os.path.join(current_directory, 'corpus', 'count_2w.txt')
        with open(bigram_source, 'r') as f:
            for line in f:
                words = line.split()
                bigrams.append((words[0], words[1]))
        usertext = os.path.join(current_directory, 'usertexts', 'project.txt')
        usertext_words = generate_words(usertext)
        user_bigrams = get_bigrams(usertext_words)
        defects = []
        for bigram in user_bigrams:
            if bigram not in bigrams:
                defects.append(bigram)
        self.assertEqual([], defects)

    def test_get_bigrams(self):
        self.maxDiff = None
        defects = []
        masta_bigrams = get_master_bigrams()
        for bigram in get_bigrams_from_usertext():
            if bigram not in masta_bigrams:
                defects.append(bigram)
        self.assertEqual([], defects)

    def test_size_bigrams(self):
        self.assertEqual(1, len(list(get_bigrams_from_usertext())))

    def test_google_bigquery(self):


def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])


def get_bigrams_from_usertext():
    current_directory = os.path.dirname(__file__)
    text = os.path.join(current_directory, 'usertexts', 'project.txt')
    words = []
    with open(text, 'r') as f:
        for line in f:
            w = [word.lower().replace(',', '').replace('.', '') for word in line.split()]
            words.extend(w)
    return find_ngrams(words, 2)

def get_master_bigrams():
    bigrams = []
    current_directory = os.path.dirname(__file__)
    bigram_source = os.path.join(current_directory, 'corpus', 'count_2w.txt')
    with open(bigram_source, 'r') as f:
        for line in f:
            words = line.split()
            bigrams.append((words[0], words[1]))
    return bigrams
