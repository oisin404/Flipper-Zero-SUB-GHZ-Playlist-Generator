# Flipper Zero SUB-GHZ Playlist Generator
import os


def test():
    # Prompt the user to enter a path for the folder
    folder_path = str(input("Enter the path for the folder: "))
    playlist_name = str(input("Enter a name for the playlist: "))
    # Create the text file in the current working directory
    playlist_file = open((playlist_name + ".txt"), "w")
    # Iterate through the files in the folder
    playlist_file.write("# " + playlist_name + "\n")
    for file in os.listdir(folder_path):
        # Check if the file ends with the ".sub" extension
        if file.endswith(".sub"):
            # Get the full path of the file
            file_path = os.path.join(folder_path, file)
            file_path = file_path.replace("\\", "/")
            file_path = file_path.replace("E:", "ext")
            # Write the name and path of the file to the text file
            playlist_file.write(f"sub: {file_path}\n")
    # Close the text file
    playlist_file.close()
    print(file_path)
    print("Done!")


test()
