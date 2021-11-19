import tensorflow as tf
import pandas as pd
import numpy as np
import os
import time
# -*- coding: utf-8 -*-
import nltk
import re
from nltk.corpus import stopwords
from random import randint
from ai.TFmodel import MyModel
from ai.TFmodel import OneStep

dataset = pd.read_csv("dataset.csv")

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

dataset = optimizasyon(dataset)


# Pozitif için 1, negatif için 0
def rastgeleObekSec(dataset,duygu):
    dataset_duygu = dataset.loc[dataset['Duygu'] == duygu]
    yorumSayi = len(dataset_duygu)
    rastgeleSayi = randint(0, yorumSayi-1)
    rastgeleYorum = dataset_duygu['Yorum'][rastgeleSayi-1]
    kelimeler = rastgeleYorum.split(" ")
    kelimeSayi = len(kelimeler)
    rastgeleSayi = randint(0, kelimeSayi-1)
    return kelimeler[rastgeleSayi]





model_negatif = tf.saved_model.load('ai/egitilmis_model_negatif')
model_pozitif = tf.saved_model.load('ai/egitilmis_model_pozitif')


def yorum_uret(duygu,token):
    if token == "-":
        token = ""
        while token == "":
            try:
                token = rastgeleObekSec(dataset,duygu)
            except:
                continue
    states = None
    next_char = tf.constant([token])
    result = [next_char]

    for n in range(100):
        if duygu == 0:
            next_char, states = model_negatif.generate_one_step(next_char, states=states)        
        else:
            next_char, states = model_pozitif.generate_one_step(next_char, states=states)        
        result.append(next_char)
    return tf.strings.join(result)[0].numpy().decode("utf-8")



yorum1 = yorum_uret(1,"iyi")
yorum2 = yorum_uret(0,"kötü")

print(yorum1)
print("-"*100)
print(yorum2)