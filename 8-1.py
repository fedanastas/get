import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print((tmp))

freq_time = tmp[1]
freq_volt = tmp[0]

data_array = np.loadtxt("data.txt", dtype = int)
voltage_array = data_array * freq_volt
no_time = np.arange(0, len(data_array), 1)
time = no_time * freq_time

charge_time = (np.argmax(data_array)) * freq_time

fig, ax = plt.subplots(figsize = (18, 14), dpi = 300)

ax.plot(time, voltage_array, label = 'U(t)', linewidth = 2, color = 'blue')
ax.plot(time, voltage_array, marker = 'X', markersize = 0.8, color = 'blue', markevery = 1000)
ax.legend() #примитивная легенда

ax.set_xlim(0, 15)
ax.set_ylim(0, 3.5)

ax.set_xlabel('Время (с)')
ax.set_ylabel('Напряжение (В)')
ax.set_title('Процесс зарядки и разрядки конденсатора в RC-цепочке') #задание заголовка

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.2))

#добавление текста
uncharge_time = len(data_array) * freq_time - charge_time
ax.text(2.5, 1.75, 'Время зарядки = {:.3f}c'.format(charge_time))
ax.text(2.5, 1.55, 'Время разарядки = {:.3f}c'.format(uncharge_time))

#включение второстепенного деления осей
ax.minorticks_on()

#настройка сетки
ax.grid(which = 'major', color = 'k', linewidth = 1)
ax.grid(which = 'minor', color = 'k', linestyle = ':')

fig.savefig("grafic.png")
plt.show()


