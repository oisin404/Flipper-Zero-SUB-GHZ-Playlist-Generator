# Flipper Zero SUB-GHZ Playlist Generator
import os


def test():
    folder_path = str(input("Enter the path for the folder: "))
    playlist_name = str(input("Enter a name for the playlist: "))
    playlist_file = open((playlist_name + ".txt"), "w")
    playlist_file.write("# " + playlist_name + "\n")
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            if file.endswith(".sub"):
                file_path = os.path.join(root, file)
                file_path = file_path.replace("\\", "/")
                file_path = file_path.replace("E:", "ext")
                playlist_file.write(f"sub: {file_path}\n")
    playlist_file.close()
    print("Done!")


test()