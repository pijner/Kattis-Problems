# https://open.kattis.com/problems/alphabetanimals

prevWord = input()
n = int(input())
remainingAnimals = []
usableAnimals = []
startLetters = {}

while(n):
    n -= 1
    thisAnimal = input()
    remainingAnimals.append(thisAnimal)
    startLetters[thisAnimal[0]] = (startLetters[thisAnimal[0]] + 1 if thisAnimal[0] in startLetters else 1)
    if prevWord[-1] == thisAnimal[0]:
        usableAnimals.append(thisAnimal)

if not len(usableAnimals):
    print("?")
else:
    winFlag = False
    for word in usableAnimals:
        if word[-1] not in startLetters or (startLetters[word[-1]] == 1 and word[0] == word[-1]):
            print(word + "!")
            winFlag = True
            break
    
    if not winFlag:
        print(usableAnimals[0])
    
