from random import randint
import matplotlib.pyplot as plt

n = 1000000
a = []
result = 0
for i in range(n):
    a = []
    while len(a) < 6:
        card = randint(1, 52)
        if card not in a:
            a.append(card)
    if 1 in a and 2 in a and 3 in a and 4 in a and 5 in a:
        result += 1

print(result)
#100만번당 2.3번 나옴