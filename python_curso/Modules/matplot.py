#https://es.stackoverflow.com/questions/348101/error-al-instalar-paquetes-pip-no-se-reconoce-como-un-comando-interno-o-exte
#py -m pip install matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,4,6,8]



legend = ("January", "February", "March", "April")

plt.xticks(x, legend)

plt.plot(x, y)
plt.show()