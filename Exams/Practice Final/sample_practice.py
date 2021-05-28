#!/usr/bin/env python
# coding: utf-8

# In[2]:


import datascience as ds
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
nyc_class_size_file = "https://data.cityofnewyork.us/api/views/82rt-zc4y/rows.csv"
nyc_table = ds.Table.read_table(nyc_class_size_file)
nyc_labels = nyc_table.labels
CSD,BORO,GRADE = nyc_labels[0:3]
SEATS = nyc_labels[7]
AVE = nyc_labels[-1]
nyc_table = nyc_table.relabeled(GRADE,'GRADE').relabeled(SEATS,'SEATS')
nyc_table = nyc_table.relabeled(AVE,'CLASS SIZE')
nyc_table.show()


# In[ ]:




