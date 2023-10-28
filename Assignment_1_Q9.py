#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt


# In[9]:


data = pd.read_csv("Q9_a.csv")
data1 = pd.read_csv("Q9_b.csv")


# In[3]:


data


# In[10]:


data1


# In[5]:


data.skew()


# In[11]:


data1.skew()


# In[6]:


data.kurtosis()


# In[12]:


data1.kurtosis()


# In[7]:


plt.hist(data['speed'])


# In[8]:


plt.hist(data['dist'])


# In[13]:


plt.hist(data1['SP'])


# In[15]:


plt.hist(data1['WT'])


# In[ ]:




