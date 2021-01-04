#!/usr/bin/env python
# coding: utf-8

# <img src = "https://global-uploads.webflow.com/5f0d53c042a9ed6288de7f8d/5f6337ae2cfaa10946ceeb06_Hacktiv8%20logo%20horizontal%2001%20black-p-500.png" width = 400>
# <h1 align=center><font size = 5>Hacktiv8 PTP Introduction to Data Science Projects 1 // Publication-Grade Plot</font></h1>

# Title: Hacktiv8 PTP Introduction to Data Science Projects 1: Publication-Grade Plot\
# Last Updated: September 20, 2020\
# Author: Raka Ardhi

# ## Publication-grade Plot Introduction
# 
# The aim of this projects is to introduce you to data visualization with Python as concrete and as consistent as possible. Using what you’ve learned; download the London Crime Dataset from Kaggle. This dataset is a record of crime in major metropolitan areas, such as London, occurs in distinct patterns. This data covers the number of criminal reports by month, LSOA borough, and major/minor category from Jan 2008-Dec 2016.
# 
# This dataset contains:
# 
# * `lsoa_code`: this represents a policing area
# * `borough`: the london borough for which the statistic is related
# * `major_category`: the major crime category
# * `minor_category`: the minor crime category
# * `value`: the count of the crime for that particular borough, in that particular month
# * `year`: the year of the summary statistic
# * `month`: the month of the summary statistic
# 
# Formulate a question and derive a statistical hypothesis test to answer the question. You have to demonstrate that you’re able to make decisions using data in a scientific manner. And the important things, Visualized the data. Examples of questions can be:
# 
# * What is the change in the number of crime incidents from 2011 to 2016?
# * What were the top 3 crimes per borough in 2016?
# 
# Please make sure that you have completed the session for this course, namely Advanced Visualization which is part of this Program.
# 
# Note: You can take a look at Project Rubric below:
# 
# Criteria |	Meet Expectations
# ---|---
# Area Plot |	Mengimplementasikan Area Plot Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik
# Histogram |	Mengimplementasikan Histogram Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Bar Chart | Mengimplementasikan Bar Chart Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Pie Chart |	Mengimplementasikan Pie Chart Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Box Plot |	Mengimplementasikan Box Plot Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Scatter Plot |	Mengimplementasikan Scatter Plot Menggunakan `Matplotlib` Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Word Clouds |	Mengimplementasikan Word Clouds Menggunakan `Wordclouds` Library Dengan Data Yang Relevan Dan Sesuai Dengan Kegunaan Plot/Grafik.
# Folium Maps |	Mengimplementasikan London Maps Menggunakan `Folium`.
# Preprocessing |	Student Melakukan Preproses Dataset Sebelum Menerapkan Visualisasi. | | Apakah Kode Berjalan Tanpa Ada Eror?
# Apakah Kode Berjalan Tanpa Ada Eror? |	Seluruh Kode Berfungsi Dan Dibuat Dengan Benar.
# Area Plot |	Menarik Informasi/Kesimpulan Berdasarkan Area Plot Yang Telah Student Buat
# Histogram |	Menarik Informasi/Kesimpulan Berdasarkan Histogram Yang Telah Student Buat
# Bar Chart |	Menarik Informasi/Kesimpulan Berdasarkan Bar Chart Yang Telah Student Buat
# Pie Chart |	Menarik Informasi/Kesimpulan Berdasarkan Pie Chart Yang Telah Student Buat
# Box Plot |	Menarik Informasi/Kesimpulan Berdasarkan Box Plot Yang Telah Student Buat
# Scatter Plot |	Menarik Informasi/Kesimpulan Berdasarkan Scatter Plot Yang Telah Student Buat
# Overall Analysis |	Menarik Informasi/Kesimpulan Dari Keseluruhan Plot Yang Dapat Menjawab Hipotesis.
# 
# **Focus on "Graded-Function" sections.**
# 
# ------------

# ## Exploring Datasets with *pandas* <a id="0"></a>
# 
# *pandas* is an essential data analysis toolkit for Python. From their [website](http://pandas.pydata.org/):
# >*pandas* is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, **real world** data analysis in Python.
# 
# The course heavily relies on *pandas* for data wrangling, analysis, and visualization. We encourage you to spend some time and  familizare yourself with the *pandas* API Reference: http://pandas.pydata.org/pandas-docs/stable/api.html.

# The first thing we'll do is import two key data analysis modules: *pandas* and **Numpy**.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("C:\\Users\\STAMET FATMAWATI\\Documents\\Python_course\london_crime_by_lsoa.csv")
print ('Data read into a pandas dataframe!')


# In[3]:


# Let's view the top 5 rows of the dataset using the head() function.
df.head(6)


# In[4]:


# We can also veiw the bottom 5 rows of the dataset using the tail() function.
df.tail(3)


