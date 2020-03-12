from FileManagement import FileManager as FM
from FileManagement import FileTrackingArray as FTA

# Variables
txtFileName = FM.get_txt_fileName()
videoFileName = FM.get_video_fileName()
fileInfo = FM.file_date_time_info()

for i in range(15):
    print(FTA.current_snippet_video())
    print(FTA.current_snippet_txt())
    FTA.update_ranking()


