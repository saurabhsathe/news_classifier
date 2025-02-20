# -*- coding: utf-8 -*-
"""fake_news.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mBMikVqlSM7eFhMGdSCns9FQFUj8uUy9
"""

import pandas as pd

import os

print(os.listdir())
os.chdir('../content')
dataset=pd.read_csv("news.csv")

print(dataset)

x = dataset.iloc[1:,:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)

x=x[:,[2]]

from sklearn.feature_extraction.text import TfidfVectorizer

tfid=TfidfVectorizer(stop_words='english',max_df=0.7)

x=tfid.fit_transform(dataset['text'])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=7)

print(xtrain)

from sklearn.ensemble import RandomForestClassifier

classifier= RandomForestClassifier(n_estimators=1000)

classifier.fit(xtrain,ytrain)

ypred=classifier.predict(xtest)

from sklearn.metrics import confusion_matrix,accuracy_score
acc=accuracy_score(ytest,ypred)
print(acc)
print(confusion_matrix(ytest,ypred))