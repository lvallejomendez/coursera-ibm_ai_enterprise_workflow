#!/usr/bin/evn/python

"""
simple example of a parser
"""

import os
import csv

## specify the files
file_in = os.path.join("..","data","snowfall.csv")
file_out = os.path.join("..","data","snowfall_parsed.csv")

## create an outfile handle (needs to be closed)
fidout = open(file_out,"w")

## use the csv module to read/write
writer = csv.writer(fidout)

## generic parsing function
def parse_line(line):
    
    if line[3] not in ["HI","NC","OR"]:
        return None
    else:
        return line + ['new_data']
    
## for each line in the file read in the first file that you need to reference
with open(file_in) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header_in = reader.__next__()
    writer.writerow(header_in + ["new_column"])
    for line in reader:
        line = parse_line(line)
        if line:
            writer.writerow(line)
   
fidout.close()
print("done parsing")