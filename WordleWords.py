import twl
import matplotlib.pyplot as plt

# Define length of the words we care about
WordleLength = 5

# Define Dictionaries of letters (alphabet) w.r.t. index in array (1 counting)
LettersDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
InvLettersDict = {v:k for k,v in LettersDict.items()}

# Create a list of WordleLength letter words
WordleWords = []
for word in set(twl.iterator()):
    if len(word) == WordleLength:
        WordleWords.append(word)
print('Five Letter Words:', len(WordleWords))

# Input: This function takes on an integer between 0 and WordleLength-1 
# Output: a list of length len(LettersDict) that counts the number of times each letter appears in that position
def LetterCountPosition(position):
    LocalLetterCount = [0] * len(LettersDict)
    for word in WordleWords:
        LocalLetterCount[ LettersDict[word[position]] - 1 ] += 1
    return LocalLetterCount

# Count the number of times each letter appears in the dictionary
# Note: If a letter appears multiple times within a word, it will be counted multiple times
LetterCount = [0] * len(LettersDict)
for word in WordleWords:
    for letter in word:
        LetterCount[LettersDict[letter]-1] += 1

print('')

print('Occurrences of each letter Accounting for duplication within a word:   ', LetterCount)

# Define the Graphic
axletters = list(LettersDict.keys())
plt.bar(axletters, LetterCount, color ='forestgreen', width = 0.4)
plt.xlabel("Letters")
plt.ylabel("Appearances in Dictionary")
plt.title("Letter Appearance Accounting for Duplication Within a Word")
plt.savefig('LettersAccountingForMultiplicity')
plt.close()

# Count the number of times each letter appears in a word the dictionary
# Note: If a letter appears multiple times within a word, it will only be counted once
LettersInWordCount = [0] * len(LettersDict)
for word in WordleWords:
    for letter in set(word):
        LettersInWordCount[LettersDict[letter]-1] += 1

print('Occurrences of each letter Not Accounting or duplication within a word:', LettersInWordCount)

# Define Graphic
plt.bar(axletters, LettersInWordCount, color ='forestgreen', width = 0.4)
plt.xlabel("Letters")
plt.ylabel("Words with that letter in Dictionary")
plt.title("Letter Appearance Not Accounting for Duplication Within a Word")
plt.savefig('LettersNotAccountingForMultiplicity')
plt.close()

print('')

# Determine the distribution of letters in the dictionary (counting multiples within a word)
MaxLetterCount = max(LetterCount)
print('The letter', InvLettersDict[LetterCount.index(MaxLetterCount)+1], 'achieves occurs', MaxLetterCount, 'times, which is the maximum amount accounting for letters occurring multiple times in a single word.')
MaxLetterCountDistWithLetter = []
MaxLetterCountLetterOrder = ''
for idx,occurrence in enumerate(LetterCount):
    MaxLetterCountDistWithLetter.append([occurrence, InvLettersDict[idx+1]])
MaxLetterCountDistWithLetter.sort()
for letter in MaxLetterCountDistWithLetter:
    MaxLetterCountLetterOrder += letter[1] + ' ,'
print('    ', 'Letter Order accounting for letters occurring multiple times in a single word:', MaxLetterCountLetterOrder[:-2][::-1])
print('')

# Determine the distribution of letters within a word in the dictionary (NOT counting multiples within a word)
MaxLettersInWordCount = max(LettersInWordCount)
print('The letter', InvLettersDict[LettersInWordCount.index(MaxLettersInWordCount)+1], 'achieves occurs', MaxLettersInWordCount, 'times, which is the maximum amount without accounting for letters occurring multiple times in a single word.')
MaxLetterInWordCountDistWithLetter = []
MaxLetterInWordCountLetterOrder = ''
for idx,occurrence in enumerate(LettersInWordCount):
    MaxLetterInWordCountDistWithLetter.append([occurrence, InvLettersDict[idx+1]])
MaxLetterInWordCountDistWithLetter.sort()
for letter in MaxLetterInWordCountDistWithLetter:
    MaxLetterInWordCountLetterOrder += letter[1] + ' ,'
print('    ', 'Letter Order without accounting for letters occurring multiple times in a single word:', MaxLetterInWordCountLetterOrder[:-2][::-1])

print('')

# Determine what letters appear the most in a given position
# for loop ranges over all positions (zero counting)
PositionDistributions = []
for i in range(WordleLength):
    # Distribution of letters as achieved from the above function definition.
    Distribution = LetterCountPosition(i)

    # Plot the distribution
    plt.bar(axletters, Distribution, color ='forestgreen', width = 0.4)
    plt.xlabel("Letters")
    plt.ylabel("Words with that letter in position %s" %str(i))
    plt.title("Letter Appearance in Position %s" %str(i))
    plt.savefig('LetterDistributionPosition%s' %str(i))
    plt.close()

    # Print the statistics reguarding each position.
    MaxDistribution = max(Distribution)
    LetterOrder = ''
    print('Position', str(i) + ':')
    print('    ', 'Distribution:', Distribution)
    print('    ', 'Max in Dist: ', MaxDistribution)
    print('    ', 'Max Letter:  ', InvLettersDict[Distribution.index(MaxDistribution)+1])
    DistWithLetter = []
    for idx,occurrence in enumerate(Distribution):
        DistWithLetter.append([occurrence, InvLettersDict[idx+1]])
    DistWithLetter.sort()
    for letter in DistWithLetter:
        LetterOrder += letter[1] + ' ,'
    print('    ', 'Letter Order:', LetterOrder[:-2][::-1])
    PositionDistributions.append(LetterOrder[:-2][::-1])
    print('')

# Assign weight to each word.  Weight is the um of the rank of each letter position
# Find a minimum weight word
MinimumWeight = WordleLength*len(LettersDict)
WordsWithMinWeight = []
for word in WordleWords:
    wordWeight = 0
    for letteridx in range(WordleLength):
        wordWeight += PositionDistributions[letteridx].index(word[letteridx])/3
    if wordWeight < MinimumWeight:
        MinimumWeight = wordWeight
        WordsWithMinWeight = [word]
    if wordWeight == MinimumWeight:
        WordsWithMinWeight.append(word)

print(MinimumWeight,WordsWithMinWeight)