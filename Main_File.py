import os
import hashlib
import json
from find_last_modified_time import verify_last_modified
from find_last_modified_time import should_check_files_or_folder
from find_last_modified_time import update_last_modified_in_dictionary
from find_last_modified_time import write_last_modified
from find_last_modified_time import get_last_modified_dic
from constant import last_modified_json_path
from abs_path import abs_path

def findCheckSumMD5(fname):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


def find_directory(dir_path,filename,filepath,filedic,ext, last_modified_dic):
    check_folder = should_check_files_or_folder(dir_path, last_modified_dic)
    for fname in os.listdir(dir_path):
        _path = os.path.join(dir_path, fname)
        path = abs_path(_path)
        if os.path.isdir(path): # folder
            print("FOLDER: " + "\t" + path)
            find_directory(path,filename,filepath,filedic,ext, last_modified_dic)
        else: # is a file
            if not check_folder:
                continue
            check_file = should_check_files_or_folder(path, last_modified_dic)
            if not check_file:
                continue
            print("FILE: " + "\t" + path)
            filename.append(fname)
            filepath.append(path)
            key = findCheckSumMD5(path)
            if key in filedic:
                filedic[key].append(path)
            else:
                filedic[key] = [path]
            continue

            if fname.endswith(tuple(ext)):
                # check if same last modified.
                if should_check_files_or_folder(path, last_modified_dic):
                    update_last_modified_in_dictionary(path, last_modified_dic)

def make_dictionary(last_modified_dic):
    cwd = os.getcwd()
    filename = []
    filepath = []
    filedic = {}
    ext = ['.jpeg', '.png', '.jpg', '.txt']

    dir_path = os.path.join(cwd, "test_dir")
    find_directory(dir_path, filename, filepath, filedic, ext, last_modified_dic)
    return filedic


def main():
    print("Starting")
    # if os.path.isfile(last_modified_json_path):
    last_modified_dic = get_last_modified_dic()
    filedic = make_dictionary(last_modified_dic)

    with open('cache.json', 'w') as file:
        json.dump(filedic,file, sort_keys=True, indent=4)
    # print(last_modified_dic)
    write_last_modified(last_modified_dic)

if __name__ == "__main__":
    main()

