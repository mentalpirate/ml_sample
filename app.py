#!/usr/bin/env python
# coding: utf-8

# # python project to learn linear regression using sk learn

# ### importing important library

# In[1]:


import pandas 
from sklearn.linear_model import LinearRegression


# ### reading csv file 

# In[2]:


file = pandas.read_csv("SalaryData.csv")


# ### setting x and y axis put value to predict in x asix always 

# In[3]:


y = file["Salary"]


# In[5]:


x = file["YearsExperience"].values.reshape(30, 1)


# In[6]:


model = LinearRegression()


# In[ ]:


pred = int(input("Enter your years of experience "))


# ### fitting the model using fit function 

# In[7]:


model.fit(x ,y)


# In[11]:


model.coef_


# ### predicting the value 

# In[12]:


model.predict([[2.5]])

