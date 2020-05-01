# https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn
# https://towardsdatascience.com/building-a-simple-machine-learning-model-on-breast-cancer-data-eca4b3b99fa3

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


# Load dataset
data = load_breast_cancer()


# Organize our data
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# # Look at our data
# print(label_names)
# print(labels[0])
# print(feature_names[0])
# print(features[0])

# Split our data
train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.40,
                                                          random_state=42)

# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model = gnb.fit(train, train_labels)

# Make predictions
preds = gnb.predict(test)
# print(preds)

# Evaluate accuracy
print('naive bayes',accuracy_score(test_labels, preds))

#Using Logistic Regression Algorithm to the Training Set
from sklearn.linear_model import LogisticRegression
# Initialize our classifier
lr_classifier = LogisticRegression(random_state = 0)
# Train our classifier
lr_classifier.fit(train, train_labels)
# Make predictions
lr_preds = lr_classifier.predict(test)
# Evaluate accuracy
print('logistic regression',accuracy_score(test_labels, lr_preds))

# confusion matrix
cm = confusion_matrix(test_labels, lr_preds)

#Using DecisionTreeClassifier of tree class to use Decision Tree Algorithm

from sklearn.tree import DecisionTreeClassifier
# initialize
dt_classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
# train our classifier
dt_classifier.fit(train, train_labels)
# Make predictions
dt_preds = dt_classifier.predict(test)
# Evaluate accuracy
print('decision tree',accuracy_score(test_labels, dt_preds))

from sklearn.ensemble import RandomForestClassifier
# initialize
rf_classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
# train our classifier
rf_classifier.fit(train, train_labels)
# Make predictions
rf_preds = rf_classifier.predict(test)
# Evaluate accuracy
print('random forest',accuracy_score(test_labels, rf_preds))