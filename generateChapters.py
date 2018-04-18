#!/usr/bin/env

# import required modules
import os # lib for operating system operations
import csv # lib for reading csv
import requests  # lib for reading url as file
import re # regex
import wget

# define variables
# update bookpath if repo changes
bookpath = "https://raw.githubusercontent.com/safesoftware/FMETraining/"
branch = "Desktop-Basic-2018/" # update for current branch/version

# download md files and images from other books based on csv structure
with open('chapters.csv', 'r') as csvfile: # open csv
    next(csvfile, None) # skip header
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # iterate on urls to generate chapters
        if row[0] == "": # don't worry about sections not in other books
            pass
        else:
            # check if directory exists, make it if not
            if not os.path.exists(row[5]):
                os.makedirs(row[5])
            if not os.path.exists(row[5] + "/Images"):
                os.makedirs(row[5] + "/Images")
            # download md file
            url = bookpath + branch + row[7] # form url
            if not os.path.isfile(row[8]): # check if file already exists
                wget.download(url, row[8]) # if not, download it
            # download images
            with open(row[8], encoding="utf8") as md_read:
                for line in md_read: # iterate on md file lines
                    if "](./" in line: # look for images by line
                        # grab image filename
                        imgsplit = line[6:-2].rsplit('/', 1)[-1]
                        # form url
                        url = bookpath + branch + row[0] + "/Images/" + imgsplit
                        # check if file already exists
                        if not os.path.exists(row[5] + "/Images/" + imgsplit):
                            # if not, download it
                            wget.download(url, row[5] + "/Images/" + imgsplit)

# generate summary.md to create book structure
summary = open("SUMMARY.md","w") # open summary.md to write
summary.write("# Summary \n\n") # write summary title
with open('chapters.csv', 'r') as csvfile: # open csv
    next(csvfile, None) # skip header
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # read rows in csv
        # camel case to spaces (not working with file exts)
        title = re.sub("([a-z])([A-Z])","\g<1> \g<2>",row[6])
        # write link in summary with proper indentation
        summary.write(2*int(row[3])*" " + "* [" + title[5:-3] + "](" + row[8] + ")\n")

summary.close() # close summary.md
