# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:53:48 2022

@author: Christian
"""
#import json
#import plotly.express as px
import matplotlib.pyplot as plt
from csv import reader
import seaborn as sns
from bs4 import BeautifulSoup
import requests

#regions = ['CA', 'DE', 'FR', 'GB', 'IN', 'US', 'BR']
regions = ['GB']

lengths = []
views = []

counter = 0

for r in regions:
            
    with open('{}_youtube_trending_data.csv'.format(r), 'r', encoding="UTF-8") as read_obj:
            csv_reader = reader(read_obj)
            for line in csv_reader:
                    counter+=1
                    if counter < 100:
                        try:
                            vid = line[0]
                            page = requests.get("https://www.youtube.com/watch?v={}".format(vid))
                            soup = BeautifulSoup(page.content, 'html.parser')
                            text = str(soup)
                            start = text.find("lengthSeconds\":\"") + 16
                            end = text.find("\",\"keywords\"")
                            lengths.append(int(text[start:end])/60)
                            views.append(int(line[8])/1000000)
                            print(len(lengths), len(views))
                        except:
                            print('exception')



x = sns.regplot(x=lengths, y=views)

x.set_xlabel("length of video in minutes")
x.set_ylabel("Average Views (millions)")
x.set_title('Avg views vs video length')
plt.show()