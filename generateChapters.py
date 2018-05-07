#!/usr/bin/env
# requires pandoc installed and added to path
# likely doesn't work on Unix systems due to filepaths

# import required modules
import os # lib for operating system operations
import csv # lib for reading csv
# import requests  # lib for reading url as file
import re # regex
import wget # for downloading files
import bs4 # beautifulsoup4 for scraping KC
import subprocess # for calling pandoc from cmd

# method to split camel case string to list
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

# method to replace all items in a dic [item, replace] in text
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# define variables
# update bookpath if repo changes
bookpath = "https://raw.githubusercontent.com/safesoftware/FMETraining/"
branch = "Desktop-Basic-2018/" # update for current branch/version

# download md files and images from other books based on csv structure
with open('chapters.csv', 'r') as csvfile: # open csv
    next(csvfile, None) # skip header
    data = csv.reader(csvfile, delimiter=',') # define csvreader
    for row in data: # iterate on urls to generate chapters
        if not (row[0] + row[9]): # don't worry about sections not in KC
            pass
        elif row[9]: # download process for KC articles
            if not os.path.isfile(row[8]): # check if file already exists
                read = row[8][:-3] + "_read.html"
                write = row[8][:-3] + ".html"
                wget.download(row[9], read) # if not, download it from url
            with open(read, "r", encoding="utf8") as html_read: #
                html_write = open(write, "w", encoding="utf8")
                # extract div
                soup = bs4.BeautifulSoup(html_read, "html.parser")
                div = soup.find("div", {"class": "kbentry post row-fluid"})
                content = div.prettify().replace("=\"/storage/attachments/",
                                                 "=\"https://knowledge.safe.com/storage/attachments/")
                html_write.write(str(content)) # .encode('utf-8')))
            # close files, delete temp
            html_write.close()
            html_read.close()
            os.remove(read)
            # use pandoc to convert to md
            subprocess.run("pandoc " + write + " --extract-media=" +
                           row[8].rsplit('/', 1)[-2]
                           + "/Images --strip-comments -f html-native_divs-native_spans -t markdown -o "
                           + write[:-5] + "_read.md",
                           check=True,
                           shell=True)
            # open md files
            read = row[8][:-3] + "_read.md"
            write = row[8][:-3] + ".md"
            with open(read, "r", encoding="utf8") as md_read: #
                md_write = open(write, "w", encoding="utf8")
                # extract div
                for line in md_read:
                    # md replacements
                    # w_dic = {"![](" + row[5]:"",
                    #          "###":"",
                    #          "Article created with FME Desktop 2018.0":"",
                    #          "[thub.nodes.view.add-new-comment](#)":""
                    #          }
                    # line = replace_all(line, w_dic)
                    # text = replace_all(line, c_dic)
                    line = line.replace("![](" + row[5] + "/", "![](")
                    line = line.replace("###", "")
                    line = line.replace("Article created with FME Desktop 2018.0", "")
                    line = line.replace("[thub.nodes.view.add-new-comment](#)", "")
                    # below here: specific to CAD, should make external file
                    line = line.replace("***Note:** this video was created with FME version 2016.0. Some of the","")
                    line = line.replace("steps might be slightly different, but the overall process is the same.","")
                    line = line.replace("The instructions below are for 2018.0.*","")
                    line = line.replace("tutorial","exercise")
                    line = line.replace("article","exercise")
                    md_write.write(line) # .encode('utf-8')))
            # close files and delete them
            md_write.close()
            os.remove(read)
            md_read.close()
            os.remove(row[8][:-3] + ".html")
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
        # camel case to proper title
        title = ' '.join(camel_case_split(row[6]))
        # write link in summary with proper indentation
        summary.write(2*int(row[3])*" " + "* [" + title[5:-3] + "](" + row[8] + ")\n")

summary.close() # close summary.md
