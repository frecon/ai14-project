import unittest

import nltk

from wordprediction.nextword import (
    bi_grams,
    top_ten_bigrams,
    frequency_distribution,
    sentences
)


class TestGrams(unittest.TestCase):
    def test_grams(self):
        text = "I like AI. I like AI. It's the best course ever."
        actual = bi_grams(text)
        expected = [
            ('i', 'like'),
            ('like', 'ai'),
            ('i', 'like'),
            ('like', 'ai'),
            ('it', "'s"),
            ("'s", 'the'),
            ('the', 'best'),
            ('best', 'course'),
            ('course', 'ever'),
        ]
        self.assertEqual(expected, list(actual))

    def test_top_ten_bigrams(self):
        expected = [
            ('Beer', 'Lahai'),
            ('Lahai', 'Roi'),
            ('gray', 'hairs'),
            ('Most', 'High'),
            ('ewe', 'lambs'),
            ('many', 'colors'),
            ('burnt', 'offering'),
            ('Paddan', 'Aram'),
            ('east', 'wind'),
            ('living', 'creature'),
        ]
        words = nltk.corpus.genesis.words('english-web.txt')
        self.assertEqual(expected, top_ten_bigrams(words))

    def test_frequency_distribution(self):
        text = "I like AI. I like AI. It's the best course ever."
        freq_distribution = frequency_distribution(text)
        expected = {
            2: {
                'AI': 2,
                'It': 1,
                "'s": 1,
            },
            3: {
                'the': 1,
            },
            4: {
                'like': 2,
                'best': 1,
                'ever': 1,
            },
            5: {
               # should be empty
            },
            6: {
                'course': 1,
            },
        }
        self.assertEqual(expected[2], freq_distribution[2])
        self.assertEqual(expected[3], freq_distribution[3])
        self.assertEqual(expected[4], freq_distribution[4])
        self.assertEqual(expected[5], freq_distribution[5])

    def test_sentences(self):
        text = "I like AI. I like AI. It's the best course ever."
        expected = [
            "I like AI.",
            "I like AI.",
            "It's the best course ever."
        ]
        self.assertEqual(expected, sentences(text))
