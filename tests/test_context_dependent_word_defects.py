import unittest
import os

from wordprediction.context_dependent_word_defects import (
    get_defects,
    get_defects_in_correct_sentences,
    get_bigrams,
)


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

    def test_get_defects_in_correct_sentences(self):
        actual = get_defects_in_correct_sentences()
        self.assertEqual([], actual)

class TestGrams(unittest.TestCase):
    def test_bigrams(self):
        text = "I like AI. It's the best course ever."
        actual = get_bigrams(text.split())
        expected = [
            ('i', 'like'),
            ('like', 'ai.'),
            ('ai.', "it's"),
            ("it's", "the"),
            ('the', 'best'),
            ('best', 'course'),
            ('course', 'ever.'),
        ]
        self.assertEqual(expected, list(actual))

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
