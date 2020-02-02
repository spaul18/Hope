#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import csv
get_ipython().run_line_magic('matplotlib', 'inline')


# In[86]:


import csv
with open('survey.csv', 'r') as file:
    reader = csv.reader(file, delimiter = '\t')
    for row in reader:        
        print(row)


# In[87]:


test = pd.read_csv('survey.csv')
print(test.head())


# In[88]:


df = test[['Gender', 'Age', 'mental_health_consequence']]
display(df)


# In[89]:


gender_map = {'male': 'm', 'Male': 'm', 'M': 'm', 'female': 'f', 'Female': 'f', 'F': 'f'}
df['Gender'] = df['Gender'].map(gender_map)
df.head(10)


# In[90]:


df = df.dropna(subset=['Gender'])
df.head(10)


# In[91]:


c1 = df['Gender'].value_counts()


# In[92]:


dfm, dff = df.copy(), df.copy()

dfm = df[df['Gender'] == 'm']
dfm = dfm[:200]

dff = df[df['Gender'] == 'f']
dff = dff[:200]


# In[93]:


df1 = pd.concat([dfm, dff], axis=0)
print('{} \n {}'.format(df1.head(5), df1.tail(5)))


# In[94]:


df_sick = df1[df1['mental_health_consequence'] == 'Yes']
mf_sick = df_sick['Gender'].value_counts()

df_nsick = df1[df1['mental_health_consequence'] == 'No']
mf_nsick = df_nsick['Gender'].value_counts()

print('{} \n {}'.format(mf_sick, mf_nsick))


# In[95]:


df = pd.read_csv('https://query.data.world/s/bs6aqtm2l54gty0ng1vsgw37k')
df_status_gender = df[['Do you currently have a mental health disorder?','What is your gender?']].copy()
df_status_gender.columns = ['Status','Gender']


# In[100]:


# keep on Female and Male (Analysis is easier)
idx1 = (df_status_gender['Gender']=='Female') | (df_status_gender['Gender']=='Male')
df1 = df_status_gender[idx1]

#Create Contigency Table
Cont_Table = pd.crosstab(pd.Categorical(df1.Gender),pd.Categorical(df1.Status))
Cont_Table.index.name = 'Gender'
Cont_Table.columns.name = 'Do you currently have a mental health disorder?'
Cont_Table
Cont_Table.plot.barh()


# In[103]:


idx2 = (df_status_gender['Status']=='Yes') | (df_status_gender['Status']=='No')
df2 = df_status_gender[idx2]

idx3 = (df2['Gender']=='Female') | (df2['Gender']=='Male')
df2 = df2[idx3]

#Create Contigency Table
Cont_Table = pd.crosstab(pd.Categorical(df2.Gender),pd.Categorical(df2.Status))
Cont_Table.index.name = 'Gender'
Cont_Table.columns.name = 'Do you currently have a mental health disorder?'
Cont_Table
Cont_Table.plot.barh()


# In[106]:


df3 = pd.read_csv('prevalence-by-mental-and-substance-use-disorder.csv')
display(df3.head())


# In[108]:


sns.heatmap(df3.corr())


# In[ ]:





# In[ ]:




