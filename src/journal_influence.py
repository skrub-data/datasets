import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

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
    df = pandas.read_csv(csv_path)
    write_df(save, df, data_dir[1], JOURNAL_INFLUENCE_CONFIG.main_file)
    return df
