"""
Created on Fri Nov 18 11:47:45 2022

"""

import pandas as pd
df = pd.read_csv("smsspamcollection.tsv", sep='\t')
df.head()
df.shape

df.isnull().sum()
list(df)

df['label'].value_counts()

Y = df['label']
X = df['message']

#===================================================================

# Pre-Processing
df['message'] = df.message.map(lambda x : x.lower())

#=== Lemmatizer ========================================================

from nltk.stem import WordNetLemmatizer
Lemm = WordNetLemmatizer()
for x in df['message'].index:
    df['message'].iloc[x] = Lemm.lemmatize(df['message'].iloc[x])
df['message']


#=== TOKENIZATION ======================================================
from sklearn.feature_extraction.text import CountVectorizer
Vectorizer = CountVectorizer()
Vt = Vectorizer.fit_transform(df['message'])
Vt.toarray()

pd.DataFrame(Vt.toarray())
pd.DataFrame(Vt.toarray()).to_csv("vt.csv")

#=====================================================================

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer().fit(Vt)
X_vect = transformer.transform(Vt)  
X_vect.shape
X_vect.toarray()

pd.DataFrame(X_vect.toarray()).to_csv("tfidf.csv")

pd.DataFrame(X_vect.toarray())[0].describe()

#====================================================================
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train,Y_test = train_test_split(X_vect,Y)
print(X_train.shape, X_test.shape,Y_train.shape,Y_test.shape)

# naive baye
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train,Y_train)
Y_pred = nb.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test,Y_pred)
cm

score = accuracy_score(Y_test,Y_pred)
score.round(2)
#===================================================================
