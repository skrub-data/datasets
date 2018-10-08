import os
import pandas
from collections import namedtuple
from common.file_management import fetch

DatasetInfo = namedtuple('DatasetInfo',
                         ['name', 'urlinfos', 'main_file', 'source'])
# a DatasetInfo Object is basically a tuple of UrlInfos object
# an UrlInfo object is composed of an url and the filenames contained
# in the request content
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

data_dir = fetch(JOURNAL_INFLUENCE_CONFIG)
file = os.listdir(data_dir)[0]
csv_path = os.path.join(data_dir, file)
df = pandas.read_csv(csv_path)
