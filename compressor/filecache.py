import os

from compressor.conf import settings

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def get_filename_for_key(key):
    output_dir = settings.COMPRESS_FILECACHE_DIR.rstrip('/')
    return os.path.join(output_dir, key)


def filecache_get(key):
    filename = get_filename_for_key(key)
    try:
        with open(filename, 'r') as file:
            return file.read()
    except:
        return None


def filecache_set(key, val):
    filename = get_filename_for_key(key)
    ensure_dir(filename)
    with open(filename, 'w') as file:
        file.write(val)
        file.close()
