import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [100, 200, 150, 350]

legend = ("January", "February", "March", "April")
plt.xticks(x, legend)

plt.bar(x,y)
plt.ylabel("Sales")
plt.title("Sales per month")
plt.show()