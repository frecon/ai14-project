import unittest
import nltk

from wordprediction.nextword_sandras import (
    get_most_common
)


class TestGrams(unittest.TestCase):
    def test_eget_most_common(self):
        text = "I like AI. I like AI. It's the best course I have ever had."
        actual = get_most_common(text.split(), 'I')
        expected = [
            ('like', 2),
            ('have', 1)
        ]
        self.assertEqual(expected, list(actual))