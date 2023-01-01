import os
name = str(input("SUB-GHZ Playlist Name: "))
path = str(input("Path For The Folder: "))
file_end = ".txt"
playlist = open((f"{name}{file_end}"), "wt")
for f in os.listdir(path):
  if f.endswith(".sub"):
    playlist.write(f + os.linesep)