# When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe. We can do this by using the `info()` method.

# In[5]:


df.info()


# To get the list of column headers we can call upon the dataframe's `.columns` parameter.

# In[6]:


df.columns.values


# Similarly, to get the list of indicies we use the `.index` parameter.

# In[7]:


df.index.values


# To view the dimensions of the dataframe, we use the `.shape` parameter.

# In[8]:


df.shape


# Let's make one dataset that contains value 1 in value features.

# In[9]:


criminal = df[df['value'] == 1]


# In[10]:


criminal.head()


# In[11]:


criminal.info()


# ## Visualizing Data using Matplotlib<a id="8"></a>
# 
# ### Matplotlib: Standard Python Visualization Library<a id="10"></a>
# 
# The primary plotting library we will explore in the course is [Matplotlib](http://matplotlib.org/).  As mentioned on their website: 
# >Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.
# 
# If you are aspiring to create impactful visualization with python, Matplotlib is an essential tool to have at your disposal.
# 
# **Matplotlib.Pyplot**
# 
# One of the core aspects of Matplotlib is `matplotlib.pyplot`.
# 
# Let's start by importing `Matplotlib` and `Matplotlib.pyplot` as follows:

# In[12]:


# we are using the inline backend
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[13]:


mpl.style.use(['ggplot']) # optional: for ggplot-like style


# In[14]:


df1 = criminal.pivot_table(index='year', columns='minor_category', values='value', aggfunc=sum)
df1


# In[15]:


df1.drop(df1.columns[8:33], axis=1, inplace=True)
#df1.drop(['Counted per Victim'], axis=1, inplace=True)
df1


# ## Area Pots (Series/Dataframe) <a id="12"></a>
# 
# **What is a line plot and why use it?**
# 
# An Area chart or area plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields. Use line plot when you have a continuous data set. These are best suited for trend-based visualizations of data over a period of time.
# 
# **Questions:**
# 
# (Line of Theft and Handling of major category in criminal)

# In[16]:


# Write your function below

# Graded-Funtion Begin (~1 Lines)

# Graded-Funtion End
df1.plot(kind='line', figsize=(8,5))

plt.title('Minor Category') # add a title to the area plot
plt.ylabel('Number of Minor Category') # add y-label
plt.xlabel('Year') # add x-label


#plt.show()


# In[17]:


df1['Assault with Injury'].plot(label='Assault with Injury', legend=True)
df1['Burglary in Other Buildings'].plot(label='Burglary in Other Buildings', legend=True)

plt.title(' Minor Category') # add a title to the area plot
plt.ylabel('Number of Minor Category') # add y-label
plt.xlabel('Year') # add x-label


# **Insight:**
# 
# (Make your own Insight)

# ## Histogram
# 
# A histogram is a way of representing the frequency distribution of numeric dataset. The way it works is it partitions the x-axis into bins, assigns each data point in our dataset to a bin, and then counts the number of data points that have been assigned to each bin. So the y-axis is the frequency or the number of data points in each bin. Note that we can change the bin size and usually one needs to tweak it so that the distribution is displayed nicely.
# 
# **Question:**
# 
# (Make your own questions)

# **Insight:**
# 
# (Make your own Insight)

# In[18]:


df1.plot(kind='hist', figsize=(10,5))

plt.title('Minor Category') # add a title to the area plot
plt.ylabel('Number of Minor Category') # add y-label
plt.xlabel('Year') # add x-label


# ## Bar Charts (Dataframe) <a id="10"></a>
# 
# A bar plot is a way of representing data where the *length* of the bars represents the magnitude/size of the feature/variable. Bar graphs usually represent numerical and categorical variables grouped in intervals. 
# 
# To create a bar plot, we can pass one of two arguments via `kind` parameter in `plot()`:
# 
# * `kind=bar` creates a *vertical* bar plot
# * `kind=barh` creates a *horizontal* bar plot
# 
# **Question:**
# 
# (Histogram of Minor Category of Criminal)

# In[19]:


# Write your function below

# Graded-Funtion Begin (~1 Lines)

# Graded-Funtion End
df1.plot(kind='bar', figsize=(8,5))

plt.title('Histogram of Minor Category') # add a title to the area plot
plt.ylabel('Number of Minor Category') # add y-label
plt.xlabel('Year') # add x-label


plt.show()


# In[20]:


df2=df1['Assault with Injury']
df2.plot(kind='bar', figsize=(10,6))

plt.title('Histogram of Assault with Injury') # add a title to the area plot
plt.ylabel('Number of Assault with Injury') # add y-label
plt.xlabel('Year') # add x-label


# **Insight:**
# 
# (Make your own Insight)

