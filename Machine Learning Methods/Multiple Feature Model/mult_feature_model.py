import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# create some data
col1 = np.asarray(np.random.choice(10,size=(10)))
col2 = np.asarray(np.random.choice(10,size=(10)))
col3 = np.asarray(np.random.choice(10,size=(10)))
text = ['Some models allow for specialized',
         'efficient parameter search strategies,',
         'outlined below. Two generic approaches',
         'to sampling search candidates are ',
         'provided in scikit-learn: for given values,',
         'GridSearchCV exhaustively considers all',
         'parameter combinations, while RandomizedSearchCV',
         'can sample a given number of candidates',
         ' from a parameter space with a specified distribution.',
         ' After describing these tools we detail best practice applicable to both approaches.']

# create a dataframe from the the created data
df = pd.DataFrame([col1,col2,col3,text]).T
# set column names
df.columns=['col1','col2','col3','text']

tfidf_vec = TfidfVectorizer()
tfidf_dense = tfidf_vec.fit_transform(df['text']).todense()
new_cols = tfidf_vec.get_feature_names()

# remove the text column as the word 'text' may exist in the words and you'll get an error
df = df.drop('text',axis=1)
# join the tfidf values to the existing dataframe
df = df.join(pd.DataFrame(tfidf_dense, columns=new_cols))

print(df)