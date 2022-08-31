import random
import os

"""
Create random number and writes into a log file
"""

text_file_path = os.path.join(os.getcwd(), "hash_log.txt")

def generate_hash_and_write():
    
    for i in range(5):
        hash = random.getrandbits(64)
        print("{}. Hash Values == %16x".format(i+1) % hash)

    f = open(str(text_file_path), "a")
    f.write(str(hash)+ "\n")

if __name__ == '__main__':
    generate_hash_and_write()

# main changes