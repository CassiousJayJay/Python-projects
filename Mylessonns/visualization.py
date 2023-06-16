import matplotlib.pyplot as plt
import numpy as np
import pylab



x = [1, 2, 3, 4, 5, 6]
y = [x ** 2 for x in x]
print(x)
print(y)
plt.plot(x, y)
plt.xlabel("Marks")
plt.ylabel("Gradient")
plt.show()
