import os
from collections import namedtuple

import pandas as pd

from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

BEER_REVIEWS_CONFIG = DatasetInfo(
    name='beer_reviews',
    urlinfos=(
        UrlInfo(
            url="https://query.data.world/s/vmplvzsgmb2gdcomuhwktnzt2laoiy",
            filenames=(
                "beer_reviews.csv",
            ), uncompress=True
        ),
    ),
    main_file="beer_reviews.csv",
    source="https://data.world/socialmediadata/beeradvocate"
)


def get_beer_reviews_df(save=True):
    data_dir = fetch(BEER_REVIEWS_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path)
    for c in df:
        arr = []
        for elt in df[c]:
            if isinstance(elt, str) and '\xa0' in elt:
                elt = elt.replace('\xa0', ' ')
            arr.append(elt)
        df[c] = pd.Series(arr, dtype=df[c].dtype, index=df.index)
    write_df(save, df, data_dir[1], BEER_REVIEWS_CONFIG.main_file)
    return df
