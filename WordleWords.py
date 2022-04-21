import twl

WordleLength = 5

LettersDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

InvLettersDict = {v:k for k,v in LettersDict.items()}

WordleWords = []
for word in set(twl.iterator()):
    if len(word) == WordleLength:
        WordleWords.append(word)

print('Five Letter Words:', len(WordleWords))

def LetterCountPosition(position):
    LocalLetterCount = [0] * 26
    for word in WordleWords:
        LocalLetterCount[ LettersDict[word[position]] - 1 ] += 1
    return LocalLetterCount

LetterCount = [0] * 26
for word in WordleWords:
    for letter in word:
        LetterCount[LettersDict[letter]-1] += 1

LettersInWordCount = [0] * 26
for word in WordleWords:
    for letter in set(word):
        LettersInWordCount[LettersDict[letter]-1] += 1

print('')

print('Occurances of each letter Accounting for duplication within a word:   ', LetterCount)
print('Occurances of each letter Not Accounting or duplication within a word:', LettersInWordCount)

print('')

MaxLetterCount = max(LetterCount)
print('The letter', InvLettersDict[LetterCount.index(MaxLetterCount)+1], 'achieves occurs', MaxLetterCount, 'times, which is the maximum amount accounting for letters occuring multiple times in a single word.')

MaxLettersInWordCount = max(LettersInWordCount)
print('The letter', InvLettersDict[LettersInWordCount.index(MaxLettersInWordCount)+1], 'achieves occurs', MaxLettersInWordCount, 'times, which is the maximum amount without accounting for letters occuring multiple times in a single word.')

print('')

for i in range(WordleLength):
    Distribution = LetterCountPosition(i)
    MaxDistribution = max(Distribution)
    LetterOrder = ''
    print('Position', str(i) + ':')
    print('        ', 'Distribution:', Distribution)
    print('        ', 'Max in Dist: ', MaxDistribution)
    print('        ', 'Max Letter:  ', InvLettersDict[Distribution.index(MaxDistribution)+1])
    while Distribution != []:
        LetterOrder += InvLettersDict[Distribution.index(max(Distribution))+1] + ', '
        Distribution.remove(max(Distribution))
    print('        ', 'Letter Order:', LetterOrder[:-2])
    print('')