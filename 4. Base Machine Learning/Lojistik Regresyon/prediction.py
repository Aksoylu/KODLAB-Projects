import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def optimizasyon(metin):

    stop_words = set(stopwords.words('turkish'))
    noktalamaIsaretleri = ['•', '!', '"', '#', '”', '“', '$', '%', '&', "'", '–', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…']
    stop_words.update(noktalamaIsaretleri)

    body = metin
    body = body.lower()
    body = re.sub(r'http\S+', '', body)
    body = re.sub('\[[^]]*\]', '', body)
    body = (" ").join([word for word in body.split() if not word in stop_words])
    body = "".join([char for char in body if not char in noktalamaIsaretleri])
    return body


tahminEdilecekMetin  = input("Sınıflandırılmak üzere bir yorum giriniz:")
tahminEdilecekMetin = optimizasyon(tahminEdilecekMetin)

tfIdf = pickle.load(open("vektorlestirici", 'rb'))
tahminEdilecekMetin_vec = tfIdf.transform([tahminEdilecekMetin])
#print(tahminEdilecekMetin_vec)

LogisticRegressionModel = pickle.load(open("egitilmis_model", 'rb'))
tahminSonuc = LogisticRegressionModel.predict(tahminEdilecekMetin_vec)
print(tahminSonuc)

if(tahminSonuc == 0):
    print("Bu yorumun makine üretimi olduğu tahmin edilmiştir")
else:
    print("Bu yorumun insan üretimi olduğu tahmin edilmiştir")