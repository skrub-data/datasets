import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
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
    main_file="colleges.csv",
    source="https://beachpartyserver.azurewebsites.net/VueBigData/DataFiles"
)


def get_colleges_df(save=True):
    data_dir = fetch(COLLEGES_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pandas.read_csv(csv_path, sep='\t', encoding='latin1', index_col='UNITID')
    df.drop(["Unnamed: 0"], 1, inplace=True)
    df['State'] = df['State'].astype(str).astype('category')
    write_df(save, df, data_dir[1], COLLEGES_CONFIG.main_file)
    return df
