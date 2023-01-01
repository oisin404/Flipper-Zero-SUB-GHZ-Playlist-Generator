# Flipper Zero SUB-GHZ Playlist Creator
import os

def find_files():
    path = str(input("Path For The Folder: "))
    for files in os.listdir(path):
        if files.endswith(".sub"):
            return files

def write_playlist(files):
    name = str(input("SUB-GHZ Playlist Name: "))
    file_end = ".txt"
    playlist = open((f"{name}{file_end}"), "wt")
    playlist.writelines(files)

write_playlist(find_files())