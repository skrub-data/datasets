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

TRAFFIC_VIOLATIONS_CONFIG = DatasetInfo(
    name='traffic_violations',
    urlinfos=(
        UrlInfo(
            url="https://data.montgomerycountymd.gov/api/views/"
                "4mse-ku6q/rows.csv?accessType=DOWNLOAD",
            filenames=(
                "rows.csv",
            ), uncompress=True
        ),
    ),
    main_file="rows.csv",
    source="https://catalog.data.gov/dataset/ traffic-violations-56dda"
)


def get_traffic_violations_df(save=True):
    data_dir = fetch(TRAFFIC_VIOLATIONS_CONFIG)
    file = os.listdir(data_dir)[0]
    csv_path = os.path.join(data_dir, file)
    df = pandas.read_csv(csv_path)
    if save:
        df.to_csv('traffic_violations_df.csv')
    return df
