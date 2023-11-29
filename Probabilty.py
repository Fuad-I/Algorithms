import random


output3 = 0
total = 10000
for j in range(10000):
    count3 = 0
    for i in range(18):
        if random.randint(1, 6) == 6:
            count3 += 1

    if count3 == 3:
        output3 += 1

print(output3/total * 100)


output = 0
total = 10000
for j in range(10000):
    count = 0
    for i in range(6):
        if random.randint(1, 6) == 6:
            count += 1

    if count == 1:
        output += 1

print(output/total * 100)


output2 = 0
total = 10000
for j in range(10000):
    count2 = 0
    for i in range(12):
        if random.randint(1, 6) == 6:
            count2 += 1

    if count2 == 2:
        output2 += 1

print(output2/total * 100)
