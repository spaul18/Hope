import numpy as np
import pandas as pd 
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline 
import string 
from nltk.corpus import stopwords 

#Removing punctuations  and stopwords
def function_before (mess): 
    nopunc = [] 
    for char in mess : 
        if char not in string.punctuation: 
            nopunc.append(char) 
    nopunc=''.join(nopunc) 
    clean = [] 
    for word in nopunc.split(): 
        word = word.lower() 
        if word not in stopwords.words('english'): 
            clean.append(word) 
    return clean 
    
from sklearn.pipeline import Pipeline  
from sklearn.naive_bayes import MultinomialNB 
from sklearn.feature_extraction.text import CountVectorizer as cv 
from sklearn.feature_extraction.text import TfidfTransformer

#Using the naive bayes classifier we created an NLP model 
pipeline = Pipeline([('bow', cv(analyzer=function_before)), 
                    ('tfidf', TfidfTransformer()), 
                    ('classifier', MultinomialNB()), 
                    ]) 
pipeline.fit(data, emotional_class) 
