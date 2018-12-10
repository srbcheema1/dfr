import os
import json
import hashlib
from .abs_path import abs_path
from .constant import last_modified_json_path
from .constant import last_modified_template
from .constant import findCheckSumMD5
from .constant import cache_file_path
from .files import verify_file
debug = False
last_modified_dic={}

def verify_last_modified():
    if not os.path.isfile(last_modified_json_path):
        verify_file(last_modified_json_path)
        with open(last_modified_json_path, 'w') as _file:
            json.dump(last_modified_template, _file, sort_keys=True, indent=4)

def verify_file_dic():
    if not os.path.isfile(cache_file_path):
        verify_file(cache_file_path)
        with open(cache_file_path, 'w') as _file:
            json.dump(last_modified_template, _file, sort_keys=True, indent=4)


def get_last_modified_dic():
    try:
        jfile = open(last_modified_json_path)
    except FileNotFoundError:
        verify_last_modified()
    jfile = open(last_modified_json_path)
    data = json.load(jfile)
    return data

def get_file_dic():
    try:
        jfile = open(cache_file_path)
    except FileNotFoundError:
        verify_file_dic()
    jfile = open(cache_file_path)
    data = json.load(jfile)
    return data


def write_last_modified( current_dic ):
    verify_last_modified()
    with open(last_modified_json_path, 'w') as _file:
        json.dump(current_dic, _file, sort_keys=True, indent=4)

def write_filedic_in_cache_json(filedic):
    verify_file_dic()
    with open(cache_file_path, 'w') as file:
        json.dump(filedic,file, sort_keys=True, indent=4)


# todo keep name genric for files and folder ... say is_modified
def should_check_files_or_folder(path, last_modified_dic, filedic):
    verify_last_modified()
    if last_modified_dic.get(path) is None:
        if os.path.isdir(path):
            last_modified_dic[path] = [str(os.path.getmtime(path))]
        else:
            last_modified_dic[path] = [str(os.path.getmtime(path)), findCheckSumMD5(path)]
        return True

    if last_modified_dic[path][0] != str(os.path.getmtime(path)):
        if debug: print('hash changed      :','\t',path)
        if os.path.isdir(path):
            last_modified_dic[path] = [str(os.path.getmtime(path))]
        else:
            should_delete_entry_hash = last_modified_dic[path][1]
            delete_duplicate_enrty_in_cache_file(should_delete_entry_hash, path, filedic)
            last_modified_dic[path] = [str(os.path.getmtime(path)), findCheckSumMD5(path)]
        return True

    return False

def delete_duplicate_enrty_in_cache_file(hash, path, filedic):
    if hash in filedic:
        if path in  filedic[hash]:
            filedic[hash].remove(path)

