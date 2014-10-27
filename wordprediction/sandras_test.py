import nltk
from nltk.util import ngrams
from nltk.util import bigrams

## Sixgrams from sentence
#from nltk.book import text4

# sentence = text4
# #sentence = "Detaljhandelsföretag sjönk på Hongkongbörsen. Protesterna väntas slå mot detaljhandeln bland annat genom att turister från fastlands-Kina håller sig borta från Hong Kong under firandet av Kinas nationaldag och de omgivande helgdagarna, då protesterna väntas kulminera."
# n = 2
# #sixgrams = ngrams(sentence.split(), n)
# sixgrams = ngrams(text4, n)
# count = 0
# for grams in sixgrams:
#     count=count+1
#     print (grams)
# print (count)


## Load corpus
# from nltk.corpus import webtext
# txt = webtext.words('overheard.txt')
# print (len(txt))
# print (txt)

## Loading own corpus
# from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/usr/share/dict' [1]
# wordlists = PlaintextCorpusReader(corpus_root, '.*') [2]
# wordlists.fileids()
# wordlists.words('filename.txt')

## Bigrams
# from nltk.util import bigrams
# grams = list(bigrams(['more', 'is', 'said', 'than', 'done']))
# print (grams)

## Collocations
## http://www.nltk.org/book/ch01.html#collocations-and-bigrams
# from nltk.book import *
# text4.collocations()

## Funkar inte
#text = nltk.corpus.genesis.words('english-kjv.txt')
#bigrams = nltk.bigrams(text)
#bigrams_test = nltk.bigrams(text4)
#cfd = nltk.ConditionalFreqDist(bigrams)


# from nltk.corpus import *
# from nltk.book import text4
# from nltk.util import bigrams
# test = list(bigrams(text4))
# print (test[0])
# print (test[1])
# print (test[2])
# print (test[3])
# print (test[4])
# print (test[5])
# print (test[6])

# from nltk.probability import FreqDist
# from nltk import word_tokenize
# from nltk.collocations import *
# sentence = "Detaljhandelsföretag sjönk på Hongkongbörsen. Protesterna väntas slå mot detaljhandeln bland annat genom att turister från fastlands-Kina håller sig borta från Hong Kong under firandet av Kinas nationaldag och de omgivande helgdagarna, då protesterna väntas kulminera."
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# # change this to read in your data
# finder = BigramCollocationFinder.from_words(
#    nltk.corpus.genesis.words('english-web.txt'))
# # only bigrams that appear 3+ times
# print (finder.apply_freq_filter(1))
# # return the 10 n-grams with the highest PMI
# print (finder.nbest(bigram_measures.pmi, 10))


from nltk.corpus import brown
#brown_learned_text = brown.words(categories='learned')
from collections import Counter
testtext = "Detaljhandelsföretag sjönk på Hongkongbörsen. Protesterna väntas slå mot detaljhandeln och blä och de bland annat genom att turister och de från fastlands-Kina håller sig borta från Hong Kong under firandet av Kinas nationaldag och de omgivande helgdagarna, då protesterna väntas kulminera."
brown_learned_text = testtext.split()
#print (brown_learned_text)
#hej = sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'och'))

count_list = Counter()
list = [b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'och']
for word in list:
    count_list[word] += 1
print (count_list)

print (count_list.most_common(3))
#Counter(words).most_common(10)