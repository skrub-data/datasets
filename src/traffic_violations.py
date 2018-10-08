import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
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
    main_file="traffic_violations.csv",
    source="https://catalog.data.gov/dataset/ traffic-violations-56dda"
)


def get_traffic_violations_df(save=True):
    data_dir = fetch(TRAFFIC_VIOLATIONS_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pandas.read_csv(csv_path)
    write_df(save, df, data_dir[1], TRAFFIC_VIOLATIONS_CONFIG.main_file)
    return df
