#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[64]:


dataset1 = pd.read_csv('MissingData1.txt', delimiter='\t')


# In[66]:


dataset1.head(15)


# In[67]:


missing_value_mark = 1.00000000000000e+99


# In[68]:


#Replace values containing the missing value marker with NaN
dataset1.replace(missing_value_mark, np.nan, inplace=True)
    


# In[69]:


dataset1.head(15)


# In[70]:


#Create imputer object to fill missing values with median value of the column
imputer = SimpleImputer(strategy='median')


# In[71]:


#Create variable to fit the imputer on the dataset and transform it
imputed_data = imputer.fit_transform(dataset1)


# In[72]:


#Convert imputed data back into a dataframe
data_imputed_d1 = pd.DataFrame(imputed_data, columns=dataset1.columns)


# In[73]:


print(data_imputed_d1)


# In[ ]:




