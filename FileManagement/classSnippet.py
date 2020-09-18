class Snippet(object):
    """Snippet contains two strings, each represent the file location of the respective element."""
    def __init__(self, txtFile, videoFile):
        self.txtFile = txtFile
        self.videoFile = videoFile
        print("New Snippet Initiated")

    def update_text(self, txtFile):                     # Updates txt string
        self.txtFile = txtFile
        print("Snippet txt updated")

    def update_video(self, videoFile):                  # Updates video string
        self.videoFile = videoFile
        print("Snippet video updated")

    def complete_update(self, txtFile, videoFile):      # Updates txt and video strings
        self.txtFile = txtFile
        self.videoFile = videoFile
        print("Snippet completely updated")
        
