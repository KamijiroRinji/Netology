import hashlib


def md5_hash(path):
    md5_hasher = hashlib.md5()
    with open(path, "rb") as file:
        while True:
            word = file.readline()
            if not word:
                break
            md5_hasher.update(word)
            yield md5_hasher.digest()
