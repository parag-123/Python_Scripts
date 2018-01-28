
# coding: utf-8

# In[1]:

import pandas as pd

full_tsv = pd.read_table('D:/Johnson/Aegis/Python/train.tsv')
print full_tsv #printing only for verification


# In[2]:

train_tsv = full_tsv[:124800] #80% of the data
test_tsv = full_tsv[124800:] #20% of the data


# In[3]:

train1_tsv = train_tsv[['Phrase','Sentiment']] #extracting the relevant fields

tuple_train = [tuple(x) for x in train1_tsv.values] #converting to tuples for feeding to NaiveBayes classifier

print tuple_train #printing only for verification


# In[9]:

import textblob
from textblob.classifiers import NaiveBayesClassifier
fit = NaiveBayesClassifier(tuple_train) #training the model


# In[20]:

for x in test_tsv.Phrase:
    print x, fit.classify(x) #testing the model

