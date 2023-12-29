# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:13:28 2023

@author: excel
"""

import nltk
nltk.download()

text = 'The capital of India is Newdelhi'

from nltk.tokenize import word_tokenize
token1 = word_tokenize(text)
token1

import nltk
from nltk.corpus import stopwords

l1 = stopwords.words("English")
l1[0]
len(l1)
l1.append("bought")
l1.append(",")
len(l1)

# Step 3 - Create a Simple sentence
text = "the city is beautiful, but due to traffic noise polution "
"is increasing on daily basis which is hurting all the people"

token2 = word_tokenize(text)
token2
len(token2)

newlist = []
for i in token2:
    if not i in l1:
        newlist.append(i)

print(newlist)
len(newlist)

# from nltk.stem import PorterStemmer
from nltk.stem import PorterStemmer
p_stemmer = PorterStemmer()
e_words= ["wait", "waiting", "waited", "waits"]

for word in e_words:
    print(word+' --> '+p_stemmer.stem(word))


#=================================================================







