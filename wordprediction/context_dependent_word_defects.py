from decimal import Decimal
import os

from wordprediction.project_input import get_bigrams
from wordprediction.corpus import Corpus, generate_words


def get_defects_in_correct_sentences():
    current_directory = os.path.abspath(os.getcwd())
    directory = 'usertexts'
    filename = 'correct_sentences.txt'
    usertext = os.path.join(current_directory, directory, filename)
    corpus = Corpus()
    with open(usertext, 'r') as f:
        total_correct = 0
        total_incorrect = 0
        for line in f:
            print(line.strip())
            words = line.split()
            bigrams = list(get_bigrams(words))
            nr_of_bigrams = len(bigrams)
            print('Found {0} bigrams {1}'.format(nr_of_bigrams, bigrams))
            bigrams = get_bigrams(words)
            defects = []
            for bigram in bigrams:
                if not corpus.bigram_exists(bigram):
                    defects.append(bigram)
            incorrect = len(defects)
            correct = nr_of_bigrams - incorrect
            total_incorrect += incorrect
            total_correct += correct
            print('Found {0} defects {1}'.format(incorrect, defects))
            print('z = {0}'.format(get_z(correct, 0, incorrect)))
            print('')
        print('tot z = {0}'.format(get_z(total_correct, 0, total_incorrect)))


def get_defects_in_false_friends():
    current_directory = os.path.abspath(os.getcwd())
    directory = 'usertexts'
    filename = 'false_friends.txt'
    usertext = os.path.join(current_directory, directory, filename)
    corpus = Corpus()
    with open(usertext, 'r') as f:
        total_correct = 0
        total_not_detected = 0
        total_incorrect = 0
        for line in f:
            if len(line) == 0:
                continue
            false_word, sentence = line.split(';')
            words = sentence.split()
            print(sentence.strip())
            print("wrong word = {0}".format(false_word))
            print('Found {0} bigrams {1}'.format(len(list(get_bigrams(words))), list(get_bigrams(words))))
            found_defects = []
            for bigram in get_bigrams(words):
                if not corpus.bigram_exists(bigram):
                    found_defects.append(bigram)
            correct_defects = get_correct_defects(get_bigrams(words), false_word)
            correct, not_detected, incorrect = get_hitrate_for_bigrams(correct_defects, found_defects)
            print('z = {0}'.format(get_z(correct, not_detected, incorrect)))
            total_correct += correct
            total_incorrect += incorrect
            total_not_detected += not_detected
            print('Found {0} defects {1}'.format(len(found_defects), found_defects))
            print('Correct defects {0} defects {1}'.format(len(correct_defects), correct_defects))
            print('')
        print(get_z(total_correct, total_incorrect, total_not_detected))


def get_correct_defects(bigrams, false_word):
    result = []
    for bigram in bigrams:
        if false_word in bigram:
            result.append(bigram)
    return result

def get_hitrate_for_bigrams(correct_defects, found_defects):
    found = False
    incorrect = 0
    for bigram in found_defects:
        if bigram in correct_defects:
            found = True
        else:
            incorrect += 1
    if found:
        correct = 1
        not_detected = 0
    else:
        correct = 0
        not_detected = 1
    return (correct, not_detected, incorrect)


def get_z(correct, not_detected, incorrect):
    print('correct {0}'.format(correct))
    print('not detected {0}'.format(not_detected))
    print('incorrect {0}'.format(incorrect))
    if (correct + not_detected + incorrect) == 0:
        return 0
    return Decimal(correct) / (Decimal(correct) + Decimal(not_detected) + Decimal(incorrect))


def get_defects(usertext_filename, corpuses=None):
    """Return a list of bigrams that doesn't exist in the corpuses."""
    usertext_words = generate_words(usertext_filename)
    bigrams = get_bigrams(usertext_words)
    print('Found {0} bigrams in {1}'.format(len(list(get_bigrams(usertext_words))), usertext_filename))
    corpus = Corpus(corpuses)
    defects = []
    for bigram in bigrams:
        if not corpus.bigram_exists(bigram):
            defects.append(bigram)
    return defects


if __name__ == '__main__':
    # print('Searching for defects from false friends.')
    # get_defects_in_false_friends()
    print('Searching for defects from correct sentences.')
    get_defects_in_correct_sentences()
