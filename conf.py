import os
from os import listdir, getcwd
from os.path import isfile, join, normpath, basename
import hashlib


#create a file to write to
with open("file", "w") as file:
    for root, dirs, files in os.walk("/"):
        for name in files:
            #write the filenames to the file
            print(os.path.join(root, name), file=file)
            #write the directories to the file
        #for name in dirs:
         #   print(os.path.join(root, name), file=file)
    file.close()
         

#take the file as input to hash the files
#with open("file", "r") as file:
   
def get_files():
    current_path = normpath(getcwd())
    return [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]

    
def get_hashes():
    files = get_files()
    list_of_hashes = []
    for each_file in files:
        hash_md5 = hashlib.md5()
        with open(each_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        list_of_hashes.append('Filename: {}\tHash: {}\n'.format(basename(each_file), hash_md5.hexdigest()))
    return list_of_hashes

def write_hashes():
    hashes = get_hashes()
    with open('list_of_hashes.txt', 'w') as f:
        for md5_hash in hashes:
            f.write(md5_hash)
            
if __name__ == '__main__':
    write_hashes()
