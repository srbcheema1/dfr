from abs_path import abs_path
import hashlib

path = "~/PycharmProjects/duplicate_finder/venv/bin/scripts/last_modified.json"
cache_file_path = "/home/choudhary/PycharmProjects/duplicate_finder/venv/bin/scripts/cache.json"
children_json_path = "/home/choudhary/PycharmProjects/duplicate_finder/venv/bin/scripts/children.json"
last_modified_json_path = abs_path(path)

def findCheckSumMD5(fname):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

time_template = {}
children_template = {}