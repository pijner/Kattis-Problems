# https://open.kattis.com/problems/anagramcounting

from sys import stdin

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

for word in stdin:
    c = {}
    for character in word:
        if character in c:
            c[character] += 1
        else:
            c[character] = 1
    
    den = 1
    for uniqueCharacter in c.keys():
        den *= fact(c[uniqueCharacter])

    print((fact(len(word)-1)//den))



    