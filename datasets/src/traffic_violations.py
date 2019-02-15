import os
from collections import namedtuple

import numpy as np
import pandas as pd

from common.file_management import fetch, write_df, float_to_int

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
    source="https://catalog.data.gov/dataset/traffic-violations-56dda"
)


def get_traffic_violations_df(save=True):
    data_dir = fetch(TRAFFIC_VIOLATIONS_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path)
    df['Year'] = float_to_int(df['Year'], df.index)
    clean = ['Make', 'Model']
    for c in clean:
        arr = []
        for elt in df[c]:
            if elt == 'NONE':
                arr.append(np.nan)
            else:
                arr.append(elt)
        df[c] = pd.Series(arr, dtype=np.object, index=df.index)

    for c in df:
        arr = []
        for elt in df[c]:
            if isinstance(elt, str) and '\n' in elt:
                elt = elt.replace('\n', '')
            arr.append(elt)
        df[c] = pd.Series(arr, dtype=df[c].dtype, index=df.index)

    df['VehicleType'] = df['VehicleType'].astype('category')
    df['Arrest Type'] = df['Arrest Type'].astype('category')
    df['Race'] = df['Race'].astype('category')
    df['Violation Type'] = df['Violation Type'].astype('category')
    write_df(save, df, data_dir[1], TRAFFIC_VIOLATIONS_CONFIG.main_file)
    return df
