import os
import time 
from time import sleep
from datetime import datetime


def load_recent():

    path = "C:\Pi\fileName.txt" #need to update address
    
    logFile = open(r"path","r")

    textFiles = [9]
    videoFiles = [9]

    for i in range(1):
        for j in range(9):
            textFiles = logFile.read([j])
        videoFiles = logFile.read([i])




