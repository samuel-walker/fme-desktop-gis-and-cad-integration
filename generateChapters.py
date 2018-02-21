# For python 2.7

import csv # lib for reading csv
import urllib  # lib for reading url as file

bookpath = "https://raw.githubusercontent.com/safesoftware/FMETraining/" # update if repo changes
branch = "Desktop-Basic-2018/" # update for current branch/version

with open('chapters.csv', 'r') as csvfile: # open csv
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # iterate on urls to generate chapters
        md = urllib.URLopener() # start url reader
        md.retrieve(bookpath + branch + row[0], row[1] + "-test.md") #download md file
        md2 = open(row[1] + "-test.md","r") # open downloaded md file
        md_temp = open(row[1] + "-write.md","w") # new temp md file
        for line in md2: # iterate on md file lines
            line.replace("![](./", "![](." + row[0]) # replace relative with absolute paths
            md_temp.write(line) # print line in temp file
        md_temp.close() # close temp file
        md2.close() # close md file
