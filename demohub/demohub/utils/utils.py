import os
import os.path as osp
import argparse

import wget
import requests
import hashlib


def structure_file_path(file_path):
    dirname = osp.dirname(file_path)
    filename, suffix = osp.basename(file_path).rsplit('.', 1)
    return dirname, filename, suffix


def download_url(
    url: str, 
    outdir: str,
    filename: str=None,
    exists_ok: bool=True,
    ):
    if not osp.exists(outdir): 
        os.makedirs(outdir, exist_ok=True)
    filename = filename or url.split('/')[-1]
    outpath = osp.join(
        outdir, filename
    )
    if osp.exists(outpath) and exists_ok:
        return outpath
    
    wget.download(url, outpath)
    return outpath


class Range(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __eq__(self, x):
        return self.start <= x <= self.end

    def __str__(self):
        return f"range({self.start}, {self.end})"


class FileTypes(object):

    def __init__(self, *args):
        suffixes = []
        for arg in args:
            suffixes.append(arg)
            suffixes.append(arg.upper())
            suffixes.append(arg.lower())
        self.suffixes = set(suffixes)

    def __eq__(self, x):
        suffix = x.split('.')[-1]
        return suffix in self.suffixes

    def __str__(self):
        return str(self.suffixes)




def str2md5(x: str):
    return hashlib.md5(x.encode('utf-8')).hexdigest()