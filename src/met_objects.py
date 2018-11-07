import os
from collections import namedtuple

import numpy as np
import pandas as pd

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
    df = pd.read_csv(csv_path, encoding='utf-8')
    cat_cols = ['Department', 'Dynasty', 'State']
    clean = ['Geography Type', 'State', 'Classification', 'Artist Role', 'Artist Prefix', 'Artist Display Bio',
             'Artist Suffix', 'Geography Type']

    period = []
    for c in df:
        arr = []
        for elt in df[c]:
            if isinstance(elt, str) and '\r\n' in elt:
                elt = elt.replace('\r\n', '')
            if isinstance(elt, str) and '\u3000' in elt:
                elt = elt.replace('\u3000', ' ')
            if isinstance(elt, str) and '\x1e' in elt:
                elt = elt.replace('\x1e', '')
            arr.append(elt)
        df[c] = pd.Series(arr, dtype=df[c].dtype, index=df.index)

    for c in df['Period']:
        if type(c) is str:
            period.append(c)
        else:
            period.append(np.nan)
    df['Period'] = pd.Series(period, dtype=np.object, index=df.index)

    for c in clean:
        tab = []
        for elt in df[c]:
            if elt == '|' or elt == '||' or elt == '(none assigned)':
                tab.append(np.nan)
            else:
                tab.append(elt)
        df[c] = pd.Series(tab, dtype=np.object, index=df.index)

    for c in cat_cols:
        df[c] = df[c].astype('category')

    write_df(save, df, data_dir[1], MET_OBJECTS_CONFIG.main_file)
    return df
