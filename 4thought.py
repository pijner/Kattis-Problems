# https://open.kattis.com/problems/4thought

m = int(input())

"""
The computation of the dict can be automated by the following code. 
It shouldn't affect the speed since there will be 3*3*3 permutations at max.
"""
operators = [' + ', ' - ', ' * ', ' / ']
p = {}
for i in operators:
    for j in operators:
        for k in operators:
            temp = '4' + i + '4' + j + '4' + k + '4'
            val = eval(temp.replace('/','//'))
            p[val] = temp + " = {}".format(val)


while m:
    m-=1
    n = int(input())
    print(p[n]) if n in p else print("no solution")
