# https://stackabuse.com/classification-in-python-with-scikit-learn-and-pandas/
# data download from: https://web.stanford.edu/~hastie/ElemStatLearn/
# South African Heart Disease: download the .data file, and rename the extention to .csv. It will convert the file into csv file.
# important concepts to understand: https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os
from warnings import filterwarnings
filterwarnings('ignore')

os.chdir('../../../Data')
heart = pd.read_csv('SAHeart.csv', sep=',', header=0)
#print(heart.head())

# replacing string with categorization numbers
heart.famhist[heart.famhist == 'Present'] = 0
heart.famhist[heart.famhist == 'Absent'] = 1
# print(heart['famhist'])

X = heart.iloc[:,:9] #first 9 columns of data frame with all rows
y = heart.iloc[:,9] #only 9th column of data frame will all rows


# print(X)
# print(y)

LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X, y)
print(LR.predict(X.iloc[460:,:]))
#We can then use the predict method to predict probabilities of new data, as well as the score method to get the mean prediction accuracy
print(round(LR.score(X,y), 4) )

SVM = svm.LinearSVC()
SVM.fit(X, y)
print(SVM.predict(X.iloc[460:,:]))
print(round(SVM.score(X,y), 4))

RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
RF.fit(X, y)
print(RF.predict(X.iloc[460:,:]))
print(round(RF.score(X,y), 4))