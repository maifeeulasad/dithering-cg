import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

n = 300
real = np.random.randint(low = 0, high=256, size=(n,n), dtype='l')
#print(real)

dn = 3
rng = default_rng()
dither = rng.choice(dn*dn, size=(dn,dn), replace=False)
print(dither)

res = np.zeros((n,n))
for y in range (0,n):
    for x in range (0,n):
        i = x % dn
        j = y % dn
        res[x][y] = 255 if (real[x][y] > dither[i][j]) else 0
#print(res)


fig = plt.figure()

plt.subplot(1, 3, 1)
plt.imshow(real, cmap="gray")

plt.subplot(1, 3, 2)
plt.imshow(dither, cmap="gray")

plt.subplot(1, 3, 3)
plt.imshow(res, cmap="gray")

plt.show()
