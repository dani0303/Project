import os

class main:
    def __init__(self, filename):
        self.filename = filename

    def get_length(self):
        file = open(self.filename, "r")
        return len(file.readlines())##returns the length of the file passed

    def get_audio(self):
        file = open(self.filename, "r")##pass the filename to iterate through txt file to execute youtube command
        for song in file.readlines():##readlines so that it will go to the next line after every iterations
            result = os.system("youtube-dl -x --audio-format mp3 " + song)
            print("Done")


