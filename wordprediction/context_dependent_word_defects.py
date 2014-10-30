from decimal import Decimal, ROUND_DOWN
import os

from nltk import bigrams

from wordprediction.corpus import Corpus, generate_words


def get_defects_in_correct_sentences():
    current_directory = os.path.abspath(os.getcwd())
    directory = 'usertexts'
    filename = 'correct_sentences.txt'
    usertext = os.path.join(current_directory, directory, filename)
    corpus = Corpus()
    print(' & '.join(
        ['Hitrate',
         'Sentence',
         'Count',
         'Defects found \\\\']
    ))
    print('\\hline')
    with open(usertext, 'r') as f:
        total_correct = 0
        total_incorrect = 0
        for line in f:
            words = line.split()
            bigrams = list(get_bigrams(words))
            nr_of_bigrams = len(bigrams)
            defects = []
            for bigram in bigrams:
                if not corpus.bigram_exists(bigram):
                    defects.append(bigram)
            incorrect = len(defects)
            correct = nr_of_bigrams - incorrect
            not_detected = 0
            total_incorrect += incorrect
            total_correct += correct
            print('{0} & {1} & {2} & {3} \\\\'.format(
                str(get_z(correct, not_detected, incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
                line.strip(),
                len(defects),
                '' if len(defects) == 0 else defects,
                ))
        total_not_detected = 0
        print('\\hline')
        print('{0} & hitrate'.format(
            str(get_z(total_correct, total_not_detected, total_incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
        ))


def get_result_for_sentences():
    current_directory = os.path.abspath(os.getcwd())
    directory = 'usertexts'
    filename = 'sentences.txt'
    usertext = os.path.join(current_directory, directory, filename)
    corpus = Corpus()
    print('#'.join(
        ['Hitrate',
        'Correct',
        'Not detected',
        'Incorrect',
        'Wrong word',
        'Incorrect sentence',
        'Correct sentence',
        'Correct defects',
        'Nr defects found',
        'Defects found',
        'Nr bigrams',
        'Bigrams']
    ))
    with open(usertext, 'r') as f:
        total_correct = 0
        total_not_detected = 0
        total_incorrect = 0
        for line in f:
            if len(line) == 0:
                continue
            false_word, incorrect_sentence, correct_sentence = line.split(';')
            bigrams = list(get_bigrams(incorrect_sentence.split())) + list(get_bigrams(correct_sentence.split()))
            found_defects = []
            for bigram in bigrams:
                if not corpus.bigram_exists(bigram):
                    found_defects.append(bigram)
            correct_defects = get_correct_defects(bigrams, false_word)
            correct, not_detected, incorrect = get_hitrate_for_bigrams(correct_defects, found_defects)
            total_correct += correct
            total_incorrect += incorrect
            total_not_detected += not_detected
            print('{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}#{8}#{9}#{10}#{11}'.format(
                str(get_z(correct, not_detected, incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
                correct,
                not_detected,
                incorrect,
                false_word,
                incorrect_sentence.strip(),
                correct_sentence.strip(),
                correct_defects,
                len(found_defects),
                found_defects,
                len(bigrams),
                bigrams,
            ))
        print('{0}#{1}#{2}#{3}'.format(
            str(get_z(total_correct, total_not_detected, total_incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
            total_correct,
            total_not_detected,
            total_incorrect,
        ))


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


def get_defects_in_false_friends():
    current_directory = os.path.abspath(os.getcwd())
    directory = 'usertexts'
    filename = 'false_friends.txt'
    usertext = os.path.join(current_directory, directory, filename)
    corpus = Corpus()
    print(' & '.join(
        ['Hitrate',
         'Wrong word',
         'Sentence',
         'Nr defects found',
         'Defects found \\\\']
    ))
    print('\\hline')
    with open(usertext, 'r') as f:
        total_correct = 0
        total_not_detected = 0
        total_incorrect = 0
        for line in f:
            if len(line) == 0:
                continue
            false_word, sentence = line.split(';')
            words = sentence.split()
            found_defects = []
            for bigram in get_bigrams(words):
                if not corpus.bigram_exists(bigram):
                    found_defects.append(bigram)
            correct_defects = get_correct_defects(get_bigrams(words), false_word)
            correct, not_detected, incorrect = get_hitrate_for_bigrams(correct_defects, found_defects)
            total_correct += correct
            total_incorrect += incorrect
            total_not_detected += not_detected
            print('{0} & {1} & {2} & {3} & {4} \\\\'.format(
                str(get_z(correct, not_detected, incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
                false_word,
                sentence.strip(),
                len(found_defects),
                '' if len(found_defects) == 0 else found_defects,
            ))
        print('\\hline')
        print('{0} & hitrate'.format(
            str(get_z(total_correct, total_not_detected, total_incorrect).quantize(Decimal('.001'), rounding=ROUND_DOWN)).replace('.', ','),
        ))

def get_bigrams(words):
    """From a list of words, bigrams are constructed and returned"""
    return bigrams([word.lower() for word in words])

if __name__ == '__main__':
    #  get_result_for_sentences()
    #  get_defects_in_false_friends()
    get_defects_in_correct_sentences()
