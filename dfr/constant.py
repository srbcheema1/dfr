from .abs_path import abs_path
import hashlib


last_modified_json_path = abs_path("~/.config/dfr/last_modified.json")
cache_file_path = abs_path("~/.config/dfr/cache.json")
children_json_path = abs_path("~/.config/dfr/children.json")

def findCheckSumMD5(fname):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

last_modified_template = {}
children_template = {}
