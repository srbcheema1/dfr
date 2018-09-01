import os
import hashlib

def findCheckSumMD5(fname):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

# try not to use globals
textfilename = []
textfilepath = []
imagefilename = []
imagefilepath = []

textdic = {}
imagedic = {}

def find_directory(dir_path):
    for fname in os.listdir(dir_path):
        path = os.path.join(dir_path, fname)
        if os.path.isdir(path):
            print("FOLDER: " + "\t" + path)
            find_directory(path)
        else: # it is file
            print("FILE: " + "\t" + path)
            if fname.endswith('.txt'):
                textfilename.append(fname)
                textfilepath.append(path)
                key = findCheckSumMD5(path)
                if key in textdic:
                    textdic[key].append(path)
                else:
                    textdic[key] = [path]

            elif fname.endswith(('.jpeg', '.png', 'jpg')):
                imagefilename.append(fname)
                imagefilepath.append(path)
                key = findCheckSumMD5(path)
                if key in imagedic:
                    imagedic[key].append(path)
                else:
                    imagedic[key] = [path]


find_directory("/home/choudhary/Music")

print("Text File Dictionary")
for i in textdic:
    print(i, ':', textdic[i])

print("\nImage File Dictionary")
for i in imagedic:
    print(i, ':', imagedic[i])
