#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm


# In[5]:


conf_94 =stats.t.interval(alpha = 0.94, df=1999, loc=200, scale=30/np.sqrt(2000))


# In[6]:


print(np.round(conf_94,0))


# In[7]:


conf_96 =stats.t.interval(alpha = 0.96, df=1999, loc=200, scale=30/np.sqrt(2000))


# In[8]:


print(np.round(conf_96,0))


# In[9]:


conf_98 =stats.t.interval(alpha = 0.98, df=1999, loc=200, scale=30/np.sqrt(2000))


# In[10]:


print(np.round(conf_98,0))


# In[ ]:




