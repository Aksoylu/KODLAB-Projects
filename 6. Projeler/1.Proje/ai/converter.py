import googletrans
import pandas as pd
import httpx
timeout = httpx.Timeout(50) # 5 seconds timeout
dataset = pd.read_csv("out.csv")


#data = dataset.iloc[3:]

data = dataset.loc[:, ["Body","Label"]]

from googletrans import Translator
translator = Translator(timeout=timeout)

#print(data[615:].head())

#exit()
l = len(data.index)
i = 0
for ind in data.index:
    if ind <= 2930:
        i = i + 1
        continue

    result = translator.translate(text=str(data['Body'][ind]), src='en', dest='tr')
    data['Body'][ind] = result.text
    print(result.text)
    print("Tamam :" +str(i) + "| Kalan : " + str(l-i))
    
    if i % 10 == 0:
        data.to_csv("out.csv", index=False)
    i = i + 1



data.to_csv("out.csv", index=False)



