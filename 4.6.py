# задача 6

from itertools import count
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle
с = 0
for el in cycle([1, 2, 3]):
    if с > 10:
        break
    print(el)
    с += 1
