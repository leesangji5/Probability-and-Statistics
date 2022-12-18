import matplotlib.pyplot as plt

label = ['1', '2', '3', '4', '5']
result = [999, 1018, 956, 1040, 1027]
plt.bar(label, result, color='blue')
plt.axhline(y=1000, color='r', linestyle='-')
plt.show()