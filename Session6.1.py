
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


Names=pd.read_csv('E:/US_Baby_Names_right.csv')


# In[3]:


Names.head()


# ## 1. Delete unnamed columns

# In[7]:


#finding the columns which has unnamed and droping . case is used to check for casesensitive or not
Names=Names.drop(Names.columns[Names.columns.str.contains('unnamed',case = False)],axis = 1)


# In[8]:


Names.head()


# ## 2. Show the distribution of male and female

# In[17]:


byGender =Names.groupby('Gender')
byGender.describe()


# In[27]:


# State wide distribution
Names.groupby('Gender')['State'].value_counts().head()


# ## 3. Show the top 5 most preferred names

# In[73]:


# grouping by Name and max is used to show the max count of that name wise. we can use same as min as well
df=Names.groupby('Name').max()


# In[30]:


# Finaly will apply builtin function to find the n number of laest count base on whihc column.
df.nlargest(5, 'Count')


# ## 4. What is the median name occurence in the dataset

# In[53]:


print(df.median())


# In[88]:


Names.loc[Names['Name'] == 'Elvira'].sort_values(by='State').head()


# ## 5. Distribution of male and female born count by states

# In[97]:


df_mf=Names.groupby('Gender')['State'].value_counts()
df_mf.head()


# In[98]:


df_mf.describe()


# In[99]:


df_mf=Names.groupby('State')['Gender'].value_counts()
df_mf.head()


# In[100]:


df_mf.describe()

