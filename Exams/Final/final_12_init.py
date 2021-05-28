#!/usr/bin/env python
# coding: utf-8

# In[21]:


import datascience as ds
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
input_file="https://data.cityofnewyork.us/api/views/7yay-m4ae/rows.csv"
input_table = ds.Table.read_table(input_file)
input_labels = input_table.labels
print(input_labels)
input_table


# In[ ]:




