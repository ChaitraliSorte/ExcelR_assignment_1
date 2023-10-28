#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Cars.csv")


# In[4]:


data.head()


# In[5]:


data['MPG'].mean()


# In[6]:


data['MPG'].median()


# In[7]:


data['MPG'].mode()


# In[8]:


data['MPG'].hist()


# In[9]:


sns.distplot(data['MPG'])
plt.grid(True)
plt.show()


# In[10]:


data['MPG'].skew()


# In[11]:


data['MPG'].kurt()


# In[ ]:


#From above plot and values we can say that data is fairly symmetrical, i.e fairly normally distributed.


# In[12]:


data1 = pd.read_csv("wc-at.csv")


# In[13]:


data1.head()


# In[15]:


data1['Waist'].mean()


# In[16]:


data1['AT'].mean()


# In[17]:


data1['Waist'].median()


# In[18]:


data1['AT'].median()


# In[19]:


data1['Waist'].mode()


# In[20]:


data1['AT'].mode()


# In[21]:


data1['Waist'].hist()


# In[22]:


data1['AT'].hist()


# In[23]:


sns.distplot(data1['Waist'])
plt.grid(True)
plt.show()


# In[24]:


sns.distplot(data1['AT'])
plt.grid(True)
plt.show()


# In[ ]:




