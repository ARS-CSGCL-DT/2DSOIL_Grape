# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:36:59 2019

@author: Tony
"""

import easygui as gui
from os import chdir
import csv

# define function to test for an integer in a string
def is_integer(String):
    try:
        int(String)
        return True
    except ValueError:
        return False

# define function to test for an integer in a string
def is_float(String):
    try:
        float(String)
        return True
    except ValueError:
        return False

# change directory
        
gui.msgbox("This program processes the *.csv file from 2DSOIL_Grape\n into a consolidated 'csv' file", 
           title="Important Message", ok_button="Left Click to proceed to proceed")

path_chdir = gui.diropenbox(msg='Please select folder', title='Select')

chdir(path_chdir)

file_path = gui.fileopenbox('Select file to Open', 'Which file?')

# open input file and read all lines

infile = open(file_path, 'r')

lines = infile.readlines()
titles = []

# split of titles
titles = lines[0].split(",")

# read next line and extrcat starting date
    
numbers = []
numbers = lines[1].split(",")
start_date = float(numbers[0])

# open file to write first date giving data as part of filename

fileName = file_path[:-4]
fileName = fileName + '_' + numbers[0] + ".csv"
outfile = open(fileName, 'w+', newline='')
outwriter = csv.writer(outfile, dialect='excel')

# write out tile and first numbers

outwriter.writerow(titles[0:6])

print(int(numbers[0]), numbers[1], float(numbers[2]), float(numbers[4]), \
      float(numbers[5]), float(numbers[6]))
outwriter.writerow(numbers[0:6])

# iterate of remainder of lines and output evry 10 days

NoL = 1
for lineNo in range(2, len(lines)):
    numbers = []
    numbers = lines[lineNo].split(",")
    date = float(numbers[0])

    if date == start_date:
        NoL += 1
        print(int(numbers[0]), numbers[1], float(numbers[2]), float(numbers[4]), \
              float(numbers[5]), float(numbers[6]), NoL)
        outwriter.writerow(numbers[0:6])
    
    elif date == start_date + 10.0:
        fileName = file_path[:-4]
        fileName = fileName + '_' + numbers[0] + ".csv"
        outfile = open(fileName, 'w+', newline='')
        outwriter = csv.writer(outfile, dialect='excel')
        outwriter.writerow(titles[0:6])

        print(int(numbers[0]), numbers[1], float(numbers[2]), float(numbers[4]), \
              float(numbers[5]), float(numbers[6]), NoL)
        outwriter.writerow(numbers[0:6])
        start_date = date
        NoL = 1
    
    else:
        outfile.close()
# output last NoL number of lines
        
fileName = file_path[:-4]
fileName = fileName + '_' + numbers[0] + ".csv"
outfile = open(fileName, 'w+', newline='')
outwriter = csv.writer(outfile, dialect='excel')
outwriter.writerow(titles[0:6])

for lineNo in range(len(lines)-NoL, len(lines)):
    numbers = []
    numbers = lines[lineNo].split(",")
    print(int(numbers[0]), numbers[1], float(numbers[2]), float(numbers[4]), \
          float(numbers[5]), float(numbers[6]), lineNo)
    outwriter.writerow(numbers[0:6])
    
outfile.close()
    
            
            