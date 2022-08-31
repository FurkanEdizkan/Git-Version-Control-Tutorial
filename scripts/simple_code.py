import random
import os

"""
Create random number and writes into a log file
"""

code_folder_path = os.getcwd()
file_path = os.path.join(code_folder_path, "hash_log.txt")

def generate_hash_and_write():
    
    for i in range(5):
        hash = random.getrandbits(32)
        print("Hash Number == {}".format(hash))

        f = open(str(file_path), "a")
        f.write(str(hash)+ "\n")

if __name__ == '__main__':
    generate_hash_and_write()
