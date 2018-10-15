import os
from collections import namedtuple

import pandas as pd

from common.file_management import fetch, write_df, float_to_int

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

JOURNAL_INFLUENCE_CONFIG = DatasetInfo(
    name='journal_influence',
    urlinfos=(
        UrlInfo(
            url='https://github.com/FlourishOA/Data/raw/master/estimated-article-influence-scores-2015.csv',
            filenames=(
                "estimated-article-influence-scores-2015.csv",
            ), uncompress=False
        ),
    ),
    main_file="estimated-article-influence-scores-2015.csv",
    source="https://github.com/FlourishOA/Data/raw/master/"
)


def get_journal_influence_df(save=True):
    data_dir = fetch(JOURNAL_INFLUENCE_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path)
    df.drop(["Unnamed: 0"], 1, inplace=True)
    cols = ['citation_count_sum', 'paper_count_sum']
    for c in cols:
        df[c] = float_to_int(df[c], df.index)
    df['journal_name'] = df['journal_name'].astype('category')
    write_df(save, df, data_dir[1], JOURNAL_INFLUENCE_CONFIG.main_file)
    return df
