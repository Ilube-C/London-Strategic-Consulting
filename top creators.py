# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:44:04 2022

@author: Christian
"""
from csv import reader

channels = {}

regions = ['CA', 'DE', 'FR', 'GB', 'IN', 'US', 'BR']

for r in regions:
    #print(r)
    

            
    with open('{}_youtube_trending_data.csv'.format(r), 'r', encoding="UTF-8") as read_obj:
            csv_reader = reader(read_obj)
            for line in csv_reader:
                if line[4] != "channelTitle":
                    if line[4] in channels:
                        channels[line[4]] += 1
                    else:
                        channels[line[4]] = 1
    
top = {}

for i in range(100):
    x = max(channels, key=channels.get)
    top[x] = channels[x]
    del channels[x]

for i in top.keys():    
    print(i, top[i])