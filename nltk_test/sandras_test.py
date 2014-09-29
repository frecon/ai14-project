## Sixgrams from sentence
from nltk.util import ngrams
sentence = "Detaljhandelsföretag sjönk på Hongkongbörsen. Protesterna väntas slå mot detaljhandeln bland annat genom att turister från fastlands-Kina håller sig borta från Hong Kong under firandet av Kinas nationaldag och de omgivande helgdagarna, då protesterna väntas kulminera."
n = 2
sixgrams = ngrams(sentence.split(), n)
count = 0
for grams in sixgrams:
    count=count+1
    print (grams)
print (count)


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
# from nltk.corpus import *
# from nltk.util import bigrams
# text = nltk.corpus.genesis.words('english-kjv.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)