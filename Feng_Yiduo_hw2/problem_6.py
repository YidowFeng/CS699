"""
Yiduo Feng
Class: CS 699
Date: 05/24/2022
Homework Problem: 4

"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

# def get_frames():

#read files
file = "autism-adult-a2.csv"
df = pd.read_csv(file)
# get the class column
label = []
for r in df['Class/ASD'].values:
    if r == "YES":
        label.append(1)
    else:
        label.append(0)
df['label'] = label

# predict by Gaussian Naive Bayes

train, test = train_test_split(df, test_size=0.34, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :10], df.loc[:, "label"],
                     test_size=0.34, random_state=3)

gnb = GaussianNB()
Y_pred = gnb.fit(X_train, Y_train).predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)

print(accuracy)

