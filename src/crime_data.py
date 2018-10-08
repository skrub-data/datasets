import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

CRIME_DATA_CONFIG = DatasetInfo(
    name='crime_data',
    urlinfos=(
        UrlInfo(
            url="https://data.lacity.org/api/views/y8tr-7khq/rows.csv?accessType=DOWNLOAD",
            filenames=(
                "rows.csv",
            ), uncompress=True
        ),
    ),
    main_file="Crime_Data_from_2010_to_Present.csv",
    source="https://catalog.data.gov/dataset/crime-data-from-2010-to-present"
)


def get_crime_df(save=True):
    data_dir = fetch(CRIME_DATA_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pandas.read_csv(csv_path)
    write_df(save, df, data_dir[1], CRIME_DATA_CONFIG.main_file)
    return df