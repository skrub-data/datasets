

import os
from collections import namedtuple
import re

import pandas as pd

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

DATING_PROFILE_CONFIG = DatasetInfo(
    name='dating_profile',
    urlinfos=(
        UrlInfo(
            url="https://github.com/rudeboybert/JSE_OkCupid/raw/master/profiles.csv.zip",
            filenames=(
                "profile.csv",
            ), uncompress=False
        ),
    ),
    main_file="profile.csv",
    source="https://github.com/rudeboybert/JSE_OkCupid/raw/master/profiles.csv.zip"
)


def get_dating_profile_df(save=True):
    
    df = pd.read_csv('data/profiles/profiles.csv', sep=',', encoding='latin1')
    df.rename(columns={col: re.sub(' ', '_', col).lower() for
              col in df.columns}, inplace=True)
    
    return df
