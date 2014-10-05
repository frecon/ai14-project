import nltk
from nltk import ngrams
from nltk import bigrams
from collections import Counter
import string

def get_most_common(word_list, search_word):
    ordered_bigrams = Counter()
    punct = set(string.punctuation)
    grams = [b.lower() for (a, b) in nltk.ngrams(word_list, 2) if a.lower() == search_word and b not in punct]
    #grams = [b.lower() for (a, b) in get_ngrams(word_list, 2) if a.lower() == search_word]
    #grams = [b.lower() for (a, b) in nltk.bigrams(word_list) if a == 'och']
    for gram in grams:
        ordered_bigrams[gram] += 1
    return ordered_bigrams.most_common(3)

# def get_ngrams(text, n):
#     punct = set(string.punctuation)
#     n_grams = []
#     for gram in ngrams(text, n):
#         if gram[1] not in punct:
#             n_grams.extend(gram)
#     return n_grams

def main():
    # with open("corpus_text.txt", "r") as file:
    #     word_list = file.read()
    # word_list = word_list.split()r
    word_list = nltk.corpus.gutenberg.words('austen-emma.txt')

    val = ''
    while (val!='e'):
        val = input('Type your word: ')
        ordered_bigrams = get_most_common(word_list, val.lower())
        if len(ordered_bigrams) == 0:
            print ('No matching words')
        else:
            #print (ordered_bigrams)
            for (word, nr) in ordered_bigrams:
                print (word + ' (' + str(nr) + ')')
        print ('\nType e to end the program')

if __name__ == "__main__": main()