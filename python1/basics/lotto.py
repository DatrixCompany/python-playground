import random


def calcWinRate():
    win_numbs = [4, 35, 24, 21, 6, 33]
    all_numbs = []
    rand_numbs = []
    for x in range(1, 37):
        all_numbs.append(x)
    random.shuffle(all_numbs)
    for x in range(6):
        rand_numbs.append(all_numbs.pop())
    win = True
    right_numb = True
    while (win and right_numb):
        for x in range(6):
            right_numb = rand_numbs[x] in win_numbs
            win = win and right_numb
        if (win):
            print(rand_numbs)
            return win


count = 0
won = False
while (not calcWinRate()):
    count += 1
print(count)
