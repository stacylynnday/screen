# Get the list of all csv files in root/data dir and process
# process csv filelist to  1) get avg num columns per file, 2)create a csv file off ALL values and counts in all files,
# and 3) get the total number of lines in all files

import os
import subprocess
import sys
import logging
import traceback
import csv
#from collections import Counter
#import pandas as pd

# counts the number of lines in a file
def line_count(file):
    return int(subprocess.check_output('wc -l {}'.format(file), shell=True).split()[0])

# set key or append value to new dictionary object:
def add_key_to_dict(dict, key):
    if key in dict:
        dict[key] = dict.get(key) + 1
    else:
        dict[key] = 1

# Get the list of all csv files in root/data dir and process
# This is the path where you want to search
path ='/app/data'

# this is the extension we want to detect
extension = '.csv'

# filelist will store all csv files
filelist = []

for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
            #print(file_name)
            #print(file_name_path)   # This is the full path of the filter file
            filelist.append(file_name_path)

# process csv filelist to  1) get avg num columns per file, 2)create a csv file off ALL values and counts in all files,
# and 3) get the total number of lines in all files
 
filecount = 0
numcol = 0
totalLines = 0

#print(filelist)
#print(len(filelist))

# put bad/corrupt files here
badfilelist = []
dict = {}

for file in filelist:
    if (os.path.isfile(file) and os.stat(file).st_size != 0):
        #print("processing file: ", file)
        with open(file) as csvfile:
            try: 
                #reader = csv.reader(csvfile)
                
                if (file != "/app/data/geo-nuts-administrative-boundaries/data/NUTS_2013_60M_SH/data/NUTS_AT_2013.csv"):
                    reader = csv.reader(csvfile)
                else:
                    #trying to read this one file!
                    #print("this is the bad file")
                    open(file, encoding = "ISO-8859-1")
                    #reader = csv.reader(csvfile, encoding = "ISO-8859-1")
                    reader = csv.reader(csvfile)

                numcol += len(next(reader))
                filecount += 1
                totalLines += line_count(file)

                for row in reader:
                    for key in row:
                        add_key_to_dict(dict, key)

            except BaseException as error:
                print(file, "adding to list of bad files")
                logging.error(traceback.format_exc())
                badfilelist.append(file)
                continue

avgnumfields = int(round(numcol/filecount))

# write dict to a csv file
with open('valuecounts.csv', 'w') as csvfile:
    fieldnames = ['value', 'count']
   
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    
    for key, value in dict.items():    
        list=[key,value]
        writer.writerow(list) 



print("this is the list of files not used for valuecounts.csv file bc they couldn't be read")
print(badfilelist)

# print out answers
print("Average number of fields is:")
print(avgnumfields)

print("csv file of value, count: valuecounts.csv" )

print("Total number of lines in all csv files:")
print(totalLines)
