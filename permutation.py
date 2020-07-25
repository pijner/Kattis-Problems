# https://open.kattis.com/problems/permcode

x = int(input())
while(x):
    s = input()
    p = input()
    c = input()
    n = len(c)
    m = [" "]*n     # Strings are immutable, so it's much easier to work with lists


    d = int(n**1.5 + x) % n

    # Find m[d] first
    m[d] = p[s.index(c[d])]

    # Work backwards from m[d]
    for i in range(1, n):
        # Make sure index doesn't do out of bounds (could have avoided this since python can handle negative indices)
        thisIndex = (d - i + n) % n
        nextIndex = (thisIndex + 1) % n

        res = s.index(c[thisIndex])
        b = s.index(m[nextIndex])

        # property: if c = a ^ b, then a = c ^ b
        m[thisIndex] = p[res ^ b]

    print("".join(m))
    x = int(input())