#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm


# In[5]:


print('Z score for 90% Conifidence Interval =',np.round(stats.norm.ppf(.05),4)) 


# In[6]:


print('Z score for 94% Conifidence Interval =',np.round(stats.norm.ppf(.03),4)) 


# In[7]:


print('Z score for 60% Conifidence Interval =',np.round(stats.norm.ppf(.2),4))


# In[8]:


print('T score for 95% Confidence Interval =',np.round(stats.t.ppf(0.025,df=24),4)) 


# In[9]:


print('T score for 94% Confidence Inteval =',np.round(stats.t.ppf(0.03,df=24),4))


# In[10]:


print('T score for 95% Confidence Interval =',np.round(stats.t.ppf(0.005,df=24),4)) 

