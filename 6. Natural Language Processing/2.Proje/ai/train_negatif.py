# -*- coding: utf-8 -*-

# Gerekli kütüphaneleri projeye dahil et
import pandas as pd
import numpy as np
import os
import time
import nltk
import re
from nltk.corpus import stopwords

# Tensorflow'u dahil et
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

# Oluşturduğumuz özel modelleri TFModel.py dosyasından import et
from TFmodel import MyModel
from TFmodel import OneStep

# Veri setini oku
dataset = pd.read_csv("../dataset.csv")

# Optimizasyon fonksiyonu, veri setindeki Türkçe gereksiz kelimeleri ve noktalama işaretlerini, URL leri ve dil dışı yapıları temizler.
def optimizasyon(dataset):
    dataset = dataset.dropna()

    stop_words = set(stopwords.words('turkish'))
    noktalamaIsaretleri = ['•', '!', '"', '#', '”', '“', '$', '%', '&', "'", '–', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '…']
    stop_words.update(noktalamaIsaretleri)

    for ind in dataset.index:
        body = dataset['Yorum'][ind]
        body = body.lower()
        body = re.sub(r'http\S+', '', body)
        body = (" ").join([word for word in body.split() if not word in stop_words])
        body = "".join([char for char in body if not char in noktalamaIsaretleri])
        dataset['Yorum'][ind] = body
    return dataset

# İhtiyaç halinde kullanılabilir; 
# Türkçe karakterleri ingilizce UTF-8 uyumlu hale dönüştüren fonksiyon
def trEnCevirici(metin):
  translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
  metin = metin.translate(translationTable)
  return metin


# Dataset'i optimizasyon fonksiyonundan geçir
dataset = optimizasyon(dataset)

# Yalnızca negatif (olumsuz) yorumları ayıkla
dataset_negatif = dataset.loc[dataset['Duygu'] == 0]

# negatif yorumları tek bir metin (string) içerisinde topla.
rawData = ""
for index,row in dataset_negatif.iterrows():
    rawData = rawData + row['Yorum'] + "\n"


# Bir sözcük oluştur
sozluk = sorted(set(rawData))

# Sözlük içerisindeki her bir karakterinlerden ID çıkarımı
ids_from_chars = preprocessing.StringLookup(  vocabulary=list(sozluk))
# ID lerden karakter çıkarımı
chars_from_ids = tf.keras.layers.experimental.preprocessing.StringLookup( vocabulary=ids_from_chars.get_vocabulary(), invert=True)
# Tüm metin üzerinde ID çıkarımı yap
all_ids = ids_from_chars(tf.strings.unicode_split(rawData, 'UTF-8'))

# Her bir girdi dizisi; keza yorum üreten bir yapay zeka tasarladığımız için bir girdi dizisinin bir yorumu temsil etmesi amaçlanır.
# Girdi dizisinin yani bir yorumun uzunluğunu 150 olarak belirledik.
girdi_uzunluk = 150

# Metin vektörünü bir karakter ID (index) leri veri setine dönüştür
ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)
# Bu ID dataset'inden girdi+ 1 uzunluğu kadar örnekler al.
# Batch yöntemi, bu ayrı karakterleri kolayca istenen boyuttaki dizilere dönüştürmenize olanak tanır.
diziler = ids_dataset.batch(girdi_uzunluk+1, drop_remainder=True)

# Karakterleri tekrar dizelerde birleştirmek için tf.strings.reduce_join kullanacağız.
# Bunun için text_from_ids adında bir fonksiyon oluşturacağız.
def text_from_ids(ids):
  return tf.strings.reduce_join(chars_from_ids(ids), axis=-1)

# 1 sola kaydırarak X,Y eşleşmesi oluştaracak şekilde map lemek üzere veri üretiyoruz.
# AHMET kelimesi üretilecek ise 
# (A,H,M,E) = X
# (T) = Y olması sağlanmaktadır. Böylelikle sıralı dizi üretilebilir.
def giris_cikis_bolumle(dizi):
    giris = dizi[:-1]
    cikis = dizi[1:]
    return giris, cikis

# Eğitim için gerekli X,Y değerlerini içeren dataset'i oluşturduk.
dataset = diziler.map(giris_cikis_bolumle)



# Veri kümesini karıştırmak için arabellek boyutu
# (TF verileri muhtemelen sonsuz dizilerle çalışmak üzere tasarlanmıştır,
# böylece bellekteki tüm diziyi karıştırmaya çalışmaz. Yerine, öğeleri karıştırdığı bir arabellek tutar).
dataset = (
    dataset
    .shuffle(10000)  # Buffer boyutu olarak 10000
    .batch(64, drop_remainder=True) # Batch boyutu olarak 64, 
    .prefetch(tf.data.experimental.AUTOTUNE))


# Modelimizi MyModel sınıfından oluşturuyoruz
model = MyModel(
    # Kelime boyutunun "StringLookup" katmanlarıyla eşleştiğinden emin olun.
    vocab_size=len(ids_from_chars.get_vocabulary()),
    embedding_dim=256,  # 256 gömme boyutu
    rnn_units=1024) # 1024 RNN Ünitesi

for batch_x, batch_y in dataset.take(1):
    batch_tahmin = model(batch_x)
    print(batch_tahmin.shape[0],"Batch Boyutu")
    print(batch_tahmin.shape[1],"Dizi Uzunluğu")
    print(batch_tahmin.shape[2],"Sözlük Boyutu")

model.summary()

# Bu bize her zaman adımında bir sonraki karakter indeksi için bir tahmin verir:
karakter_indexi = tf.random.categorical(batch_tahmin[0], num_samples=1)
karakter_indexi = tf.squeeze(karakter_indexi, axis=-1).numpy()

print("Giriş :\n", text_from_ids(batch_x[0]).numpy().decode('utf-8'))
print()
print("Sonraki Tahmin:\n", text_from_ids(karakter_indexi).numpy().decode('utf-8'))



# Loss fonksiyonunu "SparseCategoricalCrossentropy" olarak seçiyoruz
loss = tf.losses.SparseCategoricalCrossentropy(from_logits=True)
# Optimizer parametresini "Adam" olarak seçiyoruz
optimizer = 'adam'
# Modeli derle
model.compile(optimizer=optimizer, loss=loss)


# model.fit() fonksiyonuna dataset ve Epoch  (Döngü tekrar) sayımızı veriyoruz ve eğitimi başlatıyoruz.
# Başlatmadan önce şimdiki zamanı tutalım. Eğitim sonrası zamandan çıkarıp eğitimin ne kadar sürdüğünü hesaplayacağız.
start = time.time()
model.fit(dataset, epochs=50)

#Eğitimin ardından bir üretici model oluştur
uretici_model = OneStep(model, chars_from_ids, ids_from_chars)
states = None

# OrnekUret fonksiyonumuz üretici modeli kullanarak UTF-8 decode edilmiş bir metin döndürür.
# Bu, yapay zeka tarafından üretilen bir yorumdur.
# Bu yorum token'i baz alarak üretilir.
token = 'kargo'
sonraki = tf.constant([token])
sonuc = [sonraki]

for n in range(150):
  sonraki, states = uretici_model.generate_one_step(sonraki, states=states)
  sonuc.append(sonraki)

sonuc = tf.strings.join(sonuc)
yorum = sonuc[0].numpy().decode('utf-8')


end = time.time()
print('Model eğitildi ve kayıt edildi.\nEğitim süresi:', end - start)
print("Yapay zeka tarafından üretilen yorum:\n")
print('_'*80)
print(yorum)
tf.saved_model.save(uretici_model, 'egitilmis_model_negatif')



