import sys

def strip_punctuation(sentence):
    charsToRemove = [':', ';', '"']
    for c in charsToRemove:
        sentence = sentence.replace(c,"")
    return sentence

def main():
    filename = sys.argv[-2]
    nrOfSentences = int(sys.argv[-1])
    sentenceList = []
    with open(filename, "r") as file:
        #word_list = file.read()
        sentence = ""
        for line in file:
            lineList = line.split();
            for word in lineList:
                if word.find('.')>-1 or word.find('?')>-1 or word.find('!')>-1:
                    sentence = sentence + word + " "
                    sentence = strip_punctuation(sentence)
                    sentenceList.append(sentence)
                    sentence = ""
                elif word.find(',')>-1 and len(sentence)>25:
                    sentence = sentence + word + " "
                    sentence = strip_punctuation(sentence)
                    sentence = sentence.replace(',','.')
                    sentenceList.append(sentence)
                    sentence = ""
                    break
                else:
                    sentence = sentence + word + " "

    if (nrOfSentences > len(sentenceList)):
        nrOfSentences = len(sentenceList)

    f = open('correct_sentences.txt','w')
    for i in range(0, nrOfSentences):
        #print (sent)
        f.write(sentenceList[i] + '\n')
    f.close()
    print('Antal meningar: '+str(nrOfSentences))

if __name__ == "__main__": main()
