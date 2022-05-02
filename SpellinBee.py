import string
import twl

KeyLetter = ''
while len(KeyLetter) != 1:
    try:
        KeyLetter = str(input('Letter that must be in each word: '))
    except:
        print('Please enter exactly one letter.')

Letters = ''
while len(Letters) != 6:
    try:
        Letters = input('Other letters: ')
    except:
        print('Please enter eactly 6 letters.')

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
for i in sorted(PossibleWords):
    print('   ', i)

