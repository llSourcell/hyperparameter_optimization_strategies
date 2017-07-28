import pandas as pd
import svm
from random import randint

#read data
dataframe=pd.read_csv("tweets_all.csv")
X = dataframe[['tweet']]
y = dataframe[['sentiment']]

best_score = 0  
best_params = {'C': None, 'gamma': None}

#for a preset number of iterations
for i in range(10):
    #try random values for each hyperparameter
    svc = svm.SVC(C=randint(0, 9), gamma=randint(0, 3))
    svc.fit(X, y)
    score = svc.score(Xval, yval)

    if score > best_score:
        best_score = score
        best_params['C'] = C
        best_params['gamma'] = gamma

best_score, best_params  
