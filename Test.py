# from math import *
from random import randint

total = 10
r = 1 / total
p = [1 for _ in range(7)] + [0 for _ in range(3)]
wk, nwk = 0.7, 0.3
times = [i for i in range(total)]

cycles = 10000
correct = 0

"""for i in range(cycles):
    time = times[randint(0, total-1)]
    if p[randint(0, 9)]:
        w1 = time
    else:
        w1 = times[randint(0, total-1)]
    if p[randint(0, 9)]:
        w2 = time
    else:
        w2 = times[randint(0, total-1)]

    if randint(0, 1):
        if w1 == time:
            correct += 1
    else:
        if w2 == time:
            correct += 1

print(correct/cycles)
print(0.7*0.7 + 0.7*0.3 + 0.7*0.3*r + 0.3*0.3*r) 

for i in range(cycles):
    time = times[randint(0, total - 1)]

    if p[randint(0, 9)]:
        w1 = time
    else:
        w1 = times[randint(0, total - 1)]

    if p[randint(0, 9)]:
        w2 = time
    else:
        w2 = times[randint(0, total - 1)]

    if p[randint(0, 9)]:
        w3 = time
    else:
        w3 = times[randint(0, total - 1)]

    temp = randint(1, 3)
    if temp == 1:
        if w1 == time:
            correct += 1
    elif temp == 2:
        if w2 == time:
            correct += 1
    else:
        if w3 == time:
            correct += 1

print(correct / cycles)
print(wk ** 3 + 2 * wk ** 2 * nwk + wk**2*nwk*r + wk * nwk ** 2 + 2*wk*nwk**2*r + nwk ** 3 * r) """


