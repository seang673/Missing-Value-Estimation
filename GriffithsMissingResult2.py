#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[2]:


dataset2 = pd.read_csv('MissingData2.txt', delimiter='\t')


# In[3]:


#Displays first 15 genes
dataset2.head(15)


# In[4]:


missing_value_mark = 1.00000000000000e+99


# In[7]:


#Replace values containing the missing value marker with NaN
dataset2.replace(missing_value_mark, np.nan, inplace=True)


# In[8]:


dataset2.head(15)


# In[10]:


#Create imputer object to fill missing values with mean value of the column
imputer = SimpleImputer(strategy='mean')

#Create variable to fit the imputer on the dataset and transform it
imputed_data = imputer.fit_transform(dataset2)

#Convert imputed data back into a dataframe
data_imputed_d2 = pd.DataFrame(imputed_data, columns=dataset2.columns)


# In[11]:


print(data_imputed_d2)


# In[ ]:




