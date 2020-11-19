import string

def readTxt(fileName):
    textFile = open(fileName, "r")
    lines = textFile.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

# Input Dokumen
stringText = input("Input text : ")

# Case Folding
lower_document = stringText.lower()
print("Lowcase Document : ", lower_document)

dltNumber = ''.join([i for i in lower_document if not i.isdigit()])
print("Document with no number : ", dltNumber)

punctuation = set(string.punctuation)
noPunctuation = ''.join(ch for ch in dltNumber if ch not in punctuation)
print("Document with no punctuation : ", noPunctuation)

noWhitespace = noPunctuation.strip();
print("Dokumen with no whitespace: ", noWhitespace)

#Tokenizing
word = noWhitespace.split()
print("Split: ", word)
print(len(word), " word")

removeMultipleWord = list(set(word))
print("Tokenizing: ", removeMultipleWord)
print(len(removeMultipleWord), " word")

#Filtering / Stop Removal
stopRemoval = readTxt('StopWord.txt')
withoutStopword = [x for x in removeMultipleWord if x not in stopRemoval]
print("Filtering Document : ",withoutStopword)

#Manual Stemming
kata_dasar = readTxt('kata-dasar.txt')
akhiran = ["i", "an", "kan", "ku", "mu", "nya", "lah", "kah", "tah", "pun"]
awalan = ["di","ke","se","me","be","pe", "te"]
root_word = []
for index, word in enumerate(withoutStopword):
    #print("sesi kata ", kata)

    # cek langsung ke kata_dasar
    if word in kata_dasar:
        #print(kata, " = kata dasar murni")
        root_word.append(word)
        continue

    # cek akhiran
    for p in akhiran:
        if word[-len(p):] == p and word[:-len(p)] in kata_dasar:
            #print(kata, " = ", kata[:-len(p)], " + ", p)
            root_word.append(word[:-len(p)])
            break

    # cek awalan
    for x in awalan:
        if word[:len(x)] == x and word[len(x):] in kata_dasar:
            #print(kata, " = ",  x, " + ", kata[len(x):])
            root_word.append(word[len(x):])
            break

print("Dokumen with stemming manual: ",root_word)

