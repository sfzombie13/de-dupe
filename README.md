# de-dupe
indexes duplicate files for deletion and archiving backups
this is an idea i had due to backing up way too many duplicate files.
it was started  with the help of michael and rob at H@ck-creation, the first hackathon in wv, and is still very much new.
it is eventually going to have a user interface that allows the user to choose where to 
start from, then it will index that location recursively and enter the filenames and their
hashes into a database, and keep the index for future runs. it will allow the user to 
either delete, archive, or manually handle files which are duplicates.  it will allow for 
searches by filename, file contents, or wild card searches.  it will be usable either locally
or remotely.  future additions will include ability to detect partial or corrupted files, web
interface, and the ability to actually perform the backup with an incremental system.
