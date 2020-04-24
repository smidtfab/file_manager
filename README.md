# file manager
simple script to automatically move files on creation

## Prerequisites
As of now only tested on Ubuntu 18.04

## Development Setup

First, clone repo if you haven't already and navigate into project directory e.g. Documents/file_manager

  ```bash
  $ cd Documents/file_manager
  ```

### To run the file manager stand alone:

0. Initialize and activate a virtualenv (*optional*, as no dependencies are necessary):
  ```bash
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

1. Set path in file_manager.py, where you would like to automatically organize the files:
  ```python
  PATH = '/home/xyz/Downloads/'
  ```

2. Define rules where to move files, otherwise default folders in PATH will be created with format *file_type*_files e.g. py_files:
  ```python
rules =	{
  "pdf": "/home/xyz/Documents/",
  "png": "/home/xyz/Pictures/"
}
  ```

3. Run file_manager.py
 ```bash
 python3 file_manager.py
 ```

### To run the file manager in the background and listen to changes:

0. Initialize and activate a virtualenv (*optional*, as no dependencies are necessary):
  ```bash
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

1. Set path in file_manager.py, where you would like to automatically organize the files:
  ```python
  PATH = '/home/xyz/Downloads/'
  ```

2. Define rules where to move files, otherwise default folders in PATH will be created with format *file_type*_files e.g. py_files:
  ```python
rules =	{
  "pdf": "/home/xyz/Documents/",
  "png": "/home/xyz/Pictures/"
}
  ```
3. Set path in set_listener.sh where to listen to changes (should be the same as in 1.)
 ```bash
 DIR='/home/xyz/Downloads/'
 ```

4. Run shell script
 ```bash
 sh set_listener.sh
 ```
5. Additionally, you might add the script to run automatically on start up
 ```
 Dash > Startup Applications > Add.
 ```
 
## Credits
- base version of the file managment by [Shrestha Tripathi](https://drive.google.com/file/d/15TZSoGk8QexbFlVyXFVW9sj-wg9ROKdc/view)
- [listener implementation](https://askubuntu.com/questions/781799/execution-permission-to-all-files-created-under-a-specific-directory-by-default/781909#781909)
