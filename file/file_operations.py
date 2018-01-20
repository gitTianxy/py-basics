# encoding=utf-8
"""
file operations other than w/r
---
1. list file in folder: os.walk, os.listdir
2. check exist: os.path.isfile
3. del file: os.remove
"""
import os
import errno


def list_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


def list_files_recursively(root):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(root):
        for fn in filenames:
            f = os.path.join(dirpath, fn)
            if os.path.isfile(f):
                files.append(f)
    return files


def check_exist(fpath):
    return os.path.isfile(fpath)


def del_file(fpath):
    # check before del
    if os.path.isfile(fpath):
        os.remove(fpath)
    else:
        print 'file not exist'
    # without check -- py2
    try:
        os.remove(fpath)
    except OSError as e:
        if e.errno == errno.ENOENT: # errno.ENOENT = no such file or directory
            print 'file not exist'
        else:
            raise
    # without check -- py3
    # with contextlib.suppress(FileNotFoundError):
    #     os.remove(fpath)


if __name__ == '__main__':
    # list file (recursively)
    print '---list file'
    fs = list_files("../data")
    for i in range(0, len(fs)):
        print "%s: %s" % (i, fs[i])
    print '---list file recursively'
    fs = list_files_recursively("../data")
    for i in range(0, len(fs)):
        print "%s: %s" % (i, fs[i])
    # check exist
    print '---check file existence'
    print "is 'data/hello.sh' exist:", check_exist('../data/hello.sh')
    print "is 'data/hello.txt' exist:", check_exist('../data/hello.txt')
    # del file
    print '---delete file'
    del_file('../data/2010.01.01.log')
