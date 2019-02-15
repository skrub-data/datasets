import os
from collections import namedtuple

import numpy as np
import pandas as pd

from common.file_management import fetch, write_df, float_to_int

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


def _clean_cols(cols, df):
    for c in cols:
        tab = []
        if 'Predominant' in c:
            for elt in df[c]:
                if isinstance(elt, str) and 'None' in elt:
                    tab.append(np.nan)
                else:
                    tab.append(elt)
            df[c] = pd.Series(tab, dtype=np.object, index=df.index)
        elif 'Mean Earnings' in c or 'Median Earnings' in c:
            for elt in df[c]:
                if isinstance(elt, str) and 'PrivacySuppressed' in elt:
                    tab.append(np.nan)
                elif isinstance(elt, str):
                    tab.append(int(elt))
                else:
                    tab.append(elt)
            df[c] = pd.Series(tab, dtype=np.object, index=df.index)
        elif df[c].dtype == float:
            df[c] = float_to_int(df[c], df.index)

    return df


def get_colleges_df(save=True):
    data_dir = fetch(COLLEGES_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path, sep='\t', encoding='latin1', index_col='UNITID')
    df.drop(["Unnamed: 0"], 1, inplace=True)
    df['State'] = df['State'].astype(str)
    cols = ['Undergrad Size', 'Predominant Degree', 'Average Cost Academic Year', 'Average Cost Program Year',
            'Tuition (Instate)', 'Tuition (Out of state)', 'Spend per student', 'Faculty Salary',
            'Mean Earnings 6 years', 'Median Earnings 6 years', 'Mean Earnings 10 years', 'Median Earnings 10 years']
    df = _clean_cols(cols, df)

    cats = ['State', 'Predominant Degree', 'Highest Degree', 'Ownership', 'Region', 'ZIP']
    for c in cats:
        df[c] = df[c].astype('category')

    write_df(save, df, data_dir[1], COLLEGES_CONFIG.main_file)
    return df
