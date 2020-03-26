# 3rd Party Libraries/Modules/Classes
from multiprocessing import Process
from picamera import PiCamera

# Intellihelm Modules and Classes
from FileManagement import FileManager as FM
from FileManagement import FileTrackingArray as FTA
from FileManagement.classRanking import Ranking
from FileManagement import DateTimeFunctions as DTF
from TextFile import TextFileFunctions as TFF

# Camera 
camera = PiCamera()

# Variables
txtFileName = FM.get_txt_fileName()
videoFileName = FM.get_video_fileName()
fileInfo = FM.file_date_time_info()

#Boolean Controls
txtFileCompleted = False
videoFileCompleted = False
logUptoDate = False
fileNameUptoDate = False
crashDetected = False
videoRecordingInProgress = False

#def load_log():

#def check_fta_full(): 

def txt_file_function():
    while True: 
        if fileNameUptoDate:
            TFF.create(txtFileName)
            TFF.propogate_file(txtFileName)
            txtFileCompleted = True

def video_file_function():
    while crashDetected == False & videoFileCompleted == False:
            if fileNameUptoDate:
                camera.start_recording(videoFileName)
                print("Started recording video file: " + videoFileName)
                sleep(30)
                break
            camera.stop_recording()
            videoRecordingInProgress = False
            print("Stopped recording video file: " + videoFileName)
            videoFileCompleted = True

            
  
def file_management():
    while True:
        if (fileNameUptoDate == False):
            FM.update_fileName()
            fileNameUptoDate = True
            videoFileCompleted = False
        if (videoFileCompleted == True & txtFileCompleted == True):
            fileNameUptoDate = False

for i in range(15):
    print(FTA.current_snippet_video())
    print(FTA.current_snippet_txt())
    FTA.update_ranking()

###########################################################################
#Update File Log - In same while loop as file management, while video is recording
###########################################################################

#main

FM.update_fileName() 
if __name__ == '__main__':
    FMProcess = Process(target = file_management)
    FMProcess.start()
    FMProcess.join()
    videoProcess = Process(target = video_file_function)
    txtFileProcess = Process(target = txt_file_function)
    videoProcess.start()
    videoProcess.join()
    txtFileProcess.start()
    txtFileProcess.join()


