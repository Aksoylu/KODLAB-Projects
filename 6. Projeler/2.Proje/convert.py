import pandas as pd

dataset = pd.read_csv("out.csv")


# Pozitif yorumlar için veri setini eğit ve model oluştur.

dataset_pozitif = dataset.loc[dataset['Duygu'] == 1]

rawData = ""
for index,row in dataset_pozitif.iterrows():
    rawData = rawData + row['Yorum'] + "\n"


import io
with io.open("data", "w", encoding="utf-8") as f:
    f.write(rawData)