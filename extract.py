import sys
import os
import zipfile
import tarfile


def extract(f, d, t):
    if not os.path.exists(d):
        os.makedirs(d)
    if t == "zip":
        extract_zip(f, d)
    elif t == "rar":
        extract_rar(f, d)
    elif t == "tar.gz":
        extract_tar(f, d, "r:gz")
    elif t == "tar.bz2":
        extract_tar(f, d, "r:bz2")
    elif t == "tar.xz":
        extract_tar(f, d, "r:xz")


def extract_zip(f, d):
    zip_file = zipfile.ZipFile(f)
    zip_file.extractall(d)
    zip_file.close()


def extract_rar(f, d):
    try:
        from unrar import rarfile
    except LookupError:
        print("[Error]Please install unrar library")
        sys.exit(1)
    rar_file = rarfile.RarFile(f)
    rar_file.extractall(d)


def extract_tar(f, d, mode):
    tar_file = tarfile.open(f, mode)
    tar_file.extractall(d)
    tar_file.close()
