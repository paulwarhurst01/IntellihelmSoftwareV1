import os
import time 
from time import sleep
from datetime import datetime


def load_recent():

    path = "C:\Pi\ELEC_3907\FileName.txt" #need to update address
    
    logFile = open(r"path","r") #opens previously saved logfile

    textFiles = [9]
    videoFiles = [9] # create arrays for both data types
 
    #iterates through text file saving all data values into the two arrays

    for i in range(1):
        for j in range(9):
            if i==0:
                textFiles = logFile.read([j]) #add return for final version
            else:
                videoFiles = logFile.read([j]) #add return for final version

    #Print out arrays for testing, delete before implementing final code

    for i in range(1):
        for j in range(9):
            if i==0:
                print (textFiles[j])
            else:
                print (videoFiles.read[j])

                #comment