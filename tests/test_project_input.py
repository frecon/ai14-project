import unittest

import nltk

from wordprediction.project_input import (
    get_trigrams,
    get_bigrams,
    get_words,
    input_text
)


class TestGrams(unittest.TestCase):
    def test_bigrams(self):
        text = "I like AI. I like AI. It's the best course ever."
        actual = get_bigrams(text)
        expected = [
            ('I', 'like'),
            ('like', 'ai'),
            ('ai', '.'),
            ('I', 'like'),
            ('like', 'ai'),
            ('it', "'s"),
            ("'s", 'the'),
            ('the', 'best'),
            ('best', 'course'),
            ('course', 'ever'),
        ]
        self.assertEqual(expected, list(actual))

def test_trigrams(self):
        text = "I like AI. I like AI. It's"
        actual = get_trigrams(text)
        expected = [
            ('i', 'like', 'ai'),
            ('like', 'ai', '.'),
            ('ai','.', 'i'),
            ('.','i', 'like'),
            ('i','like','ai'),
            ('like', 'ai', '.'),
            ('ai', '.','it'),
            ('.','it','\''),
            ('it','\'','s'),

        ]
        self.assertEqual(expected, list(actual))