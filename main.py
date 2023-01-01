# Flipper Zero SUB-GHZ Playlist Generator
import os

def main():
  path = str(input("Path For The Folder: "))
  name = str(input("SUB-GHZ Playlist Name: "))
  file_end = ".txt"
  playlist = open((f"{name}{file_end}"), "wt")
  playlist.write("# " + name)
  for f in os.listdir(path):
    if f.endswith(".sub"):
      playlist.write("sub: /ext/subghz/" + f + "\n")

main()