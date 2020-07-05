import pandas as pd
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
def database(text):
    pf = pd.read_csv("Product_1.csv", delimiter = "|")
    type(pf)
    names = pf["RATE DIFF 18%"]
    type(names)
    c = 0
    for i in names:
        word = word_tokenize(i)
        for i in word:
            if i == text:
                print(pf.iloc[c])
    
        c +=1
