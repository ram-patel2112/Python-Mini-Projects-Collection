import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
}

def organize_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(directory, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    break

path = input("Enter directory path: ")
organize_files(path)
print("Files organized successfully!")