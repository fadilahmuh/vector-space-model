import re
import numpy as np
import string
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math

def readTxt(fileName):
    textFile = open(fileName, "r")
    lines = textFile.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

def readDoc(fileName):
    textFile = open(fileName, "r")
    lines = textFile.readlines()
    lines2 = ''
    for i in lines:
        i = i.replace('\n', '')
        lines2 += i
    return lines2

def preprocess(doc):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    res = stemmer.stem(doc)
    res = re.sub(r"\d+", "", res)
    listres = [str(i) for i in res.split()]
    listres = [x for x in listres if x not in kamusStop]
    res = ' '.join(listres)
    # print("Result: ", res)
    tokens = nltk.tokenize.word_tokenize(res)
    kemunculan = nltk.FreqDist(tokens)
    # print(kemunculan.most_common())

    return kemunculan.most_common()

def docTerm(doc):
    res1 = [[] for i in range(len(query))]
    for i in range(len(query)):
        if query[i][0] in doc:
            cond = np.where(doc == query[i][0])[0][0]
            res1[i].append(doc[cond][0])
            res1[i].append(doc[cond][1])
        else:
            res1[i].append(query[i][0])
            res1[i].append(0)

    return res1

def vsmA(docterm):
    # print("term yg dipake", docterm)
    a,bildoc,bilterm = 0,0,0
    for i in range(len(query)):
        # print("kata ", i, " = ", query[i][1], " x ",docterm[i][1])
        a += (query[i][1] * docterm[i][1])
        bildoc += math.pow(docterm[i][1], 2)
        bilterm += math.pow(query[i][1], 2)

    b = math.sqrt(bilterm * bildoc)
    # print("perhitungan akhir ", a, "/", b)

    if b ==0:
        a = 0
    else:
        a = a / b
    return a

query = input("masukan query : ")

kamusStop = readTxt('StopWord.txt')

doc1 = preprocess(readDoc("doc1.txt"))
doc2 = preprocess(readDoc("doc2.txt"))
doc3 = preprocess(readDoc("doc3.txt"))


query = np.array(preprocess(query),dtype=np.object)
doc1 = np.array(doc1,dtype=np.object)
doc2 = np.array(doc2,dtype=np.object)
doc3 = np.array(doc3,dtype=np.object)
doc = [doc1,doc2,doc3]

term = []
hasil = []
for i in range(len(doc)):
    term.append([])
    hasil.append([])
    term[i] = docTerm(doc[i])
    a = i + 1
    hasil[i].append("doc %s" % a)
    hasil[i].append(vsmA(term[i]))

hasil = np.array(hasil,dtype=np.object)
hasil = hasil[np.argsort(hasil[:, 1])[::-1]]

print("QUERY \n",query)
print("TERM", term)
print("====================")

print("Hasil\n", hasil)
