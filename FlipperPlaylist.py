# Flipper Zero SUB-GHZ Playlist Generator
import os

def main():
  path = str(input("-------------------------\n---- Path For The Folder: "))
  flipper_path = str(input("-------------------------\n---- Folder Inside Your SUB-GHZ Folder: "))
  name = str(input("-------------------------\n---- SUB-GHZ Playlist Name: "))
  file_end = ".txt"
  playlist = open((f"{name}{file_end}"), "wt")
  playlist.write("# " + name + "\n")
  for f in os.listdir(path):
    if f.endswith(".sub"):
      playlist.write("sub: /ext/subghz/" + flipper_path + "/" + f + "\n")
  print("-------------------------\n---- Playlist Created Successfully!")

main()