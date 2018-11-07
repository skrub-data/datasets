import os
from collections import namedtuple

import pandas as pd

from common.file_management import fetch, write_df, float_to_int

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
    df = pd.read_csv(csv_path)

    cols = ['Area Name', 'Victim Sex', 'Victim Descent', 'Premise Description', 'Weapon Description',
            'Status Description', 'Crime Code Description']
    df['Victim Age'] = float_to_int(df['Victim Age'], df.index)
    df['Premise Code'] = float_to_int(df['Premise Code'], df.index)
    df['Weapon Used Code'] = float_to_int(df['Weapon Used Code'], df.index)
    df['Crime Code 1'] = float_to_int(df['Crime Code 1'], df.index)
    df['Crime Code 2'] = float_to_int(df['Crime Code 2'], df.index)
    df['Crime Code 3'] = float_to_int(df['Crime Code 3'], df.index)
    df['Crime Code 4'] = float_to_int(df['Crime Code 4'], df.index)
    for c in cols:
        if df[c].dtype == float:
            df[c] = float_to_int(df[c], df.index)
        df[c] = df[c].astype('category')

    write_df(save, df, data_dir[1], CRIME_DATA_CONFIG.main_file)
    return df
