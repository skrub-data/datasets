

import os
from collections import namedtuple
import re

import pandas as pd

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

HOUSE_PRICE_CONFIG = DatasetInfo(
    name='house_price',
    urlinfos=(
        UrlInfo(
            url="https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview",
            filenames=(
                "profile.csv",
            ), uncompress=False
        ),
    ),
    main_file="train_test.csv",
    source="https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview"
)


def get_house_price_df(save=True):
    
    df = pd.read_csv('data/house-prices/train.csv')
    df.rename(columns={col: re.sub(' ', '_', col) for
              col in df.columns}, inplace=True)
    
    return df
