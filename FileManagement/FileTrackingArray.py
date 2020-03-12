from .classSnippet import Snippet
from .classRanking import Ranking 

fileTrackingArray = []
ranking = Ranking(10, 0, 1)

def current_snippet():
    index = ranking.current
    return fileTrackingArray[index]

def current_snippet_txt():
    return current_snippet().txtFile

def current_snippet_video():
    return current_snippet().videoFile

def update_ranking():
    sizeofArray = len(fileTrackingArray) - 1
    ranking.update_ranking(sizeofArray)

def create_video_placeholder(number: int):
    videoFileName = "videoPlaceHolder" + str(i) + ".txt"
    f = open(videoFileName, 'w')
    f.write("This is a placeholder for a clip that will be recorded in the future")
    f.close()
    return videoFileName

def create_txt_placeholder(number: int):
    txtFileName = "txtPlaceHolder" + str(i) + ".txt"
    f = open(txtFileName, 'w')
    f.write("This is a placeholder for a txt file that will be recorded in the future")
    f.close()
    return txtFileName

for i in range(11):
    txt = create_txt_placeholder(i)
    video = create_video_placeholder(i)
    newSnippet = Snippet(txt, video)
    fileTrackingArray.append(newSnippet)