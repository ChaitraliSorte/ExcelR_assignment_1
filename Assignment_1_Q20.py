#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm


# In[15]:


data = pd.read_csv("Cars.csv")


# In[3]:


data


# In[17]:


stats.norm.cdf(38,data.MPG.mean(),data.MPG.std())


# In[18]:


stats.norm.cdf(40,data.MPG.mean(),data.MPG.std())


# In[19]:


stats.norm.cdf(0.50,data.MPG.mean(),data.MPG.std())-stats.norm.cdf(0.20,data.MPG.mean(),data.MPG.std())


# In[ ]:




