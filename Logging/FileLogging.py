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
            textFiles = logFile.read([j])
        videoFiles = logFile.read([i])

    #Print out arrays for testing, delete before implementing final code

    for i in range(1):
        for j in range(9):
            print (textFiles[j])
        print (videoFiles.[i])


