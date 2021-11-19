#pip3 install keras
#pip3 install tensorflow
#pip3 install nltk
#pip3 install gensim

from keras.layers import Dense,Embedding,LSTM,Dropout
from keras.models import Sequential,load_model
from sklearn.model_selection import train_test_split

from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import gensim

import nltk
from nltk.corpus import stopwords
import re

import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')

import os
#nltk.download('stopwords')
dataset = pd.read_csv('dataset.csv')
dataset.head()
dataset.sort_values("Body", inplace = True)

dataset.drop_duplicates(subset ="Body",keep = False, inplace = True)
                     
# Tüm datasetteki Body yani haber metinlerini yorumlanabilmek üzere optimize eden fonksiyon.
# Bir metini stopword kelimelerden, noktalama işaretlerinden, linklerden ve gereksiz yapılardan temizleyen optimizasyon fonksiyonu.
# Yapay zeka tarafından yorumlanacak veri ilk olarak bu aşamadan geçer
def optimizasyon(dataset):
    dataset = dataset.dropna()

    stop_words = set(stopwords.words('turkish'))
    noktalamaIsaretleri = ['•', '!', '"', '#', '”', '“', '$', '%', '&', "'", '–', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…']
    stop_words.update(noktalamaIsaretleri)

    for ind in dataset.index:
        body = dataset['Body'][ind]
        body = body.lower()
        body = re.sub(r'http\S+', '', body)
        body = re.sub('\[[^]]*\]', '', body)
        body = (" ").join([word for word in body.split() if not word in stop_words])
        body = "".join([char for char in body if not char in noktalamaIsaretleri])
        dataset['Body'][ind] = body
    return dataset

dataset = optimizasyon(dataset)

# Veri setini X ve Y yani parametre ve etiket olarak ayırıyoruz. Makine öğrenmesi uygulamalarından bu duruma alışkınız.
X = dataset.loc[:,"Body"]
y = dataset.loc[:,"Label"]

# Verilerimizi eğitim ve test olmak üzere ayırıyoruz. Verilerin %20 si test verisi olarak ayarlansın.
X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size = 0.2, random_state = 28) 




# Tokenizer sınıfı kullanılarak dataset'deki tüm düz metinler, yapay zekanın yorumlayacağı hale getirilir.
X_egitim_dizi = [metin.split() for metin in X_egitim]

# Word2Vec yani dökümanı vektöre çevirecek gensim modeli için gerekli parametreler
maxmesafe = 2 #Bir cümle içindeki mevcut ve tahmin edilen kelime arasındaki maksimum mesafe
minfrekans = 1 #Toplam sıklığı bundan daha düşük olan kelimeleri göz ardı eder
vektor_boyut = 200 #Öznitelik vektörlerinin boyutluluğu
w2v_model = gensim.models.Word2Vec(sentences = X_egitim_dizi, vector_size=vektor_boyut, window = maxmesafe,  min_count = minfrekans)          


tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_egitim_dizi)
X_egitim_tok = tokenizer.texts_to_sequences(X_egitim_dizi)
kelime_index = tokenizer.word_index

maxlen = 1000 #Bir  metninin maksimum uzunluğu
X_egitim_tok_pad = pad_sequences(X_egitim_tok, maxlen=maxlen)

# Tüm dataset'indeki vocab (sözlük) kelime sayısı.
kelime_sayi = len(kelime_index) + 1

print('Sözlük boyutu: ', kelime_sayi)

# Modelin ağırlıklarını içeren bir matris oluşturmalıyız. Bunun için kelime başına satır içeren ağırlık matrisini üreteceğiz.
# Bu matrister her satır, kelime ile ilişkili vektördür.
# Matris boyutları (kelime sayısı +1, öznitelik vektörlerinin boyutsallığı) şeklindedir. 
# İlk satır sadece [0 ... 0] vektörünü içerir ve eğitim setinde olmayan kelimeler buradadır.
matris = np.zeros((kelime_sayi, vektor_boyut))
for kelime, i in kelime_index.items():
    matris[i] = w2v_model.wv[kelime]



# LSTM yapay sinir ağı modelini kullanacağız.

model = Sequential()

# Ağırlıklar olarak Word2Vec modeli tarafından oluşturulan ağırlıkları veriyoruz.
# Modelin Word2Vec modeli tarafından belirlenen ağırlıkları değiştirmesini istemiyoruz, bu yüzden eğitilebilir parametreyi False olarak ayarlıyoruz.
model.add(Embedding(matris.shape[0], 
                    output_dim=matris.shape[1],
                    weights=[matris], 
                    input_length=maxlen, 
                    trainable=False))
model.add(LSTM(units=32))   
model.add(Dense(1, activation='sigmoid'))   # Aktivasyon fonksiyonu olarak "Sigmoid" i seçiyoruz
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])    # Optimizer parametresi olarak "adam", loss için ise "binary_crossentropy" seçiyoruz.
# Metrik olarak "acc" ise "Accuraty" yani doğruluk anlamına gelmektedir. 

# Modelimizin özetini konsola yazdıralım
model.summary()
# Eğitim için X ve y (parametre,etiket) eşleşmesi ile verilerimizi veriyoruz.
# Burada doğrulamak için verilerin %20 sini validation_split=0.2 olarak ayarladık.
# Eğitim 30 epochs olacak. Bu, verilerin yapay sinir ağından kaç defa geçeceği bilgisidir. Bir nevi döngü sayısı diyebiliriz.
# Batch size, yığın olarak ağdan geçirilecek verilerin sayısını belirler. 
# Eğitim işlemi biraz uzun sürebilir. Bu süreç konsola bir yükleme çubuğu ile yansıtılmaktadır.
model.fit(X_egitim_tok_pad, y_egitim, validation_split=0.2, epochs=30, batch_size = 32, verbose = 1)

# Modelin eğitiminin tamamlanmasının ardından, eğitilmiş ağı "model ağırlıkları" olarak "egitilmis_model.h5" dosyasına kayıt edeceğiz.
# Böylece eğitimi yapmış oluruz. Daha sonra bu modeli başka bir python dosyasında yükleyerek doğru/yanlış haberi sınıflandırmada kullanabiliriz.
model.save('egitilmis_model2.h5')
print("Model eğitildi ve kayıt edildi !")



