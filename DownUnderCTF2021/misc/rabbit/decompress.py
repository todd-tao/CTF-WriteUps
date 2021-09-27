import bz2,shutil
import magic
import zipfile
import os
import lzma
import gzip


def unbz2(in_path,):
    with bz2.BZ2File(in_path) as fr, open('123/flag.txt',"wb") as fw:
        shutil.copyfileobj(fr,fw)
    fr.close()
    fw.close()

def unzip(in_path):
    zip_file = zipfile.ZipFile(in_path)
    zip_file.extractall('123')

    zip_file.close()

def unxz(in_path):
    with lzma.open(in_path, 'rb') as fr, open('123/flag.txt',"wb") as fw:
        shutil.copyfileobj(fr,fw)
    fr.close()
    fw.close()

def ungzip(in_path):
    with gzip.GzipFile(in_path, 'rb') as fr, open('123/flag.txt',"wb") as fw:
        shutil.copyfileobj(fr,fw)
    fr.close()
    fw.close()


for i in range(900):
    or_name = '123/flag.txt'
    print(or_name)
    ty = magic.from_file(or_name).split()[0]
    print(ty)
    if ty == 'bzip2':
        new_path = '123/flag.bz2'
        os.rename(or_name, new_path)
        unbz2(new_path)
    elif ty == 'Zip':
        new_path = '123/flag.zip'
        os.rename(or_name, new_path)
        unzip(new_path)
    elif ty == 'XZ':
        new_path = '123/flag.xz'
        os.rename(or_name, new_path)
        unxz(new_path)
    elif ty == 'gzip':
        new_path = '123/flag.gz'
        os.rename(or_name, new_path)
        ungzip(new_path)
    else:
        break

    