import os
import glob
from pathlib import PurePath, Path

# path where to organise
PATH = '/home/fabian/Downloads/test/'

# glob function of glob module to detect all files inside directory
files_list = glob.glob(PATH + "*")

# set up rules for automatic moving of certain file type
rules =	{
  "pdf": "/home/fabian/Documents/",
  "png": "/home/fabian/Pictures/"
}

# creating a set of extension types inside the folder to avoid duplicate entries
extension_set = set()

# adding each type of extension to the set
for file in files_list:
    print(f"file: {file}")
    if(not Path(file).is_dir()):
        extension = PurePath(file).suffix.replace(".", "")
        print(f"extension: {extension}")
        try:
            extension_set.add(extension)
        except IndexError:
            continue

# function to create directory for each type of extension
def createDirs():
    for dir in extension_set:
        print(f"dir: {dir}")

        # check if file suffix in rules dictionary
        if dir in rules:
            # do not create sub folder
            print('File suffix in rules dictionary and will therefore be skipped')
        else:
            # create a new sub folder with file name
            try:
                os.makedirs(PATH + dir + "_files")
            except FileExistsError:
                continue

# function to move files to respective folders
def arrange():
    for file in files_list:
        if(not Path(file).is_dir()):
            print(f"file: {file}")
            fextension = PurePath(file).suffix.replace(".", "")
            print(f"extension: {fextension}")

            # check if file suffix in rules dictionary
            if fextension in rules:
                # move to default sub folder
                try:
                    rule_path = rules[fextension]
                    os.rename(file, rule_path + PurePath(file).name)
                except (OSError, IndexError):
                    continue
            else:
                # move to default sub folder
                try:
                    os.rename(file, PATH + fextension + "_files/" + PurePath(file).name)
                except (OSError, IndexError):
                    continue

# calling the functions in order
createDirs()
arrange()
