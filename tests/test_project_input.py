import unittest

import nltk

from wordprediction.project_input import (
    get_trigrams,
    get_bigrams,
    get_words,
    input_text
)

def test_ngrams(self):
        text = "I like AI. I like AI. It's."
        actual = get_ngrams(3, 'corpus_text.txt')
        expected = [
            ('i', 'like', 'ai'),
            ('like', 'ai', '.'),
            ('ai','.', 'i'),
            ('.','i', 'like'),
            ('i','like','ai'),
            ('like', 'ai', '.'),
            ('ai', '.','it'),
            ('.','it',"'s"),
            ('it',"'s",'.'),
        ]
        self.assertEqual(expected, list(actual))

class TestGrams(unittest.TestCase):
    def test_bigrams(self):
        text = "I like AI. It's the best course ever."
        actual = get_bigrams(text)
        expected = [
            ('i', 'like'),
            ('like', 'ai'),
            ('ai', '.'),
            ('.', 'it'),
            ('it', "'s"),
            ("'s", "the"),
            ('the', 'best'),
            ('best', 'course'),
            ('course', 'ever'),
            ('ever', '.'),
        ]
        self.assertEqual(expected, list(actual))

def test_trigrams(self):
        text = "I like AI. I like AI. It's."
        actual = get_trigrams(text)
        expected = [
            ('i', 'like', 'ai'),
            ('like', 'ai', '.'),
            ('ai','.', 'i'),
            ('.','i', 'like'),
            ('i','like','ai'),
            ('like', 'ai', '.'),
            ('ai', '.','it'),
            ('.','it',"'s"),
            ('it',"'s",'.'),
        ]
        self.assertEqual(expected, list(actual))