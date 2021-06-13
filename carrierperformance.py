#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import seaborn as sns

# adjusting seaborn settings

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_style("whitegrid")

# importing fake carrier data
late = pd.read_csv('days_late_example.csv')
ax = sns.boxplot(x="Carrier", y="Days Late", data=late)

# create median values
medians = late.groupby(['Carrier'])['Days Late'].median().values
median_labels = [str(np.round(s, 2)) for s in medians]

# apply median labels
pos = range(len(medians))
for tick,label in zip(pos,ax.get_xticklabels()):
    ax.text(pos[tick], medians[tick] + 0.5, median_labels[tick], 
            horizontalalignment='center', size='x-small', color='w', weight='semibold')

