from random import randint
import matplotlib.pyplot as plt

n = 10
result = [0]*11
for i in range(n):
    result[randint(1, 6) + randint(1, 6)-2] += 1

print(result)
label = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

plt.bar(label, result, color='blue')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Frequency of Number')
plt.show()