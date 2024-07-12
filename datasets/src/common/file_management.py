import contextlib
import gzip
import os
import shutil
import tarfile
import urllib
import zipfile

import numpy as np
import pandas as pd
import requests


def _unzip(file, data_dir='./'):
    z = zipfile.ZipFile(file)
    z.extractall(path=data_dir)
    z.close()


def _untargz(file, data_dir):
    out = os.path.join(data_dir, os.path.splitext(file)[0])
    with gzip.open(file) as gz:
        with open(out, 'wb') as f_out:
            shutil.copyfileobj(gz, f_out, 8192)


def _untar(file, data_dir):
    with contextlib.closing(tarfile.open(file, "r")) as tar:
        tar.extractall(path=data_dir)


def _uncompress_file(file, data_dir, delete_archive):
    filename, ext = os.path.splitext(file)

    with open(file, "rb") as fd:
        header = fd.read(4)

    processed = False

    if zipfile.is_zipfile(file):
        _unzip(file, data_dir)
        processed = True
    elif ext == '.gz' or header.startswith(b'\x1f\x8b'):
        _untargz(file, data_dir)
        processed = True
    if os.path.isfile(file) and tarfile.is_tarfile(file):
        _untar(file, data_dir)
        processed = True

    if delete_archive:
        os.remove(file)

    return processed


def _process_file(file, data_dir, delete_archive=True):
    try:
        if os.path.splitext(file)[1].lower() not in ['.zip', '.tgz', '.tar.gz', '.gz']:
            shutil.move(file, data_dir)
        elif len(file) == 0 or not _uncompress_file(file, data_dir, delete_archive):
            raise IOError(
                "[Uncompress] unknown archive file format: %s" % file)
    except Exception as e:
        print('Error uncompressing file: %s' % e)
        raise


def _download_file(url):
    file = urllib.parse.urlparse(url).path
    file = os.path.basename(file)
    with contextlib.closing(requests.get(url, stream=True)) as r:
        total_length = r.headers.get('Content-Length')
        total_length = 1000 if total_length is None else total_length
        if total_length is not None:
            with open(file, 'wb') as local_file:
                content_iterator = r.iter_content(chunk_size=1024)
                for chunk in content_iterator:
                    if chunk:
                        local_file.write(chunk)
                        local_file.flush()
    return file


def _extract_filenames(config):
    files = []
    for cnf in config.urlinfos:
        if cnf.filenames is not None:
            for file in cnf.filenames:
                files.append(file)
    return files


def _check_dir(config, directory=os.getcwd()):
    download = False
    path = os.path.join(directory, 'data', config.name)
    paths = [os.path.join(path, 'raw'), os.path.join(path, 'output')]
    files = _extract_filenames(config)

    if not os.path.exists(path) or False in [os.path.exists(os.path.join(paths[0], f)) for f in files]:
        shutil.rmtree(path, ignore_errors=True)
        for p in paths:
            os.makedirs(p)
        download = True

    return paths, download


def fetch(config):
    paths, download = _check_dir(config)

    if download:
        urls = [elt.url for elt in config.urlinfos]
        for url in urls:
            file = _download_file(url)
            try:
                _process_file(file, paths[0])
            except Exception as e:
                print(e)

    return paths


def write_df(save, df, path, name):
    save_path = os.path.join(path, name)
    if save:
        df.to_csv(save_path)


def float_to_int(col, index):
    c = []
    for elt in col:
        try:
            c.append(int(elt))
        except ValueError as e:
            c.append(np.nan)
    return pd.Series(c, dtype=np.object, index=index)
