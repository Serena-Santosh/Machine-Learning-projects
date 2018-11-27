#!/usr/bin/env python
# coding: utf-8

# 
# ## No-Show appointments data analysis
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# Introduction
# 
# The project aims at analyzing the No-show appointments data set and arriving at necessary conclusions.This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment.
#   From the data set, we can see if there is any relation between the gender of the patient and their showing up for the appointment. We can also see whether there is a trend among those who received scholarships. We will also be able to find out whether the patient's age affects their showing up for the appoinment.Conclusions can be arrived at based on the results obtained.

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[6]:



df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# Loads the data set and displays the first 5 rows.

# In[24]:


df.shape


# Returns the number of rows and columns of the data set.

# In[25]:


df.describe()


# Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding null values.

# In[26]:


df.info()


# This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.

# In[27]:


df.tail()


# Displays the last 5 rows of the data set.

# 
# ### Data Cleaning 

# In[28]:


#Cleaning the data before analyzing it.
df.drop(['PatientId', 'AppointmentID', ], axis=1, inplace = True)


# In[29]:


df.head()


# Dropped the 'PatientId' and 'ApointmentID' colums as it was not very much essential for analyzing this data set.

# In[30]:


df.dropna(inplace=True)
df.info()


# Drops null values if any.

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# ### Is there any relation between the age of the patient and their showing up for the appointment?

# In[8]:



sample = sns.stripplot(x="Age", y="No-show", data=df)
plt.title("age vs no-show");


# The graph shows the relationship between age and no-show.From the graph we can see that children below 10 years show up for appoinments more while people above 90 years are unlikely to show up for appoinments.Most of the people between 40-60 years also show up for appoinments.

# ### Is there any trend among those who received scholarships?

# In[39]:


df['Scholarship'].mean()


# finds the mean of scholarship.

# In[4]:


df['Scholarship'].hist(alpha=0.5,  label='scholarship')
df['No-show'].hist(alpha=0.5,  label='no-show')
plt.xlabel("no-show")
plt.ylabel("scholarship")
plt.title("scholarship vs no-show")
plt.legend();


# A histogram which shows the relationship between scholarship and no-show.From the histogram we can see that, people who received scholarships showed up for appointments more when compared to those who did not receive any.

# In[41]:


df.Gender.value_counts()


# A function which gives the count of male and female patients.

# In[43]:


df.query('Gender == "M" ')['Age'].median(), df.query('Gender == "F" ')['Age'].median()


# Returns the median of the ages of male and female patients.

# <a id='conclusions'></a>
# ## Conclusions
# 
# From the results obtained by performing various operations on the data set, we can conclude that, we don't see any trend in the age of the patients and their showing up for the appointment. Those who received scholarship may have shown up for the appointment more.
#    Limitations-Instead of find the mean and replacing the null values with their respective means, we could find some other more effective ways like regression.The data is also not representative of the entire population, making it hard to arrive at a conclusion.
# 

# In[44]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




