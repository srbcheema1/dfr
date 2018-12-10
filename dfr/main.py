import os
import sys
import hashlib
import json
from .args import Args
from .abs_path import abs_path
from .children_file import write_children_json_file
from .children_file import check_all_children_exists
from .children_file import get_children_dic
from .children_file import get_children_dic
from .constant import findCheckSumMD5
from .constant import debug
from .find_last_modified_time import verify_last_modified
from .find_last_modified_time import should_check_files_or_folder
from .find_last_modified_time import write_last_modified
from .find_last_modified_time import write_filedic_in_cache_json
from .find_last_modified_time import get_last_modified_dic, get_file_dic
from .Colour import Colour
from .remover import finder

def write_in_children_dic(dir_path, path, children_dic):
    if children_dic.get(dir_path) is None:
        children_dic[dir_path] = [path]
    elif not path in children_dic[dir_path]:
        children_dic[dir_path].append(path)

def find_directory(dir_path, filedic, last_modified_dic, children_dic):
    if debug: print("FOLDER processing : " + "\t" + dir_path)
    check_folder = should_check_files_or_folder(dir_path, last_modified_dic, filedic)
    if check_folder:
        check_all_children_exists(dir_path, filedic, last_modified_dic, children_dic)
    for fname in os.listdir(dir_path):
        _path = os.path.join(dir_path, fname)
        path = abs_path(_path)
        if os.path.isdir(path): # folder

            find_directory(path,filedic, last_modified_dic, children_dic)
            write_in_children_dic(dir_path, path, children_dic)
        else: # is a file
            if not check_folder:
                continue
            check_file = should_check_files_or_folder(path, last_modified_dic, filedic)
            if not check_file:
                continue
            write_in_children_dic(dir_path, path, children_dic)
            key = findCheckSumMD5(path)
            if key in filedic:
                filedic[key].append(path)
            else:
                filedic[key] = [path]
            continue

def make_dictionary(dir_path):
    # extract old dictionaries
    last_modified_dic = get_last_modified_dic()
    filedic = get_file_dic()
    children_dic = get_children_dic()

    # process directories
    find_directory(dir_path, filedic, last_modified_dic, children_dic)

    # writing updated dictionaries
    write_children_json_file(children_dic)
    write_last_modified(last_modified_dic)
    write_filedic_in_cache_json(filedic)


def main():
    cwd = os.getcwd()
    parser = Args.get_parser()

    if(parser.action == 'cache'):
        if(not parser.loc):
            location = input('Enter a location : ')
        else:
            location = parser.loc
        Colour.print("Caching...",Colour.GREEN)
        path = os.path.join(cwd, location)
        make_dictionary(path)
        Colour.print("Done Caching !",Colour.GREEN)

    if(parser.action == 'find'):
        if(not parser.inp):
            location = input('Enter a location : ')
        else:
            location = parser.inp
        path = os.path.join(cwd, location)
        finder(path)
        # call finder


if __name__ == "__main__":
    main()
