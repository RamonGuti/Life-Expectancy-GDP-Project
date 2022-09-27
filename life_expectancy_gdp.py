#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Python Modules
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Loaded and previewed data set
df = pd.read_csv("all_data.csv")
df.head()


# In[5]:


df.shape
#96 rows and 4 columns in the data set


# In[7]:


#Checking the different names in the Country column
print(df.Country.unique())


# In[8]:


#Checking the different years covered in the data set
print(df.Year.unique())


# In[9]:


#Changing the Life expectancy at birth column name to be one word like the other columns
df = df.rename({"Life expectancy at birth (years)":"LEABY"}, axis = "columns")
df.head()


# In[11]:


#Plotting GDP to see the data better
plt.figure(figsize=(8,6))
sns.displot(df.GDP, rug = True, kde=False)
plt.xlabel("GDP in Trillions of U.S. Dollars");


# In[ ]:


#The GDP distribution is very right skewed


# In[13]:


#Plotting LEABY to compare it to GDP
plt.figure(figsize=(8,6))
sns.displot(df.LEABY, rug = True, kde=False)
plt.xlabel("Life expectancy at birth (years)");


# In[ ]:


#The distribution of LEABY is very left skewed


# In[15]:


#Calculating average GDP and LEABY by Country
dfMeans = df.drop("Year", axis = 1).groupby("Country").mean().reset_index()
print(dfMeans)


# In[16]:


#Plotting the averages for LEABY
plt.figure(figsize=(8,6))
sns.barplot(x="LEABY", y="Country", data=dfMeans)
plt.xlabel("Life expectancy at birth (years)");


# In[ ]:


#The averages are in the mid to high 70s except Zimbabwe


# In[17]:


#Plotting averages for GDP
plt.figure(figsize=(8,6))
sns.barplot(x="GDP", y="Country", data=dfMeans)
plt.xlabel("GDP in Trillions of U.S. Dollars");


# In[ ]:


#The US has a much higher GDP compared to the rest and Chile and Zimbabwe are very low


# In[18]:


#Plotting GDP in a line chart
plt.figure(figsize=(8,6))
sns.lineplot(x=df.Year, y=df.GDP, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("GDP in Trillions of U.S. Dollars");


# In[ ]:


#US and China had substantial gains between 2000-2015


# In[19]:


#Plotting LEABY in a line chart
plt.figure(figsize=(8,6))
sns.lineplot(x=df.Year, y=df.LEABY, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("Life expectancy at birth (years)");


# In[ ]:


#Zimbabwe has had a big increase after a dip in 2004, the other countries have been steadily increasing


# In[20]:


#Plotting GDP and LEABY in a scatter plot
sns.scatterplot(x=df.LEABY, y=df.GDP, hue=df.Country).legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1);


# In[ ]:


#Zimbabwe has stayed flat while US and China has been increasing at similar slopes


# In[ ]:


#Coclusions
#Looking at all the different charts the overall life expectancy has increased in these countries especially in Zimbabwe
#I can aslo see that GDP has increased in these countries with China having the greatest increase.
#You can see a positive correlation between GDP and life expectancy in these countries.
#The Average life expectancy amongst these countries is in the mid to high 70s but Zimbabwe is in the 50s.
#The life expectancy had a left skew with most observations being on the right side.

