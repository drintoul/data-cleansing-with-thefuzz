#!/usr/bin/env python
# coding: utf-8

# # Fuzzy Matching

# A library to find and correct misspellings

# # Logo for Misspellings

# <p><a href="https://d65im9osfb1r5.cloudfront.net/spellchecker.net/7970248-st-petersburg.png" target="_blank"> <img src="https://d65im9osfb1r5.cloudfront.net/spellchecker.net/7970248-st-petersburg_thumbnail.png" alt="Correct spelling for St. Petersburg" /></a><br/><a href="http://www.spellchecker.net/st.%20petersburg">Correct spelling for St. Petersburg</a> </p>

# In[24]:


get_ipython().system('pip install thefuzz')
from thefuzz import process


# In[32]:


help(process)


# ## List of misspelled values

# In[42]:


city = ['St. petersburgh', 'st. pete', 'st. petersburg', 'saint petersburg', 'at. petersburg', 
        'zt. petersburg', 'xt. petersburg', 'dt. petersburg', 'et. petersburg', 'wt. petersburg',
        'sr. petersburg', 'Sf. petersburg', 'sg. petersburg', 'sy. petersburg', 's6. petersburg', 
        's5. petersburg', 'st. oetersburg', 'st. letersburg', 'st. -etersburg', 'st. 0etersburg', 
        'st. pwtersburg', 'st. pstersburg', 'st. pdtersburg']


# ## Make Pandas DataFrame column from data

# In[43]:


import pandas as pd
df = pd.DataFrame(city, columns=['city'])
df['city'] = df['city'].str.lower()
df.head()


# ## Find Unique Names and explore Distance from 'St. Petersburg'

# In[44]:


unique_types = df['city'].unique()
print (process.extract('st. petersburg', unique_types, limit = len(unique_types)))


# ### Decide on cut-off of 87

# In[46]:


# scores values compared to 'st. petersburg'
matches = process.extract('st. petersburg', df['city'], limit = len(df.city))

for match in matches:
    if match[1] >= 87: # if value in 2nd position of tuple meets threshold...
        df.loc[match[2], 'city'] = 'Saint Petersburg' # find rows where city equals misspelling, correct it


# ### In practice, there will be other values in column so value must be chosen high enough to eliminate

# In[49]:


# matches tuples contain (wrong spelling, distance and row number)
print (matches)


# In[50]:


df


# In[ ]:




