#%% Package Import
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#%% File Import, making databases

raw_files = [f"annual_reports/{year}.csv" for year in range(2015,2020)] 
dblist = [pd.read_csv(file) for file in raw_files]
db15,db16,db17,db18,db19 = dblist
years = np.arange(2015,2020)
# %%

fig1, axes1 = plt.subplots(1,5, figsize = (10,3))

for db, ax in zip(dblist,axes1):
    ax.bar(db.filter(like = "Country").squeeze()[:10],db.filter(like = "Score").squeeze()[:10])
    ax.tick_params(axis = 'x', rotation = -90)

# %%
fig2, axes2 = plt.subplots(5)
for i,(db,ax,year) in enumerate(zip(dblist,axes2,years)):
    X = db.filter(like = 'GDP').squeeze()
    Y = db.filter(like = 'Health').squeeze()
    ax.scatter(X,Y, s=1,c='k')
    if i<4:
        ax.sharex(axes2[4])
        ax.sharey(axes2[4])
    if i<4:
        ax.set_xticklabels([])
    ax.set_ylabel(f'{year}')
fig2.suptitle("Happiness to GDP")
fig2.supylabel('Happiness Score')
fig2.supxlabel('GDP')

# %%
