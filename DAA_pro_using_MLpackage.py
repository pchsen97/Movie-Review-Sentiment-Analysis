from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS
from os import listdir
import string

neg_data=[]
pos_data=[]

def doc_read(filename):
    file=open(filename,'r')
    text=file.read()
    file.close()
    tokens=text.lower()
    tokens=text.split()
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    ps=PS()
    tokens = [ps.stem(w) for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens=" ".join(tokens)
    return tokens

def process_dir(directory):
    if(directory[-1]=='g'):
        for file in listdir(directory):
            path=directory+"/"+file
            neg_data.append(doc_read(path))
    else:
        for file in listdir(directory):
            path=directory+"/"+file
            pos_data.append(doc_read(path))

directory1="txt_sentoken/neg"
directory2="txt_sentoken/pos"
process_dir(directory1)
process_dir(directory2)

data=[]
data=neg_data+pos_data

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=8000)
X=cv.fit_transform(data).toarray()

s1=[0 for i in range(0,1001)]
s2=[1 for i in range(0,1001)]
y=np.array(s1+s2)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.naive_bayes import BernoulliNB as NB
nb=NB()
nb.fit(x_train,y_train)
print(nb)

from sklearn.metrics import accuracy_score
y_expect=y_test
y_predict=nb.predict(x_test)
print(accuracy_score(y_expect,y_predict))


