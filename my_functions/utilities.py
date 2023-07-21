from os import listdir
from os.path import isfile, join
import csv
import pandas as pd

def files_in_dir(path: str) -> list:
    onlyfiles = ["{}{}".format(path, f) for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

def save_to_cache(df):
    #immediately saving downloads to cache
    name = df["origin"][0]
    length = df.shape[0]
    filename = "data/1-download_cache/{}-{}.pkl".format(name, length)
    df.to_pickle(filename)



