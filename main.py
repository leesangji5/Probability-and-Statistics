from random import randint
import matplotlib.pyplot as plt

dice_num = 10
n = 1000000
result = [0]*(dice_num*6-dice_num+1)
for i in range(n):
    a = 0
    for j in range(dice_num):
        a += randint(1, 6)
    result[a-dice_num] += 1

print(result)
label = []
for i in range(len(result)):
    label.append(i+dice_num)

plt.bar(label, result, color='blue')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Number')
plt.show()