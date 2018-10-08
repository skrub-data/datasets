import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

MET_OBJECTS_CONFIG = DatasetInfo(
    name='met_objects',
    urlinfos=(
        UrlInfo(
            url='https://github.com/metmuseum/openaccess/raw/master/MetObjects.csv',
            filenames=(
                "MetObjects.csv",
            ), uncompress=False
        ),
    ),
    main_file="met_objects.csv",
    source="https://github.com/metmuseum/openaccess/raw/master/"
)


def get_met_objects_df(save=True):
    data_dir = fetch(MET_OBJECTS_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pandas.read_csv(csv_path)
    write_df(save, df, data_dir[1], MET_OBJECTS_CONFIG.main_file)
    return df
