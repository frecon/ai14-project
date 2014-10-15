import unittest
import os

from wordprediction.context_dependent_word_defects import get_defects

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