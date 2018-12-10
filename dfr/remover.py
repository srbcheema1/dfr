import os
import json
import sys
from .find_last_modified_time import get_file_dic
from .find_last_modified_time import verify_file_dic
from .abs_path import abs_path
from .constant import findCheckSumMD5
from .constant import debug
from .Colour import Colour

def locate_file_duplicates(path):
    hash_of_file = findCheckSumMD5(path)
    duplicates = []
    filedic = get_file_dic()

    if(not hash_of_file in filedic):
        return duplcates

    for element in filedic[hash_of_file]:
        if os.path.exists(element): duplicates.append(element)
        elif debug: Colour.print('this doesnot exixts '+ element, Colour.YELLOW)

    return duplicates

def remove_file_duplicates(path):
    duplicates = locate_file_duplicates(path)
    if(len(duplicates) == 0):
        Colour.print('The file, ' + Colour.WHITE + path + Colour.YELLOW
                + ' is not cached please cache this location',Colour.YELLOW)
        return None

    if(len(duplicates) == 1):
        Colour.print('The file has no other duplicates',Colour.GREEN)
        return None

    count = 0
    for element in duplicates:
        if os.path.exists(element):
            count += 1
            Colour.print(Colour.CYAN + str(count) + ": " + Colour.CYAN + element,Colour.GREEN)
        else:
            # remove the useless entry
            pass

    entry_no = input("Choose any one which you wanna delete : ")
    entry_no = [int(x) - 1 for x in entry_no.split()]
    for i in entry_no:
        if(i >= 0 and i < len(duplicates)):
            os.remove(duplicates[i])



def process_dir(path):
    return

def process_path(path):
    path = abs_path(path)
    if not os.path.exists(path):
        Colour.print("Given path : " + path + " is not valid",Colour.RED)
        sys.exit(1)

    if os.path.isfile(path):
        remove_file_duplicates(path)
    if os.path.isdir(path):
        process_dir(path) # to be done


if __name__ == "__main__":
    path = str(input("Enter Path :"))
    process_path(path)
