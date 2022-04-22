import twl

KeyLetter = 'e'
Letters = 'flntuv'

SpellingBeeUpperBound = 7
SpellingBeeLowerBound = 4

SpellingBeeWords = []
for word in set(twl.iterator()):
    if SpellingBeeLowerBound <= len(set(word)) <= SpellingBeeUpperBound:
        SpellingBeeWords.append(word)

print('Spelling Bee Words:', len(SpellingBeeWords))

WordsWithKeyLetter = []
for word in SpellingBeeWords:
    if KeyLetter in word:
        WordsWithKeyLetter.append(word)

print('words with key letter:', len(WordsWithKeyLetter))

PossibleWords = []
for word in WordsWithKeyLetter:
    if set(word).issubset(set(Letters).union(set(KeyLetter))):
        PossibleWords.append(word)

print('words with key and letters:', len(PossibleWords))

print('Words:')
for i in PossibleWords:
    print('   ', i)

