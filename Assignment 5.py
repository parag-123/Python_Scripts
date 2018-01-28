# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 00:13:57 2016

@author: HP
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

import pandas as pd

 
fname='train.tsv'
import os

try:
    os.chdir('F:\\Aegis\\Python\\Assignment 5\\train.tsv')

except IOError:
    print "Could not find directory:"    

m_cols = ['PhraseId','SentenceId','Phrase', 'Sentiment']

phrase_data = pd.read_csv(fname, sep='\t',names=m_cols, header=0)

phrase_data.info()
phrase_data.dtypes
phrase_data.describe()
phrase_data.head()
phrase_data['Sentiment'].head()

def phrase_features(phrase):
#    print phrase
    return {'phrase': phrase}

#random.shuffle(phrase_data)

featuresets = [(phrase_features(sentiment[0]), sentiment[1]) for (phrase, sentiment) in phrase_data.iloc[0:150000,(2,3)].iterrows()]
               
train_set, test_set = featuresets[120000:], featuresets[:120000]


classifier=nltk.NaiveBayesClassifier.train(train_set)

#classifier.classify(test_tuples)
count =0;
for sent in test_set:
    print sent
    count+=1
    if(count ==5):
        break
print 'accuracy:', nltk.classify.accuracy(classifier, test_set)
