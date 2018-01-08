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
    for name in zip_file.namelist():
        try:
            new_name = name.encode('cp437').decode('gbk')
            new_name = os.path.join(d, new_name)
            if os.path.isdir(new_name) and not os.path.exists(new_name):
                os.makedirs(new_name)
            with open(new_name, 'wb') as file:
                file.write(zip_file.read(name))
        except:
            zip_file.extract(name, d)
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
