import pandas as pd
import numpy as np
from PIL import Image
import cv2
sayilar = pd.read_csv('test.csv')


for i in range(10):
    img = sayilar.iloc[i, 0:]
    img = img.values.reshape(28,28)
    cv2.imwrite("Images/resim_"+ str(i) + ".png", img)
