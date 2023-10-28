#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt


# In[43]:


data = pd.read_csv("Q7.csv")


# In[13]:


data


# In[7]:


mean = np.mean(data)


# In[8]:


mean


# In[16]:


df = data[,2:4]


# In[24]:


data.describe()


# In[26]:


data['Points'].mode()


# In[27]:


data['Score'].mode()


# In[28]:


data['Weigh'].mode()


# In[35]:


print(np.var(data))


# In[37]:


print(np.std(data))


# In[41]:


abs(range(data['Score']))


# In[45]:


plt.hist(data['Points'])


# In[46]:


plt.hist(data['Score'])


# In[47]:


plt.hist(data['Weigh'])


# In[49]:


Points_Range=data.Points.max()-data.Points.min()
Points_Range


# In[50]:


Score_Range=data.Score.max()-data.Score.min()
Score_Range


# In[51]:


Weigh_Range=data.Weigh.max()-data.Weigh.min()
Weigh_Range


# In[ ]:




