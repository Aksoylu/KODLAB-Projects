from PIL import Image
import numpy as np


gorselMatris = np.array(Image.open('orijinal.png'))

gorsel_K = gorselMatris.copy()
gorsel_K[:, :, (1, 2)] = 0
gorsel_Y = gorselMatris.copy()
gorsel_Y[:, :, (0, 2)] = 0
gorsel_M = gorselMatris.copy()
gorsel_M[:, :, (0, 1)] = 0

gorselTotal = np.concatenate((gorsel_K , gorsel_Y, gorsel_M ), axis=1)
yeniGorsel = Image.fromarray(gorselTotal )
yeniGorsel .save('test.jpg')