# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 00:58:05 2022

@author: Christian
"""

#category analysis
import json
#import plotly.express as px
import matplotlib.pyplot as plt
from csv import reader
import seaborn as sns
import pandas
from pandas import DataFrame as df

pandas.set_option('mode.chained_assignment', None)


ids = {}

with open('GB_category_id.json') as json_file:
        data_ = json.load(json_file)
    
        for dic in data_['items']:
            ids[dic["id"]] = [dic["snippet"]["title"]]

#print(ids)



#'JP','KR', 'MX' 'RU',
regions = ['CA', 'DE', 'FR', 'GB', 'IN', 'US', 'BR']

for r in regions:
    print(r)
    
            
    data = []
            
    with open('{}_youtube_trending_data.csv'.format(r), 'r', encoding="UTF-8") as read_obj:
            csv_reader = reader(read_obj)
            for line in csv_reader:
                data.append([line[5],line[8]])
            
    for id_ in ids.keys():
        #print('id is', id_)
        total = 0
        num = 0
        for line in data:
            if line[0] == id_:
                total+=int(line[1])
                num+=1
        #print('total =', total)
        #print('num =', num, '\n')
        if num > 0:
            ids[id_].append(round(((total/num)/1000000), 3))    
                        
               

print(ids)

for x in list(ids.keys()):
    if len(ids[x]) != 8:
        del ids[x]
        
dataset = {ids[x][0]:ids[x][1:] for x in ids.keys()}



d = df(data=dataset, index = regions)
#d.reset_index(level=0, inplace=True)
#d = d.transpose()
d['Regions'] = regions

for r in regions:
    x = sum(d.loc[r][:-1])
    for column in d:
        if column != 'Regions':
            y = d.loc[d.Regions == r, column]*100/x
            d.loc[d.Regions == r, column] = round(y,1)

print(d.head())
print(d.shape)

ax = d.plot(
    x = 'Regions',
    kind = 'barh',
    stacked = True,
    title = 'Categories of Trending Videos by Region',
    mark_right = True,
    width = 0.8)

'''
for c, r in zip(ax.containers, regions):
    print(type(c))
    # Optional: if the segment is small or 0, customize the labels
    labels = d.loc[r][:-1].values.tolist()
    print(labels)
    
    # remove the labels parameter if it's not needed for customized labels
    ax.bar_label(c, labels=labels, label_type='center')'''
    
for c in ax.containers:
    ax.bar_label(c, label_type='center', fontsize = 7.1)
#ax.set_xlabel("Views (millions)")
ax.set_xlabel("Views (% of total)")
ax.set_ylabel('Regions')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
#sns.set()
#plt.rcParams.update({'font.size': 5})


'''
for r in regions:
    x = sns.barplot(d.columns, d.loc[r].values.tolist())
    x.tick_params(labelsize=10)
    x.set_xticklabels(x.get_xticklabels(), rotation=40, ha="right")
    x.set_xlabel("Category")
    x.set_ylabel("Average Views (millions)")
    x.set_title('Avg views per category for videos trending in {}'.format(r))
    plt.show()
#plt.bar(cats, avgs, color = colours)
#plt.rcParams.update({'font.size': 2})

#plt.show()


#vidiq Views per hour vph
#metric we havent discussed today'''