# For python 2.7

import os # lib for operating system operations
import csv # lib for reading csv
import urllib  # lib for reading url as file

bookpath = "https://raw.githubusercontent.com/safesoftware/FMETraining/" # update if repo changes
branch = "Desktop-Basic-2018/" # update for current branch/version

with open('chapters.csv', 'r') as csvfile: # open csv
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # iterate on urls to generate chapters
        md = urllib.URLopener() # start url reader
        md.retrieve(bookpath + branch + row[0], row[1] + "_read.md") #download md file
        md_read = open(row[1] + "_read.md","r") # open downloaded md file
        md_write = open(row[1],"w") # new temp md file
        for line in md_read: # iterate on md file lines
            line = line.replace("![](./", "![](./" + row[0].split("/")[0] + "/") # replace relative with absolute paths
            md_write.write(line) # print line in temp file
        md_write.close() # close temp file
        md_read.close() # close md file
        os.remove(row[1] + "_read.md")

# In case we need direct link, takes form e.g.:
# https://github.com/safesoftware/FMETraining/raw/master/DesktopBasic1Basics/Images/Img1.01.WhatIsFME.png
