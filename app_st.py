#!/usr/bin/env python
# coding: utf-8

# Data: Copy the eligibility criteria for MSc Data Science, MCA, MSc Data Analytics and MSc statistics
# programs of CHRIST University from the university website as different txt documents. Perform the
# following tasks using regular expression and python
# 1. Create a dataframe which contains name of the program and list of UG degrees eligible. BSc
# in maths major should be mentioned as BSc(Maths), Statistics major as BSc(Stats) and so on.
# 2. Change/ add the minimum percentage criteria to 70% in all the txt files
# 

# In[1]:


import re
import pandas as pd


# ## Data Analytics

# In[2]:


with open('Data Analytics.txt', 'r') as f:
    contents = f.read()
    
    patternUg = re.compile(r'B[.a-zA-Z\s]+\b')
    matches1 = patternUg.findall(contents)
        
    for i in range(len(matches1)):
        match = matches1[i]
        if(len(match) > 5):
            course = match.split(" ")
            match = course[0] + "(" + course[2] + ")"
            matches1[i] = match
    
    print(matches1)
    print("\n")
    
    percentage = re.findall(r'[0-9]+%', contents)
    if(len(percentage) > 0):
        contents = re.sub(r'[0-9]+%','70%', contents)
        print(contents)


# In[3]:


df1=pd.DataFrame({'Program Name':'Data Analytics',
                 'Eligibility':[matches1]})



# ## Data Science

# In[4]:


with open('Data Science.txt', 'r') as f:
    contents = f.read()
    
    patternBCA = re.compile(r'B[A-Z]+\b')
    patternUg = re.compile(r'[0-9]\.\s*[a-zA-Z]+')
    matches2 = patternUg.findall(contents)
        
    for i in range (len(matches2)):
        match = matches2[i]
        course = re.findall(r'[a-zA-Z]+', match)
        matches2[i] = "Bsc(" + course[0] + ")"
    matches2.append(patternBCA.findall(contents)[0])
    print(matches2)
    
    print("\n")
    
    percentage = re.findall(r'[0-9]+[ %]+', contents)
    if(len(percentage) > 0):
        contents = re.sub(r'[0-9]+[ %]+','70% ', contents)
        print(contents)


# In[5]:


df2=pd.DataFrame({'Program Name':'Data Science',
                 'Eligibility':[matches2]})



# ## Statistics

# In[6]:


with open('Statistics.txt', 'r') as f:
    contents = f.read()
    
    patternStatMaths = re.compile(r'\(([A-Za-z ]+)\).')
    matches3 = patternStatMaths.findall(contents)
    
    match = matches3[0].split(" ")

    stats = "Bsc(" + match[0] + ")"    
    maths = "Bsc(" + match[2] + ")"
    
    matches3 = [stats, maths]
    print(matches3)
    
    print("\n")
    
    percentage = re.findall(r'[0-9]+[ %]+', contents)
    if(len(percentage) > 0):
        contents = re.sub(r'[0-9]+[ %]+','70% ', contents)
        print(contents)


# In[7]:


df3=pd.DataFrame({'Program Name':'Statistics',
                 'Eligibility':[matches3]})



# In[8]:


added_df=(df1.append(df2)).append(df3)



# ## MCA

# In[19]:


with open('Mca.txt', 'r') as f:
    contents = f.read()
    
    patternStatMaths = re.compile(r'\s-\s(.*)$')
    matches4 = patternStatMaths.findall(contents)

    matches4[0]=matches4[0].replace(" or",",")
    
    match = matches4[0].split(", ")

    math = "Bachelors in " + match[0]    
    
    
    matches4 = [math,match[1],match[2]]
    print(matches4)
    
    print("\n")
    
    percentage = re.findall(r'[0-9]+[ %]+', contents)
    if(len(percentage) > 0):
        contents = re.sub(r'[0-9]+[ %]+','70% ', contents)
        print(contents)


# In[25]:


df4=pd.DataFrame({'Program Name':'MCA',
                 'Eligibility':[matches4]})



# In[26]:


final_df = added_df.append(df4)



# In[20]:




# In[21]:


import streamlit as st


# In[22]:


st.title('Courses')


# In[27]:


final_df.to_csv('final_df.csv',index=False)


# In[30]:


@st.cache
def load_data(nrows):
    data = pd.read_csv('final_df.csv',nrows=nrows)
    return data


# In[31]:


data_load_state = st.text('Loading data...')
data = load_data(4)
data_load_state.text('Loading data...done!')
#final_df.drop("Unnamed:0",axis=0,inplace=True)
final_df


# In[32]:


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# In[ ]:




