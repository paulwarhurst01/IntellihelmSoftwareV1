from . import DateTimeFunctions as DTF
from os import remove
from .classSnippet import Snippet
import shutil 

# Propogate a tracking array

fileName = DTF.get_date_and_time(False)

def file_date_time_info():                                            # Date and Time as a string separated by a tab
    return DTF.get_date_and_time(False)

def get_txt_fileName():                                               # Returns the txtFileName with .txt 
    return fileName + ".txt"

def get_video_fileName():                                             # Returns the video file name with . extension
    return fileName + "h264"

def delete_file(fileName: str):                                        # Uses os.remove to delete file
    remove(fileName)

def update_fileName():                                                # Updates the fileName
    fileName = DTF.get_date_and_time(False)

#def copy_snippet(fileName: str):
#    toLocation = ""
#    shutil.copy