#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd


# In[33]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv("C:\pdata\911.csv")


# In[4]:


df.info()


# In[5]:


df.head(3)


# Top 5 zipcodes for 911 calls

# In[6]:


df['zip'].value_counts().head(5)


# 5 townships (twp) for 911 calls

# In[7]:


df['twp'].value_counts().head(5)


# Unique title codes

# In[8]:


df['title'].nunique()


# Creating new features

# In[9]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# Most common Reason for a 911 call

# In[10]:


df['Reason'].value_counts()


# In[11]:


sns.countplot(x='Reason',data=df,palette='viridis')


# In[12]:


type(df['timeStamp'].iloc[0])


# In[13]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[14]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[15]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[16]:


sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[17]:


byMonth = df.groupby('Month').count()
byMonth.head()


# Count of calls per month

# In[18]:


byMonth['twp'].plot()


# In[19]:


df['Date']=df['timeStamp'].apply(lambda t: t.date())


# Plot of counts of 911 calls Monthly

# In[20]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


#  Reason for the 911 call

# In[21]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[22]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[23]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# Dataframe with columns as hours and index as Day of Week

# In[25]:


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# HeatMap using this new DataFrame

# In[26]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# DataFrame that shows the Month as the column

# In[27]:


dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()


# In[28]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[ ]:




