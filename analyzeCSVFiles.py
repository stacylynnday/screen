# Stacy Day September 2019
# iHeartMedia screen (see Andres Lowres github account)
# Get the list of all csv files in /app/data dir 
# Process csv filelist to:  
#
# 1) Get the average number of fields across all the .csv files 
# 2) Create a csv file that shows the word count of every value
#    of every dataset (dataset being a .csv file)
# 3) Get the total number of rows for all the .csv files


import os
import subprocess
import logging
import traceback
import csv
import chardet
import datetime


## get datasets from git
##bashcommand = "/bin/bash", "-c", "mkdir data && cd data && while read i; do git clone $i; done < <(curl -s https://api.github.com/orgs/datasets/repos?per_page=100 | jq -r '.[].clone_url')"
##subprocess.check_call(bashcommand, shell=True)


# For parts 1), 2), and 3)
# creates the list of csv files
def createFileList(path, extension):
    filelist = []
    for root, dirs_list, files_list in os.walk(path):
        for file_name in files_list:
            if os.path.splitext(file_name)[-1] == extension:
                file_name_path = os.path.join(root, file_name)
                #print(file_name)
                #print(file_name_path)   # This is the full path of the filter file
                filelist.append(file_name_path)
    return filelist

# for part 1)
# calculate average number of fields
def calcAvgNumFields(numbercolumns, filecount):
    avg_num_fields = num_col/file_count
    return avg_num_fields

# helper for part 2)
# set key or append value to new dictionary object:
def add_key_to_dict(values_dict, key):
    if key in values_dict:
        values_dict[key] = values_dict.get(key) + 1
    else:
        values_dict[key] = 1

# for part 2)
# write values_dict to a csv file
def writeDictToFile(filename):
    #with open('value_counts.csv', 'w') as csv_file:
    with open(filename, 'w') as csv_file:
        # writer 
        writer = csv.writer(csv_file)

        # this is the header
        field_names = ['value', 'count']

        writer.writerow(field_names)

        # write each value(key in this case)  and counts(value in this case)    
        for key, value in values_dict.items():    
            values_list=[key,value]
            writer.writerow(values_list) 

# helper for part 3)
# counts the number of lines in a file
def line_count(csv_file):
    return int(subprocess.check_output('wc -l {}'.format(csv_file), shell=True).split()[0])


#
# Get the list of all csv files in /app/data dir and process
#

start_time = datetime.datetime.now()
print("Creating list of csv files in /app/data dir")

# this is the path where you want to search
path ='/app/data'
# this is the extension we want to detect
extension = '.csv'

csv_file_list = createFileList(path, extension)
#print(csv_file_list)
#print(len(csv_file_list))

#
# process csv filelist for 1), 2) and 3) listed at beginning of script 
#

print("Processing .csv files in list")

# create vars we need 
file_count = 0
num_col = 0
total_lines = 0
# put bad/corrupt files here
bad_file_list = []
# this dict holds value and count
values_dict = {}

# for each file in list
for csv_file in csv_file_list:
    # check that csv_file is a file and is not empty
    if (os.path.isfile(csv_file) and os.stat(csv_file).st_size != 0):
        print("Processing csv file: ", csv_file, "at time: ", datetime.datetime.now().time())

        # get encoding by opening as binary
        with open(csv_file, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            charenc = result['encoding']

        # read each cvs file and process
        with open(csv_file, 'r', encoding=charenc, newline='') as csvfile:
            try: 
                # get dialect 
                dialect = csv.Sniffer().sniff(csvfile.read())
                #print("charenc= ", charenc, "delimiter= ", dialect.delimiter) 

                csvfile.seek(0)
                reader = csv.reader(csvfile, dialect)
                
                # do calculations
                num_col += len(next(reader))
                file_count += 1
                total_lines += line_count(file)
                
                # add each column value (here called 'key') to dict of values and counts 
                # (while keeping track of counts)
                for row in reader:
                    for key in row:
                        add_key_to_dict(values_dict, key)

            except BaseException as error:
                print(csv_file, "adding to list of bad files")
                logging.error(traceback.format_exc())
                bad_file_list.append(csv_file)
                continue

# create csv file of all column values in all csv files
# and number of times value has appeared in all csv files
writeDictToFile('value_counts.csv')

# calculate average number of fields
avg_num_fields = calcAvgNumFields(num_col, file_count)

end_time = datetime.datetime.now()

total_time = end_time - start_time
print("Done processing")
print("Total time:", total_time)

# print out answers
print()
print()
print("This is the list of files not used for value_counts.csv file bc they couldn't be read: ", bad_file_list)
print()

# print out answers
print("1.  Average number of fields across all the .csv files is:" , avg_num_fields)
print()

print("2. The csv file that shows the word count of every value of every dataset")
print("   (dataset being a .csv file) is: value_counts.csv")
print("        To copy this file to local machine:")
print("        type \'docker ps -a\' to get container_id")
print("        type \'docker cp <container_id>:/app/data/value_counts.csv .\'")
print()

print("3. The total number of rows for all the .csv files is: ", total_lines)
print()
print()
