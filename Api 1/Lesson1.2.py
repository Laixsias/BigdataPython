#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import json


# In[10]:


url = 'https://api.themoviedb.org/3/movie/550?api_key=882d46b4f96ec357b9d220ab6cb1f595'
tokken = '882d46b4f96ec357b9d220ab6cb1f595'
headers = {
    'Content-Type': 'application/json', \
    'Authorization': tokken
}


# In[11]:


b= requests.get(url)


# In[12]:


from pprint import pprint


# In[13]:


pprint(b.text)


# In[16]:


movie = requests.get(url)
movie.json()


# In[18]:


with open ('movie.json','w') as d:
     json.dump(movie.json(), d)


# In[ ]:




