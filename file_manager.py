import os
import glob
from pathlib import PurePath, Path

# path where to organise
PATH = '/home/fabian/Downloads/'

# glob function of glob module to detect all files inside directory
files_list = glob.glob(PATH + "*")

# set up rules for automatic moving of certain file type
rules =	{
  "pdf": "/home/fabian/Documents/",
  "png": "/home/fabian/Pictures/",
  "jpeg": "/home/fabian/Pictures/"
}

# creating a set of extension types inside the folder to avoid duplicate entries
extension_set = set()

# adding each type of extension to the set
for file in files_list:
    if(not Path(file).is_dir()):
        # retrieve file suffix
        extension = PurePath(file).suffix.replace(".", "")
        try:
            # add file suffix to set with unique file suffixes
            extension_set.add(extension)
        except IndexError:
            continue

# function to create directory for each type of extension
def createDirs():
    for dir in extension_set:
        # check if file suffix in rules dictionary
        if dir in rules:
            # do not create sub folder
            print(f'rule for type .{dir} defined and therefore no sub folder will be created ...')
        else:
            # create a new sub folder with file name
            try:
                os.makedirs(PATH + dir + "_files")
                print(f"Created dir for: {dir}")
            except FileExistsError:
                continue

# function to move certain file to a given path
def move_file(old_file_path, new_file_path):
    # check if new_file_path already exists
    if os.path.exists(new_file_path):
        # rename the duplicate file
        converted_path = PurePath(new_file_path)

        # split path into stem e.g. test and duplicate counter __
        path_split = converted_path.stem.split(sep="__")
        name_stem = path_split[0]

        try:
            # get counter and incrementally increase
            rec_count = int(path_split[1])
        except IndexError:
            # except when first run of recursion then set 0
            rec_count = 0
        
        #increase counter for next recursion
        rec_count = rec_count + 1

        # create new file name consisten of parent e.g. /parent, file name e.g. test, counter e.g. 2 and suffix e.g. .py
        adapted_file_path = str(converted_path.parent) + '/' + name_stem + '__' + str(rec_count) + str(converted_path.suffix)

        # run move_file with adapted file_name until file_name is unique
        move_file(old_file_path, adapted_file_path)
    else:
        # stopping condition for recursion when file name is unique
        try:
            # move file from old location to new unique location 
            os.rename(old_file_path, new_file_path)
            print(f"moved file {old_file_path} >> {new_file_path}")
        except (OSError, IndexError):
            # handle errors
            print(f"could not move file {old_file_path} >> {new_file_path}")

# function to move files to respective folders
def arrange():
    for file in files_list:
        if(not Path(file).is_dir()):
            # retrieve file suffix
            fextension = PurePath(file).suffix.replace(".", "")

            # check if file suffix in rules dictionary
            if fextension in rules:
                # move to location specified by rule
                rule_path = rules[fextension] + PurePath(file).name
                move_file(file, rule_path)    
            else:
                # move to default sub folder
                default_path = PATH + fextension + "_files/" + PurePath(file).name
                move_file(file, default_path)

# calling the functions in order
createDirs()
arrange()
