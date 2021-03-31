#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA 


# In[2]:


#input trimmed dataset into dataframe
#Relative path used, so will work if file is located in Project folder
df_trim = pd.read_excel(r'./../Project_data\activated_PBMC_trimmed.xlsx')

display(df_trim)

#Trimmed data contains only empai scores for both conditions in each fraction
#fractions include nucleus, cytoplasm, and secreted protein samples


# In[3]:


#This code standardizes the dataset's features onto a unit scale (mean = 0, variance = 1)

conditions = ['activated_nuc_empai','activated_cyt_empai','activated_sec_empai','untreated_nuclei_empai','untreated_cytoplasm_empai','untreated_secreted_empai']


x = df_trim.loc[:, conditions].values

y = df_trim.loc[:,['found']].values

x = StandardScaler().fit_transform(x)


# In[4]:


#This code uses the pca function to reduce dataset dimensionality and cluster

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDF = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDF, df_trim[['found']]], axis =1)


# In[5]:


#This code plots the PCA figure and saves a png to a subfolder named "Figures"

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
found_location = ['both', 'untreated', 'activated']
colors = ['r', 'g', 'b']
for found, color in zip(found_location,colors):
    indicesToKeep = finalDf['found'] == found
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(found_location)
ax.grid() 

fig.savefig('Figures/PCA for Activated PBMCs', bbox='tight')

