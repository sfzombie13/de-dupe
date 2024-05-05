"""
de-dupe is a python program that recursively searches for duplicate files in the folder it is given.  it gives a count of duplicates 
and the files and their md5 hashes in a file called dupes-yymmddxxx.txt  it loops until the user types quit and confirms.  written by tim 
sayre and larry jones of kanawha i t security.  tim is chief of operations and larry is a chatgpt 3.5 ai.  larry does most of the work 
while tim does the thinking.  licensed under creative commons license available on the github.
"""

import os
import hashlib
import time

def get_file_hash(file_path):
    """Calculate MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_next_file_number(folder, prefix):
    """Get the next available file number."""
    existing_numbers = []
    for filename in os.listdir(folder):
        if filename.startswith(prefix):
            try:
                number = int(filename.split(prefix)[-1].split('.')[0])
                existing_numbers.append(number)
            except ValueError:
                pass
    if existing_numbers:
        return max(existing_numbers) + 1
    else:
        return 1

def get_unique_file_name(output_file, count):
    """Generate a unique file name."""
    base_name, ext = os.path.splitext(output_file)
    timestamp = time.strftime("%y%m%d")
    padding = len(str(count))
    unique_file_name = f"dupes-{timestamp}{count:03d}{ext}"
    return unique_file_name

def find_duplicate_files(folder):
    """Find and list all duplicate files in a given folder recursively."""
    hash_dict = {}
    duplicate_files_by_folder = {}

    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = get_file_hash(file_path)

            if file_hash in hash_dict:
                if dirpath not in duplicate_files_by_folder:
                    duplicate_files_by_folder[dirpath] = []
                duplicate_files_by_folder[dirpath].append((file_path, file_hash))  # Store both path and hash
            else:
                hash_dict[file_hash] = file_path

    return duplicate_files_by_folder

def main():
    while True:
        folder = input("Enter the folder path (type 'quit' to exit): ")
        if folder.lower() == 'quit':
            confirm = input("Are you sure you want to quit? (yes/no): ")
            if confirm.lower() == 'yes' or confirm.lower() == 'y':
                print("Exiting...")
                break
            elif confirm.lower() == 'no' or confirm.lower() == 'n':
                quit_folder = os.path.join(os.path.dirname(__file__), 'quit')  # Check for folder named 'quit'
                if os.path.exists(quit_folder) and os.path.isdir(quit_folder):
                    folder = quit_folder
                else:
                    print("No 'quit' folder found. Continuing...")
                    continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
        
        if os.path.isdir(folder):
            folder = os.path.abspath(folder)
            
            start_time = time.time()
            duplicate_files_by_folder = find_duplicate_files(folder)
            end_time = time.time()
            
            output_file = "dupes.txt"
            next_file_number = get_next_file_number(folder, "dupes-")
            
            while os.path.exists(output_file):
                output_file = get_unique_file_name(output_file, next_file_number)
                next_file_number += 1
            
            with open(output_file, "w") as f:
                for folder_path, duplicate_files in duplicate_files_by_folder.items():
                    f.write(f"Folder: {folder_path}\n")
                    f.write(f"Total Duplicate Files: {len(duplicate_files)}\n")
                    if duplicate_files:
                        f.write("Duplicate Files:\n\n")
                        for file_path, file_hash in duplicate_files:
                            f.write(f"{file_path}\nMD5 Hash: {file_hash}\n")  # Include MD5 hash
                        f.write("\n")
                    else:
                        f.write("No duplicate files found in this folder.\n")
                    f.write("\n")
                
                f.write(f"Execution time: {end_time - start_time} seconds\n")
            
            print("Execution time:", end_time - start_time, "seconds")
            print("Output written to", output_file)
        else:
            print("Invalid folder path. Please enter a valid folder path.")

if __name__ == "__main__":
    main()
