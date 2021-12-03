friend_file = open("friends.txt", "a")##gonna add text to the file
friend_file.write("\nJose")
"""
if friend_file.readable() == True:
    for friend in friend_file.readlines():
        print(friend)
"""
friend_file.close()
