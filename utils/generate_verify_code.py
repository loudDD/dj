import random


def getcolor():
    color_bg = []
    for i in range(3):
        color = random.randrange(256)
        # print(color)
        color_bg.append(color)
    return tuple(color_bg)


def getaZ():
    #A-z 0-9
    for i in range(48, 123):
        if i not in range(58, 65) and i not in range(91, 97):
            print(chr(i))
            return i



getaZ()

