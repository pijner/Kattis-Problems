# https://open.kattis.com/problems/display

#           0        1        2        3        4       5         6
lines = ["+---+", "+   +", "    +", "+    ", "|   |", "    |", "|    "]
dots = ["     ", "     ", "  o  ", "     ", "  o  ", "     ", "     "]
digits = {'0': [0, 4, 4, 1, 4, 4, 0], '1': [2, 5, 5, 2, 5, 5, 2], '2': [0, 5, 5, 0, 6, 6, 0],
          '3': [0, 5, 5, 0, 5, 5, 0], '4': [1, 4, 4, 0, 5, 5, 2], '5': [0, 6, 6, 0, 5, 5, 0],
          '6': [0, 6, 6, 0, 4, 4, 0], '7': [0, 5, 5, 2, 5, 5, 2], '8': [0, 4, 4, 0, 4, 4, 0],
          '9': [0, 4, 4, 0, 5, 5, 0]}

num = input()
while num != "end":

    for i in range(7):
        print(lines[digits[num[0]][i]] + "  " + lines[digits[num[1]][i]] + dots[i] + lines[digits[num[3]][i]]
              + "  " + lines[digits[num[4]][i]])
    print("\n")
    num = input()

print("end")
