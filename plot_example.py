import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# source https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/simple_plot.html
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Simple plot')
ax.grid()

fig.savefig("test.png")
plt.show()