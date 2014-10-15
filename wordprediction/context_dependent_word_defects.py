import os

from wordprediction.project_input import get_bigrams
from wordprediction.corpus import Corpus, generate_words

def get_defects(usertext_filename, corpuses):
    """Return a list of bigrams that doesn't exist in the corpuses."""
    usertext_words = generate_words(usertext_filename)
    bigrams = get_bigrams(usertext_words)
    corpus = Corpus(corpuses)
    defects = []
    for bigram in bigrams:
        if not corpus.bigram_score(bigram):
            defects.append(bigram)
    return defects
