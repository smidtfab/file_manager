#!/bin/bash
DIR="/home/fabian/Downloads/test/"
inotifywait -m -r -e create "$DIR" | while read f

do
    # insert detected
    echo change in folder detected, running python script ...
    # run python file manager
    python3 file_manager.py
done
