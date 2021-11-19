#model = https://github.com/akoksal/Turkish-Word2Vec

import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import gensim
import warnings

warnings.filterwarnings("ignore")


model =  gensim.models.Word2Vec.load('word2vec.model') #KeyedVectors.load_word2vec_format('word2vec.model', binary=True)



benzerler = model.most_similar("çay")
print("Çay kelimesine benzeyen tüm kelimeler :")
print(benzerler)

benzerler = model.most_similar("japonya")
print("Japonya kelimesine benzeyen tüm kelimeler :")
print(benzerler)



benzerler = model.most_similar(positive=["dal", "kök", "yaprak"])
print(benzerler)

benzerler =  model.most_similar(positive=["kral","kadın"],negative=["erkek"])
print(benzerler)

benzerlik =  model.similarity("çay","kahve")
print(benzerlik)


benzerlik = model.doesnt_match(["çay","kahve","fincan","insan"])
print(benzerlik)

