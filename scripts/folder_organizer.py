import os
import shutil


for file in os.listdir("folder_path"):
    ext = file.split('.')[-1]
    os.makedirs(ext, exist_ok=True)
    shutil.move(file, ext)
