#!/bin/bash
# checks if a file is valid UTF-8

inputFile="./testFile.txt"

iconv -f UTF-8 "$inputFile" -o /dev/null

if [[ $? -eq 0 ]]
then
    echo "Valid UTF-8 file.";
else
    echo "Invalid UTF-8 file!";
fi