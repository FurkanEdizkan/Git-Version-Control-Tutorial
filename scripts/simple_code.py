import random
import os

"""
Create random number and writes into a log file
"""

code_folder_path = os.getcwd()
file_path = os.path.join(code_folder_path, "hash_log.txt")

for i in range(5):
    hash = random.getrandbits(128)
    print("Hash Values == %032x", hash)

    f = open(str(file_path), "a")
    f.write(str(hash)+ "\n")
