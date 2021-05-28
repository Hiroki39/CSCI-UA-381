#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datascience as ds
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


top = ds.Table.read_table('data/' + 'top_movies.csv')
top


# In[4]:


movies_and_studios = top.select('Title', 'Studio')
movies_and_studios.group('Studio')


# In[11]:


studio_distribution = movies_and_studios.group('Studio')
studio_distribution.sort('count', descending=True).barh('Studio')


# In[5]:


movies_and_years = top.select('Title', 'Year')
movies_and_years.group('Year').sort('count', descending=True).barh('Year')


# In[6]:


movies_and_years.group('Year').sort('count', descending=True).plot('Year')


# In[ ]:




