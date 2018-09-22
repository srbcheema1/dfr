# dfr
duplicacy-finder-remover.

DFR is a project based on python3.
In this we have used checksums to compare and differentiate two different files in your system.
There might be two different names of same file. So it is generally difficult to locate both as we can’t say if two files are similar just by looking at the content. So we use the concept of checksums of files to check the similarity. If the files are found to be similar we add the data of file into a json file in form a map with key as checksum value and values as locations of duplicacy
