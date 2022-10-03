import re


def binsearch(l: list, key: int):
    # if l[0] > l[-1]:
    index = 0
    middle = int(len(l) / 2)
    if key == l[middle]:
        index = middle
        return index
    elif key < l[middle]:
        return binsearch(l[:middle], key)
    else:
        index += middle
        return binsearch(l[middle:], key)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print("index:{}".format(binsearch(l1, 10)))
