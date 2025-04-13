import os
import shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        filename, ext = os.path.splitext(file)
        ext = ext.lower()[1:]
        if ext == "":
            continue
        ext_folder = os.path.join(folder_path, ext)
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)
        shutil.move(os.path.join(folder_path, file), os.path.join(ext_folder, file))
    print("Files organized successfully!")

# Change path below to your Downloads or Desktop path
organize_files("F:\FOUR SEMESTER\AI LAB")
# Exampl