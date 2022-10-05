import matplotlib.pyplot as plt
import numpy as np
count = 0

mev = 4
y = []
while mev >= 1:
    y.append(mev)
    count += 1
    mev -= 0.000549 * mev
    if count == 2206:
        print("Count is 2206",mev)
print(count, mev)
x = np.arange(count)

plt.plot(x,y)
plt.show()
