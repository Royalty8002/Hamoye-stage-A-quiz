#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir("C:\\Users\\TEST-USMT\\Desktop\\personal.L")


# In[4]:


os.getcwd()


# In[6]:


data = pd.read_excel("FoodBalanceSheets_E_Africa_NOFLAG.xlsx")


# In[7]:


data.head(10)


# In[9]:


data.shape


# In[10]:


data.describe()


# In[15]:


data.columns


# In[19]:


data.tail(20)


# In[20]:


print(data[['Item', 'Element']])


# # Question 11. Total sum of Animal Fat produced in 2014 and 2017 respectively

# In[36]:


AnimalFat = data.groupby('Item').agg(['sum','count'])


# In[38]:


AnimalFat.head(5)


# # Answer = Animal Fat for 2014 = 209460.54 and 2017 = 269617.53

# # Question 12. Mean and standard deviation for 2015

# In[41]:


data.describe()


# # Answer = Mean(2015) = 135.235 and std(2015) = 1603.403

# # Question 13. Total number and percentage of missing data in 2016 to 2 decimal places

# In[43]:


percent_missing = data.isnull().sum() * 100 / len(data)


# In[45]:


percent_missing


# In[47]:


missing = data.isnull().sum()


# In[48]:


missing


# # Answer. Missing_Data(2016) = 1535, percent_missing = 2.52

# In[ ]:





# # Question 14. which year had the highest correlation with Element code

# In[52]:


data.corr()


# # Answer. Highest Correlation by their element code is 0.024457 (2014)

# In[ ]:





# # Question 15. Year with the highest form of import quantity

# In[58]:


Import_quantity = data.groupby('Element').agg(['sum'])


# In[59]:


Import_quantity.head(8)


# # Answer. highest sum of import quantity is year 2017 with sum = 294559.09

# In[ ]:





# # Question 16. Total number of the sum of production in 2014.

# In[61]:


Sum_of_Production = data.groupby('Element').agg(['sum', "count"])


# In[66]:


Sum_of_Production.head(12)


# # Total Production for 2014 = 1931287.75

# In[ ]:





# # Question 17. Element with highest sum in 2018

# In[68]:


Element_with_highest_sum = data.groupby('Element').agg(['sum'])


# In[78]:


Element_with_highest_sum.Y2018


# # Answer = Domestic supply quantity	2161192.10

# In[ ]:





# # Question 18. Element with 3rd lowest sum in 2018

# In[79]:


Element_with_highest_sum = data.groupby('Element').agg(['sum'])


# In[83]:


Element_with_highest_sum.Y2018


# # Answer. SEED is the 3rd lowest sum in 2018 with 25263.14
