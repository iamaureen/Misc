# https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f
# https://www.kaggle.com/selener/multi-class-text-classification-tfidf
# problem Target: Given a new complaint comes in, we want to assign it to one of 12 categories
import pandas as pd
import numpy as np
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn import metrics

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

df = pd.read_csv('../Data/Consumer_Complaints.csv')
# print(df.head())

# print(df.shape) #(1461658, 18)


# # For this project, we need only two columns — “Product” and “Consumer complaint narrative”.
# col = ['Product', 'Consumer complaint narrative']
# df = df[col]  # or the following
df1 = df[['Product', 'Consumer complaint narrative']].copy()

# # remove missing values (NaN) in “Consumer complaints narrative” column
df1 = df1[pd.notnull(df1['Consumer complaint narrative'])]

# Renaming second column for a simpler name
df1.columns = ['Product', 'Consumer_complaint']

print(df1.shape) #(475411, 2)

# Percentage of complaints with text
total = df1['Consumer_complaint'].notnull().sum()
print(round((total/len(df)*100),1)) #(~ 32.5% of the original dataset is not null).

# total number of categories we want to classify each complaint -- #18
# print(pd.DataFrame(df.Product.unique()).values)

# Because the computation is time consuming (in terms of CPU), the data was sampled
df2 = df1.sample(10000, random_state=1).copy()

# Renaming categories
# why? There are 18 different classes or categories (target). However; it is observed that some classes are contained in others.
# For instance, ‘Credit card’ and ‘Prepaid card’ are contained in ‘Credit card or prepaid card’ category. Now, imagine there is a new complaint
# about Credit card and we want to classify it. The algorithm can either classify this complaint as 'Credit card' or 'Credit card or prepaid' and
# it would be correct. Nevertheless, this would affect model performance. In order to avoid this problem, the names of some categories were renamed.

df2.replace({'Product':
             {'Credit reporting, credit repair services, or other personal consumer reports':
              'Credit reporting, repair, or other',
              'Credit reporting': 'Credit reporting, repair, or other',
              'Credit card': 'Credit card or prepaid card',
              'Prepaid card': 'Credit card or prepaid card',
              'Payday loan': 'Payday loan, title loan, or personal loan',
              'Money transfer': 'Money transfer, virtual currency, or money service',
              'Virtual currency': 'Money transfer, virtual currency, or money service'}},
               inplace= True)

# print(pd.DataFrame(df2.Product.unique())) #The number of classes were reduced from 18 to 13. (from line 34)

# Categorize the product. integer is better than strings.
# Create a new column 'category_id' with encoded categories

df2['category_id'] = df2['Product'].factorize()[0]
category_id_df = df2[['Product', 'category_id']].drop_duplicates()

# Dictionaries for future use
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Product']].values)

# New dataframe
# print(df2.head())


# # fig = plt.figure(figsize=(8,6))
# # df.groupby('Product').Consumer_complaint_narrative.count().plot.bar(ylim=0)
# # plt.show()

# another plot
# fig = plt.figure(figsize=(8,6))
# colors = ['grey','grey','grey','grey','grey','grey','grey','grey','grey',
#     'grey','darkblue','darkblue','darkblue']
# df2.groupby('Product').Consumer_complaint.count().sort_values().plot.barh(
#     ylim=0, color=colors, title= 'NUMBER OF COMPLAINTS IN EACH PRODUCT CATEGORY\n')
# plt.xlabel('Number of ocurrences', fontsize = 10);
# plt.show()

# # The classifiers and learning algorithms can not directly process the text documents in their original form, as most of them expect numerical feature
# # vectors with a fixed size rather than the raw text documents with variable length. Therefore, during the preprocessing step, the texts are converted
# # to a more manageable representation.
#
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,
                        ngram_range=(1, 2),
                        stop_words='english')
# tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

# We transform each complaint into a vector
features = tfidf.fit_transform(df2.Consumer_complaint).toarray()

#print("Each of the %d complaints is represented by %d features (TF-IDF score of unigrams and bigrams)" %(features.shape))

labels = df2.category_id

# Finding the three most correlated terms with each of the product categories #TODO: understand how this works & how this can be used later.
# N = 3
# for Product, category_id in sorted(category_to_id.items()):
#   features_chi2 = chi2(features, labels == category_id)
#   indices = np.argsort(features_chi2[0])
#   feature_names = np.array(tfidf.get_feature_names())[indices]
#   unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
#   bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
#   print("\n==> %s:" %(Product))
#   print("  * Most Correlated Unigrams are: %s" %(', '.join(unigrams[-N:])))
#   print("  * Most Correlated Bigrams are: %s" %(', '.join(bigrams[-N:])))


from sklearn.model_selection import train_test_split


X = df2['Consumer_complaint'] # Collection of documents
y = df2['Product'] # Target or the labels we want to predict (i.e., the 13 different complaints of products)

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state = 0)

models = [
    #RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0),
    #LinearSVC(),
    #MultinomialNB(),
    LogisticRegression(random_state=0),
]
#
# 5 Cross-validation
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))

entries = []
for model in models:
    model_name = model.__class__.__name__
    accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
    for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))

cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

# print(cv_df)
# Comparison of Model Performance
mean_accuracy = cv_df.groupby('model_name').accuracy.mean()
std_accuracy = cv_df.groupby('model_name').accuracy.std()

acc = pd.concat([mean_accuracy, std_accuracy], axis= 1,
          ignore_index=True)
acc.columns = ['Mean Accuracy', 'Standard deviation']
print(acc)
#
# import seaborn as sns
# plt.figure(figsize=(8,5))
# sns.boxplot(x='model_name', y='accuracy',
#             data=cv_df,
#             color='lightblue',
#             showmeans=True)
# plt.title("MEAN ACCURACY (cv = 5)\n", size=14);
#
# Model Evaluation
print("Model Evaluation")
X_train, X_test, y_train, y_test,indices_train,indices_test = train_test_split(features,
                                                               labels,
                                                               df2.index, test_size=0.25,
                                                               random_state=1)
model = LinearSVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Classification report
print('\t\t\t\tCLASSIFICATIION METRICS\n')
print(metrics.classification_report(y_test, y_pred,
                                    target_names= df2['Product'].unique()))

# conf_mat = confusion_matrix(y_test, y_pred)
# fig, ax = plt.subplots(figsize=(8,8))
# sns.heatmap(conf_mat, annot=True, cmap="Blues", fmt='d',
#             xticklabels=category_id_df.Product.values,
#             yticklabels=category_id_df.Product.values)
# plt.ylabel('Actual')
# plt.xlabel('Predicted')
# plt.title("CONFUSION MATRIX - LinearSVC\n", size=16);
# plt.show();
#
# # #missclassified complaints - cases that were wrongly classified
# # for predicted in category_id_df.category_id:
# #     for actual in category_id_df.category_id:
# #         if predicted != actual and conf_mat[actual, predicted] >= 20:
# #             print("'{}' predicted as '{}' : {} examples.".format(id_to_category[actual],
# #                                                                  id_to_category[predicted],
# #                                                                  conf_mat[actual, predicted]))
# #
# #             display(df2.loc[indices_test[(y_test == actual) & (y_pred == predicted)]][['Product',
# #                                                                                        'Consumer_complaint']])
# #             print('')
# Predictions
print("Predictions")
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state = 0)

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,
                        ngram_range=(1, 2),
                        stop_words='english')

fitted_vectorizer = tfidf.fit(X_train)
tfidf_vectorizer_vectors = fitted_vectorizer.transform(X_train)

model = LinearSVC().fit(tfidf_vectorizer_vectors, y_train)

new_complaint = """I have been enrolled back at XXXX XXXX University in the XX/XX/XXXX. Recently, i have been harassed by \
Navient for the last month. I have faxed in paperwork providing them with everything they needed. And yet I am still getting \
phone calls for payments. Furthermore, Navient is now reporting to the credit bureaus that I am late. At this point, \
Navient needs to get their act together to avoid me taking further action. I have been enrolled the entire time and my \
deferment should be valid with my planned graduation date being the XX/XX/XXXX."""
print(model.predict(fitted_vectorizer.transform([new_complaint])))

print(df2[df2['Consumer_complaint'] == new_complaint])
