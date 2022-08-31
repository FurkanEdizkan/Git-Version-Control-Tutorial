import random
import os

"""
Create random number and writes into a log file
"""

text_file_path = os.path.join(os.getcwd(), "hash_log.txt")

for i in range(10):
    hash = random.getrandbits(64)
    print("{}. Hash Values == %016x".format(i+i) % hash)

    f = open(str(text_file_path), "a")
    f.write(str(hash)+ "\n")
