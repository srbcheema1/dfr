import json
import os
from constant import children_json_path
from constant import children_template

def verify_children_dic():
    if not os.path.isfile(children_json_path):
        with open(children_json_path, 'w') as _file:
            json.dump(children_template, _file, sort_keys=True, indent=4)

def get_children_dic():
    try:
        jfile = open(children_json_path)
    except FileNotFoundError:
        verify_children_dic()
    jfile = open(children_json_path)
    data = json.load(jfile)
    return data


def write_children_json_file(children_dic):
    with open(children_json_path, 'w') as file:
        json.dump(children_dic,file, sort_keys=True, indent=4)

def safe_remove(container,data):
    if type(container) == dict:
        if data in container.keys():
            del container[data]
    if type(container) == list:
        if data in container:
            container.remove(data)
    if type(container) == set:
        if data in container:
            container.remove(data)

rec_count = 1
def _remove_recursively(dir_path, filedic, last_modified_dic, children_dic):
    if not dir_path in children_dic:
        return
    children = children_dic[dir_path]
    print('removeing it : ',dir_path)
    for child in children:
        if not child in last_modified_dic:
            continue
        hash_arr = last_modified_dic[child]
        if len(hash_arr) == 1:  # folder
            _remove_recursively(child, filedic, last_modified_dic, children_dic)
            safe_remove(last_modified_dic, child)
            if dir_path in children_dic.keys():
                safe_remove(children_dic[dir_path], child)
        else:  # file
            hash_file = hash_arr[1]
            safe_remove(last_modified_dic, child)
            if dir_path in children_dic.keys():
                safe_remove(children_dic[dir_path],child)
            if hash_file in filedic.keys():
                safe_remove(filedic[hash_file],child)
    
def check_all_children_exists(dir_path, filedic, last_modified_dic, children_dic):
    if not dir_path in children_dic:
        return
    children = children_dic.get(dir_path,None)
    for child in children:
        if not os.path.exists(child):
            if not child in last_modified_dic:
                continue
            hash_arr = last_modified_dic[child]
            if len(hash_arr) == 1: # folder
                _remove_recursively(child, filedic, last_modified_dic, children_dic)
                safe_remove(last_modified_dic, child)
                if dir_path in children_dic.keys():
                    safe_remove(children_dic[dir_path], child)
                safe_remove(children_dic,child)
            else: #file
                hash_file = hash_arr[1]
                safe_remove(last_modified_dic, child)
                if dir_path in children_dic.keys():
                    safe_remove(children_dic[dir_path], child)
                if hash_file in filedic.keys():
                    safe_remove(filedic[hash_file], child)
                
            