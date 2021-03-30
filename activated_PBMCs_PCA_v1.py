#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import scipy as sp
from pylab import *
import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import seaborn as sns
import collections
from IPython.display import clear_output
from IPython.display import display
import random


# In[5]:


#input whole dataset into dataframe
df_all = pd.read_excel(r'C:\Users\felic\Dropbox (MIT)\Spring 2021 Classes\20.440\Project\proteome signatures of inflammatory activated primary human peripheral blood moononuclear cells\1-s2.0-S1874391912005428-mmc2 cleaned up.xlsx')

display(df_all)


# In[ ]:


#Break up activated and unactivated into separate dataframes 


# In[33]:


#Histogram of number of proteins identified for untreated, activated only, and both 

options_b = ['both']
both_df = df_all[df_all['found'].isin(options_b)]

#display(both_df)

options_un = ['untreated']
untreated_df = df_all[df_all['found'].isin(options_un)]

#display(untreated_df)

options_act = ['activated'] 
activated_only_df = df_all[df_all['found'].isin(options_act)]
#display(activated_only_df)


height = [len(both_df),len(untreated_df),len(activated_only_df)]
bars = ('Found in both','Untreated', 'Activated')
y_pos = np.arange(len(bars))

fig = plt.figure(figsize=(19.20,10.80))

plt.bar(y_pos, height)
plt.xlabel('Protein Samples', fontsize = 18)
plt.ylabel('Number of Proteins', fontsize = 18)
plt.title('Overlap in Protein Identification in PBMCs', fontsize =20)
plt.xticks(y_pos, bars, fontsize = 18)
plt.yticks(fontsize=18)
plt.show()


# In[35]:



#input trimmed dataset into dataframe
df_trim = pd.read_excel(r'C:\Users\felic\Dropbox (MIT)\Spring 2021 Classes\20.440\Project\proteome signatures of inflammatory activated primary human peripheral blood moononuclear cells\activated_PBMC_trimmed.xlsx')

display(df_trim)

#Trimmed data contains only empai scores for both conditions in each fraction
#fractions include nucleus, cytoplasm, and secreted protein samples


# In[36]:


from sklearn.preprocessing import StandardScaler 

conditions = ['activated_nuc_empai','activated_cyt_empai','activated_sec_empai','untreated_nuclei_empai','untreated_cytoplasm_empai','untreated_secreted_empai']


x = df_trim.loc[:, conditions].values

y = df_trim.loc[:,['found']].values

x = StandardScaler().fit_transform(x)


# In[41]:


from sklearn.decomposition import PCA 

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDF = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])


# In[38]:


finalDf = pd.concat([principalDF, df_trim[['found']]], axis =1)
display(finalDf)


# In[42]:


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

fig.savefig('PCA for Activated PBMCs', bbox='tight')

