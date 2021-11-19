#pip3 install pyemd
#pip3 install gensim
#pip3 install nltk
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from nltk import download



stop_words = stopwords.words('turkish')

model2 = KeyedVectors.load_word2vec_format('trmodel', binary=True)


cumle1 = 'Galatasaray Fenerbahçe maçı kaç kaç bitti'.lower().split()
cumle2 = 'Bugün hava güzel'.lower().split()


# WMD algoritması ile iki cümle arası mesafeyi hesaplar.
distance = model2.wmdistance(cumle1, cumle2)

print(distance)