
# import all necessary libraries
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split

from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

sayilar = pd.read_csv('train.csv')

X = sayilar.drop("label", axis = 1)
y = sayilar['label']

X = scale(X)
X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, train_size=0.2,test_size = 0.8, random_state = 101)



# rbf model
model_linear = SVC(kernel='poly')

# egitim
model_linear.fit(X_egitim, y_egitim)

# tahmin
def resimOku(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = img.flatten()
    return img

tahmin_edilecek_veri = resimOku("Images/resim_4.png")
tahmin = model_linear.predict([tahmin_edilecek_veri])
print("Tahmin sonucu :" + str(tahmin))

