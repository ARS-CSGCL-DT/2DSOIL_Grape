# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:01:23 2019

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
        
gui.msgbox("This program processes the output data file from 2DSOIL_Grape Soil_Out.dat into a consolidated 'csv' file", 
           title="Important Message", ok_button="Left Click to proceed to proceed")

path_chdir = gui.diropenbox(msg='Please select folder', title='Select')

chdir(path_chdir)

file_path = gui.fileopenbox('Select file to Open', 'Which file?')

# define csv file name

ext = file_path[-4:]
csv_path = file_path.replace(ext, '_' + ext[1:4] + '.csv')
# open files

#infile = open(file_path, 'r')
outfile = open(csv_path, 'w+', newline='')
outwriter = csv.writer(outfile, dialect='excel')


# read all the lines

with open(file_path, 'r') as infile:
    line = infile.readline()
    titles = []
    lineNo = 0

    tline = line.split(" ")
    
    for p in range(0, len(tline)):
        if tline[p] != '':
            titles.append(tline[p])
    
    #print(titles)
    
    outwriter.writerow(titles)
    
    for line in infile:
        lineNo += 1
        snum = line.split(" ")
        numbers = []
    
        for i in range(0, len(snum)):
            if snum[i] != '':
                numbers.append(snum[i])
                
        if float(numbers[0]) % 1.0 == 0.0:
            print('Time=', LineNo, numbers[0], numbers[1], numbers[2], numbers[3])
            outwriter.writerow(numbers)
    

outfile.flush()
outfile.close()
infile.close()


