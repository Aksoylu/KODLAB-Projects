import numpy as np
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour


gorsel = data.astronaut()


gorsel = rgb2gray(gorsel)

s = np.linspace(0, 2*np.pi, 400)
r = 100 + 100*np.sin(s)
c = 220 + 100*np.cos(s)
cember = np.array([r, c]).T

                       
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(gorsel, cmap=plt.cm.gray)
ax.plot(cember[:, 1], cember[:, 0], '--r', lw=3)

kordon = active_contour(gaussian(gorsel, 3),cember, alpha=0.015, beta=10, gamma=0.001)


ax.plot(kordon[:, 1], kordon[:, 0], '-b', lw=3)

plt.savefig("sonuc.png")