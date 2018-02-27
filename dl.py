#########################################################
# This is a program that will download the desired      #
# artists music from a plex server. If you want to      #
# download everything in your music library, then       #
# enter * for the artist then x to start downloading.   #
#                                                       #
# Created by Alex Thoennes                              #
#########################################################

from plexapi.myplex import MyPlexAccount
import os

# sign into your plex account
account = MyPlexAccount('<USERNAME>', '<PASSWORD>')
# now connect to one of your servers
plex = account.resource('<SERVER_NAME>').connect()  # returns a PlexServer instance

# get the music section
music = plex.library.section('Music')
# get all the albums on the plex server
albums = music.searchAlbums()

# list of all the albums you want to download
list = []
# ask the user what albums they want
artName = input("What artist do you want to download?")
# then append it to the list
# if the user enters a * then download every album of every artist in your plex server
# other wise BE SURE TO TYPE THE ARTIST NAME CORRECTLY OR ELSE IT WILL NOT DOWNLOAD
# THEIR TRACKS!!
# finally when you have entered all the artist you want to download, enter x to start the process
while artName != 'x' and artName != '*':
    list.append(artName)
    artName = input("What artist do you want to download?")

# get the size of the list
listSize = len(list)

# now download the albums
for alb in albums:
    # if you want to download all the albums
    if artName == '*':
        # print the artist (parent of the album)
        print(alb.parentTitle)
        # create a directory to hold the albums of the artist (this directory will
        # be named after the artist)
        os.makedirs(os.path.expanduser("~/Desktop/plex music/" + alb.parentTitle), exist_ok=True)
        # get the tracks that belong to this artist
        tracks = alb.tracks()
        for t in tracks:
            # print the album name (the parent of the tracks)
            print("\t"+t.parentTitle)
            # now finally download all the tracks in the album
            alb.download(os.path.expanduser("~/Desktop/plex music/" + alb.parentTitle + "/" + t.parentTitle), True)
            break
    # this is the same thing as the first block just
    # iterating over the list of desired artists
    else:
        for idx in range(0,listSize):
            if alb.parentTitle == list[idx]:
                print(list[idx])
                os.makedirs(os.path.expanduser("~/Desktop/plex music/"+list[idx]), exist_ok=True)

                tracks = alb.tracks()
                for t in tracks:
                    print("\t" + t.parentTitle)
                    alb.download(os.path.expanduser("~/Desktop/plex music/"+list[idx]+"/"+t.parentTitle), True)
                    break
