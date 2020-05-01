# https://www.kaggle.com/mattwills8/multi-class-classification-of-iris-dataset
import pandas as pd

from sklearn.datasets import load_iris
from pandas import Series, DataFrame

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris = load_iris()
X = iris.data
Y = iris.target

print(X.shape) #(150, 4) -- 4 features: sepal length, sepal width, petal length, petal width

# create dataframes for visualisations

iris_data = DataFrame(X, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
iris_target = DataFrame(Y, columns=['Species'])

# at the moment we have 0, 1 and2 for species, so we want to change that to make it clearer
def flower(num):
    if num == 0:
        return 'Setosa'
    elif num == 1:
        return 'Versicolour'
    else:
        return 'Virginica'


iris_target['Species'] = iris_target['Species'].apply(flower)
# combine dataframes

iris = pd.concat([iris_data, iris_target], axis=1)
print(iris.shape)



log_reg = LogisticRegression()

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=3) # here X has 4 columns all numbers

log_reg.fit(X_train, Y_train)

Y_pred = log_reg.predict(X_test)

print(metrics.accuracy_score(Y_test, Y_pred))