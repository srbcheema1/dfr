import os
import json
import sys
from .find_last_modified_time import get_file_dic
from .find_last_modified_time import verify_file_dic
from .abs_path import abs_path
from .constant import findCheckSumMD5
from .constant import debug

def locate_file_duplicates(path):
    count = 0
    hash_of_file = findCheckSumMD5(path)
    duplicates = []
    filedic = get_file_dic()
    for element in filedic[hash_of_file]:
        if os.path.exists(element):
            count += 1
            duplicates.append(element)
            print(str(count) + ": " + element)
        else:
            if debug: print('this doesnot exixts', element)

    entry_no = input("Choose any one which you wanna delete : ")
    entry_no = [int(x) - 1 for x in entry_no.split()]
    for i in entry_no:
        os.remove(duplicates[i])


def process_dir(path):
    return

def finder(path):
    path = abs_path(path)
    if not os.path.exists(path):
        print("please enter a valid path")
        sys.exit(1)
    if os.path.isfile(path):
        locate_file_duplicates(path)
    if os.path.isdir(path):
        process_dir(path) # to be done


if __name__ == "__main__":
    path = str(input("Enter Path :"))
    finder(path)
