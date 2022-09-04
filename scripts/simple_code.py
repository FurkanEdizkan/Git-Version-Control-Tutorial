"""
Random hash generator
"""

import string
import random
import os
import hashlib
import uuid

FILE_PATH = os.path.join(os.getcwd(), "hash_log.txt")

def generate_hash_and_write():
    """ Random hash generator function
    Creates random value and save it into a file
    """
    letters = string.ascii_letters
    seed = ''.join(random.choice(letters) for i in range(10))
    md5_hash = hashlib.md5()
    md5_hash.update(seed.encode('utf-8'))
    new_uuid = uuid.UUID(md5_hash.hexdigest())
    print("Hash Values == %s" % new_uuid)

    with open(str(FILE_PATH), "a", encoding='utf-8') as hash_file:
        hash_file.write(str(new_uuid)+ "\n")

if __name__ == '__main__':
    generate_hash_and_write()
