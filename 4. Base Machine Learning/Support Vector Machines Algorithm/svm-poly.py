
# import all necessary libraries
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

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


# 1 rakamını yeniden çizdir
"""
bir = sayilar.iloc[2, 1:]
bir = bir.values.reshape(28,28)
plt.imshow(bir)
plt.title("Rakam: 1")
plt.show()
"""


X = sayilar.drop("label", axis = 1)
y = sayilar['label']

X = scale(X)
X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, train_size=0.2,test_size = 0.8, random_state = 101)


# Boyutları göster
"""
print('X_egitim boyutları:',X_egitim.shape)
print('y_egitim boyutları:',y_egitim.shape)
print('X_test boyutları:',X_test.shape)
print('y_test boyutları:',y_test.shape)
"""


# polinomal model
model_linear = SVC(kernel='poly')

# egitim
model_linear.fit(X_egitim, y_egitim)

# tahmin
tahmin = model_linear.predict(X_test)

print("Doğruluk oranı:", metrics.accuracy_score(y_true=y_test, y_pred=tahmin), "\n")

# Karmaşıklık Matrisi
print(metrics.confusion_matrix(y_true=y_test, y_pred=tahmin))

