# Flipper Zero SUB-GHZ Playlist Generator
import os


def test():
    folder_path = str(input("Enter the path for the folder: "))
    playlist_name = str(input("Enter a name for the playlist: "))
    playlist_file = open((playlist_name + ".txt"), "w")
    playlist_file.write("# " + playlist_name + "\n")
    for roots, dirs, files in os.walk(folder_path, topdown=True):
        if file.endswith(".sub"):
            file_path = os.path.join(folder_path, files)
            file_path = file_path.replace("\\", "/")
            file_path = file_path.replace("E:", "ext")
            playlist_file.write(f"sub: {file_path}\n")

    playlist_file.close()
    print("Done!")


test()
te(f"sub: {file_path}\n")