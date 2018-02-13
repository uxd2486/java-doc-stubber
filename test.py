

import requests


def test():
    r = requests.get("https://cs.rit.edu/~csci142/Labs/04/doc/game/HeroStorm.html")
    info = r.text
    start = info.find("START OF CLASS DATA")
    end = info.find("END OF CLASS DATA")
    info = info[start:end]
    # print(info)
    test2(r)


def test2(r):
    indexAdjust = 5
    info = r.text
    lst = [0]
    i = 0
    while True:
        addThis = info.find("========", lst[i]+5)
        if addThis == -1:
            break
        lst.append(addThis)
        i += 1
    print(lst)
    print(info[1669-indexAdjust:3898+indexAdjust])


if __name__ == '__main__':
    test()