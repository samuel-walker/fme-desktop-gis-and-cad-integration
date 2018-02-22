# For python 2.7

import os # lib for operating system operations
import csv # lib for reading csv
import urllib  # lib for reading url as file

# update if repo changes
bookpath = "https://raw.githubusercontent.com/safesoftware/FMETraining/"
branch = "Desktop-Basic-2018/" # update for current branch/version

with open('chapters.csv', 'r') as csvfile: # open csv
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # iterate on urls to generate chapters
        if row[0] == "":
            pass
        else:
            md = urllib.URLopener() # start url reader
            #download md file
            md.retrieve(bookpath + branch + row[7], row[8] + "_read.md")
            md_read = open(row[8] + "_read.md","r") # open downloaded md file
            md_write = open(row[8],"w") # new temp write md file
            for line in md_read: # iterate on md file lines
                # replace relative with absolute paths
                line = line.replace("![](./", "![](../" + row[7].split("/")[0] + "/")
                md_write.write(line) # print new line in temp file
            md_write.close() # close temp file
            md_read.close() # close md file
            os.remove(row[8] + "_read.md")

# generate summary.md
with open('chapters.csv', 'r') as csvfile: # open csv
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # read rows in csv
        # camel case to spaces (not working with file exts)
        title = row[6]
        # title = row[1].re.sub("([a-z])([A-Z])","\g<1> \g<2>",row[1])
        summary = open("SUMMARY.md","w") # open summary.md to write
        summary.write("# Summary \n\n") # write summary title
        # write link in summary with proper indentation
        summary.write(" "*int(row[3]) + "* [" + title[5:-3] + "](" + row[8] + ")\n")

# currently assuming csv can read as int or str
# could also do indent as if elif else statements instead:
# if row[3] = 0
#     indent = 0

# In case I ever need a direct link, it takes form e.g.:
# https://github.com/safesoftware/FMETraining/raw/master/
# DesktopBasic1Basics/Images/Img1.01.WhatIsFME.png
