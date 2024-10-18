# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:29:38 2022

@author: Christian
"""

from csv import reader

tags = {}

text = ''

regions = ['CA', 'DE', 'FR', 'GB', 'IN', 'US', 'BR']

for r in regions:
    #print(r)
    

            
    with open('{}_youtube_trending_data.csv'.format(r), 'r', encoding="UTF-8") as read_obj:
            csv_reader = reader(read_obj)
            for line in csv_reader:
                if line[7] != "tags":
                    x = line[7].split('|')
                    #print(x)
                    for tag in x:
                        text+=' '+tag
                        '''if tag.lower() in tags:
                            tags[tag.lower()] += 1
                        else:
                            tags[tag.lower()] = 1'''
    
top = []
from wordcloud import WordCloud

# Read the whole text.
text = s

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt


# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(background_color="white",max_words=len(s),max_font_size=40, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()