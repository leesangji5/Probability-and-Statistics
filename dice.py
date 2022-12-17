from random import randint
import matplotlib.pyplot as plt

num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0

n = 60000
for i in range(n):
    num = randint(1, 6)
    if num == 1:
        num_1 += 1
    elif num == 2:
        num_2 += 1 
    elif num == 3:
        num_3 += 1
    elif num == 4:
        num_4 += 1
    elif num == 5:
        num_5 += 1
    else:
        num_6 += 1

label = ['1', '2', '3', '4', '5', '6']
num = [num_1, num_2, num_3, num_4, num_5, num_6]

plt.bar(label, num, color='blue')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Number')
plt.axhline(y=n/6, color='r', linestyle='-')
plt.show()