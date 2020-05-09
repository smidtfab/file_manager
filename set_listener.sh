#!/bin/bash
DIR="/home/fabian/Downloads/"
inotifywait -m -r -e create "$DIR" | while read f

do
    # insert detected
    echo change in folder detected, running python script ...
    # wait for file creation (was a problem with pdfs)
    sleep 1.5
    # run python file manager
    python3 file_manager.py
done
