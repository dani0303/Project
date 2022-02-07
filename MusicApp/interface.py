import pyfiglet
from test import main

title = pyfiglet.figlet_format("Welcome", font="slant")

print(title)
print("************************************************************************")
print("By Daniel Rodriguez")

filename = input("Please enter the name of the file with the links to the songs: ")

songs = main(filename)
songs.get_audio()
