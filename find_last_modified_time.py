import os
import json
from abs_path import abs_path
from constant import last_modified_json_path
from constant import time_template
last_modified_dic={}

def verify_last_modified():
    if not os.path.isfile(last_modified_json_path):
        with open(last_modified_json_path, 'w') as _file:
            json.dump(time_template, _file, sort_keys=True, indent=4)

def write_last_modified( current_dic ):
    verify_last_modified()
    with open(last_modified_json_path, 'w') as _file:
        json.dump(current_dic, _file, sort_keys=True, indent=4)

def get_last_modified_dic():
    try:
        jfile = open(last_modified_json_path)
    except FileNotFoundError:
        verify_last_modified()
    jfile = open(last_modified_json_path)
    data = json.load(jfile)
    return data
    

# todo keep name genric for files and folder ... say is_modified
def should_check_files_or_folder(path, last_modified_dic):
    verify_last_modified()
    if last_modified_dic.get(path) is None:
        last_modified_dic[path] = [str(os.path.getmtime(path))]
        return True

    if last_modified_dic != str(os.path.getmtime(path)):
        last_modified_dic[path] = [str(os.path.getmtime(path))]
        return True

    return False

def update_last_modified_in_dictionary(path, last_modified_dic):
    verify_last_modified()
    # if last_modified_dic.get(path) is None:
    #     last_modified_dic[path] = [str(os.path.getmtime(path))]
    #     return
    last_modified_dic[path] = [str(os.path.getmtime(path))]
