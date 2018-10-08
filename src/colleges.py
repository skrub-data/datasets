import os
import pandas
from collections import namedtuple
from common.file_management import fetch

DatasetInfo = namedtuple('DatasetInfo',
                         ['name', 'urlinfos', 'main_file', 'source'])

UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

COLLEGES_CONFIG = DatasetInfo(
    name='colleges',
    urlinfos=(
        UrlInfo(
            url='https://beachpartyserver.azurewebsites.net/VueBigData/DataFiles/Colleges.txt',
            filenames=(
                "Colleges.txt",
            ), uncompress=False
        ),
    ),
    main_file="Colleges.txt",
    source="https://beachpartyserver.azurewebsites.net/VueBigData/DataFiles"
)


def get_colleges_df(save=True):
    data_dir = fetch(COLLEGES_CONFIG)
    file = os.listdir(data_dir)[0]
    csv_path = os.path.join(data_dir, file)
    df = pandas.read_csv(csv_path, sep='\t', encoding='latin1')
    if save:
        df.to_csv('colleges_df.csv')
    return df
