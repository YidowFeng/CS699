"""
Yiduo Feng
Class: CS 699
Date: 05/30/2022
Homework Problem: 4

"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score

# def get_frames():

#read files
file = "Accidents1000.csv"
df = pd.read_csv(file)

# predict by Gaussian Naive Bayes

train, test = train_test_split(df, test_size=0.34, random_state=3)
X_train, X_test, Y_train, Y_test = \
    train_test_split(df.iloc[:, :10], df.loc[:, "MAX_SEV"],
                     test_size=0.34, random_state=3)

clf = LinearDiscriminantAnalysis()
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print(accuracy)