# ## Pie Charts <a id="6"></a>
# 
# A `pie chart` is a circualr graphic that displays numeric proportions by dividing a circle (or pie) into proportional slices. You are most likely already familiar with pie charts as it is widely used in business and media. We can create pie charts in Matplotlib by passing in the `kind=pie` keyword.
# 
# **Question:**
# 
# (Make your own questions)

# In[21]:


df1['Total']=df1.sum(axis=1)
df1


# In[22]:


# Write your function below

# ratio for each continent with which to offset each wedge.
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink','red','blue','brown']
explode_list = [0, 0, 0, 0, 0, 0, 0, 0, 0.1]

df1['Total'].plot(kind='pie',
                  figsize=(10,6),
                  autopct='%1.1f%%',
                  startangle=90,
                  shadow=True,
                  labels=None,
                  pctdistance=1.12,
                  colors=colors_list,
                  explode=explode_list
                 )


# scale the title up by 12% to match pctdistance
plt.title('Total of Minor of Category', y=1.12)

plt.axis('equal')

# add legend
plt.legend(labels=df1.index, loc='upper right')

plt.show()


# **Insight:**
# 
# (Make your own Insight)

# ## Box Plots <a id="8"></a>
# 
# A `box plot` is a way of statistically representing the *distribution* of the data through five main dimensions: 
# 
# - **Minimun:** Smallest number in the dataset.
# - **First quartile:** Middle number between the `minimum` and the `median`.
# - **Second quartile (Median):** Middle number of the (sorted) dataset.
# - **Third quartile:** Middle number between `median` and `maximum`.
# - **Maximum:** Highest number in the dataset.
# 
# **Question:**
# 
# (Make your own questions)

# In[23]:


# Write your function below

# Graded-Funtion Begin (~1 Lines)
df3 = df1.loc[:,['Assault with Injury','Common Assault', 'Burglary in a Dwelling']]
df3.plot(kind='box', figsize=(8,6))
# Graded-Funtion End

#plt.title('Title')
#plt.ylabel('yLabel')

#plt.show()


# **Insight:**
# 
# (Make your own Insight)

# ## Scatter Plots <a id="10"></a>
# 
# A `scatter plot` (2D) is a useful method of comparing variables against each other. `Scatter` plots look similar to `line plots` in that they both map independent and dependent variables on a 2D graph. While the datapoints are connected together by a line in a line plot, they are not connected in a scatter plot. The data in a scatter plot is considered to express a trend. With further analysis using tools like regression, we can mathematically calculate this relationship and use it to predict trends outside the dataset.
# 
# **Question:**
# 
# (Make your own questions)

# In[24]:


df1.reset_index(inplace=True)
df1


# In[25]:


# Write your function below

# Graded-Funtion Begin (~1 Lines)

df1.plot(kind='scatter', x='year', y='Total', figsize=(10, 6), color='darkblue')
# Graded-Funtion End

plt.title('Total of Minor Category')
plt.xlabel('Year')
plt.ylabel('Number of Total')

plt.show()


# ## Word Clouds <a id="8"></a>
# 
# 
# `Word` clouds (also known as text clouds or tag clouds) work in a simple way: the more a specific word appears in a source of textual data (such as a speech, blog post, or database), the bigger and bolder it appears in the word cloud.

# In[26]:


# install wordcloud
# !conda install -c conda-forge wordcloud --yes

get_ipython().system('pip install wordcloud')

# import package and its set of stopwords
from wordcloud import WordCloud, STOPWORDS

print ('Wordcloud is installed and imported!')


# In[27]:


alice_novel = open('C:\\Users\\STAMET FATMAWATI\\Documents\\Python_course\\stamet.txt', 'r').read()


# In[28]:


stopwords = set(STOPWORDS)


# In[29]:


# instantiate a word cloud object
alice = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

# generate the word cloud
alice.generate(alice_novel)


# In[30]:


# Write your function below
fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)

# Graded-Funtion Begin (~1 Lines)
plt.imshow(alice, interpolation='bilinear')
# Graded-Funtion End

plt.axis('off')
plt.show()


# ## Folium
# 
# Folium is a powerful Python library that helps you create several types of Leaflet maps. The fact that the Folium results are interactive makes this library very useful for dashboard building.
# 
# From the official Folium documentation page:
# 
# > Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium.
# 
# > Folium makes it easy to visualize data that's been manipulated in Python on an interactive Leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map.
# 
# > The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. Folium supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes.

# In[31]:


#!conda install -c conda-forge folium=0.5.0 --yes
get_ipython().system('pip install folium')
import folium

print('Folium installed and imported!')


# In[32]:


# define the world map
world_map = folium.Map()

# display world map
world_map


# In[33]:


# define the world map centered around London with a low zoom level 8

# Write your function below

# Graded-Funtion Begin (~1 Lines)

# Graded-Funtion End

# display world map
world = folium.Map(location=[-3.47,102.15], zoom_start=8)
world


# Thanks For Completing This Labs!
