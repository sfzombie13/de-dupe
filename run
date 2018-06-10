# !/usr/bin/python

import os
with open("file", "w") as file:
    for root, dirs, files in os.walk("/"):
        for name in files:
            print(os.path.join(root, name), file=file)
        for name in dirs:
            print(os.path.join(root, name), file=file)
