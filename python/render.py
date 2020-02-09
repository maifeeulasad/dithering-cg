import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt


n = 300
real = np.random.randint(low = 0, high=256, size=(n,n), dtype='l') / 255.0
#print(real)

dn = 3
rng = default_rng()
dither = rng.choice(dn*dn, size=(dn,dn), replace=False) / float(dn*dn)
print(dither)

res = np.zeros((n,n))
for y in range (0,n):
    for x in range (0,n):
        i = x % dn
        j = y % dn
        res[x][y] = 1 if (real[x][y] > dither[i][j]) else 0
#print(res)

fig = plt.figure()

ax1 = plt.subplot(1, 3, 1)
ax1.title.set_text('Real Image('+str(n)+'x'+str(n)+')')
plt.imshow(real, cmap="gray")

ax2 = plt.subplot(1, 3, 2)
ax2.title.set_text('Dithering Matrix(3x3)')
plt.imshow(dither, cmap="gray")

ax3 = plt.subplot(1, 3, 3)
ax3.title.set_text('Resultant Image('+str(n)+'x'+str(n)+')')
plt.imshow(res, cmap="gray")

plt.show()
