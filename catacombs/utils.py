import hashlib

# found here http://www.joelverhagen.com/blog/2011/02/md5-hash-of-file-in-python/
def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()
