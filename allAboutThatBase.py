# https://open.kattis.com/problems/allaboutthatbase

def convertToBase(number:int, base:int):
    result = number
    converted = []
    while(result):
        remainder = result%base
        if remainder > 9:
            remainder = chr(remainder+87)
        converted.insert(0, str(remainder))
        result = int(result // base)
    
    return "".join(converted)


def evaluateInBase(expression:list, result, base:int):
    len1 = expression.index(" ")
    len2 = len(expression) - (len1 + 2)
    modified = []
    num1, num2 = 0, 0
    for i, e in enumerate(expression):
        if e in [" ", "+", "-", "*", "/"]:
            modified.append(e)
        elif i < len1:
            num1 += int(e) * (base ** (len1-i-1))
        else:
            num2 += int(e) * (base ** (len2 -(i - len1-2) -1))

    modified.insert(0, str(num1))
    modified.append(str(num2))
    modified = "".join(modified)

    evaluation = eval(modified)
    if evaluation == int(evaluation) and evaluation > 0:
        return convertToBase(int(evaluation), base) == result
    else:
        return False 


def checkTally(expression, result):
    num1, operator, num2 = expression.split(" ")
    for c in num1:
        if c != '1':
            return False
    for c in num2:
        if c != '1':
            return False
    num1 = str(len(num1))
    num2 = str(len(num2))
    result = len(result)

    return eval(num1 + operator + num2) == result


n = int(input())

while(n):
    n-=1
    euqation = input()
    statement, result = euqation.split(' = ')
    
    lowestBase = 1
    convertedStatement = []
    for character in statement:
        asciiVal = ord(character)
        if 'a' <= character <= 'z':
            if asciiVal-86 >= lowestBase:
                lowestBase = asciiVal - 86
            convertedStatement.append(str(asciiVal-87))
            continue
        elif '0' <= character <= '9':
            if int(character) >= lowestBase:
                lowestBase = int(character) + 1
        convertedStatement.append(character)
    

    possibleBases = []
    if lowestBase == 2 and checkTally(statement, result):
        possibleBases.append('1')
    for base in range(lowestBase, 37):
        if base < 10:
            baseChar = str(base)
        elif base < 36:
            baseChar = chr(base + 87)
        else:
            baseChar = '0'
        if evaluateInBase(convertedStatement, result, base):
            possibleBases.append(baseChar)
    
    print("".join(possibleBases)) if len(possibleBases) else print("invalid")
