import random
import matplotlib.pyplot as plt
# 433160번당 1회

n = 43316000
result = [0, 0, 0, 0, 0]
for j in range(5):
    for i in range(n):
        a = random.sample(range(1, 53), 6)
        if 1 in a and 2 in a and 3 in a and 4 in a and 5 in a:
            result[j] += 1


label = ['1', '2', '3', '4', '5']
plt.bar(label, result, color='blue')
plt.axhline(y=n/433160, color='r', linestyle='-')
plt.show()