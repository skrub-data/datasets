import os
from collections import namedtuple

import numpy as np
import pandas as pd

from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

MIDWEST_SURVEY_CONFIG = DatasetInfo(
    name='midwest_survey',
    urlinfos=(
        UrlInfo(
            url='https://raw.githubusercontent.com/fivethirtyeight/data/master/region-survey/MIDWEST.csv',
            filenames=(
                "FiveThirtyEight_Midwest_Survey.csv",
            ), uncompress=False
        ),
    ),
    main_file="midwest_survey.csv",
    source="https://raw.githubusercontent.com/fivethirtyeight/data/master/region-survey"
)

new_cols = ["In your own words, what would you call the part of the country you live in now?",
            'How much, if at all, do you personally identify as a Midwesterner?',
            "Do you consider Illinois state as part of the Midwest?",
            "Do you consider Indiana state as part of the Midwest?",
            "Do you consider Iowa state as part of the Midwest?",
            "Do you consider Kansas state as part of the Midwest?",
            "Do you consider Michigan state as part of the Midwest?",
            "Do you consider Minnesota state as part of the Midwest?",
            "Do you consider Missouri state as part of the Midwest?",
            "Do you consider Nebraska state as part of the Midwest?",
            "Do you consider North Dakota state as part of the Midwest?",
            "Do you consider Ohio state as part of the Midwest?",
            "Do you consider South Dakota state as part of the Midwest?",
            "Do you consider Wisconsin state as part of the Midwest?",
            "Do you consider Arkansas state as part of the Midwest?",
            "Do you consider Colorado state as part of the Midwest?",
            "Do you consider Kentucky state as part of the Midwest?",
            "Do you consider Oklahoma state as part of the Midwest?",
            "Do you consider Pennsylvania state as part of the Midwest?",
            "Do you consider West Virginia state as part of the Midwest?",
            "Do you consider Montana state as part of the Midwest?",
            "Do you consider Wyoming state as part of the Midwest?", "Gender", "Age", "Household Income",
            "Education", "Location (Census Region)"]

change_title = ['Which of the following states do you consider part of the Midwest? Please select all that apply. ',
                'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13',
                'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20',
                'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25']

copy = ['In your own words, what would you call the part of the country you live in now?',
        'In what ZIP code is your home located? (enter 5-digit ZIP code; for example, 00544 or 94305)']

squash = [
    ['How much, if at all, do you personally identify as a Midwesterner?', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5'],
    ['Gender', 'Unnamed: 28'], ['Age', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', "Unnamed: 33"],
    ['Household Income', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38'],
    ['Education', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43'],
    ['Location (Census Region)', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49',
     'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52']
]

category = ['How much, if at all, do you personally identify as a Midwesterner?', ]


def merge_columns(df: pd.DataFrame):
    new_df = pd.DataFrame(columns=new_cols)
    new_df[copy[0]] = df[copy[0]]
    new_df[copy[1]] = df[copy[1]]

    for name in change_title:
        new_col = ['Yes' if elt is not np.nan else 'No' for elt in df[name]]
        val = pd.Index(df[name])[0]
        c = [i for i, el in enumerate(new_cols) if val in el][0]
        new_df[new_cols[c]] = pd.Series(new_col, dtype=str, index=df.index)

    values = []
    for arr in squash:
        for elt in arr:
            col = pd.Index(df[elt])
            if 'unnamed:' not in elt.lower():
                values = [elt for elt in col]
            else:
                for indx2, val2 in enumerate(col):
                    if val2 is not np.nan and values[indx2] is np.nan:
                        values[indx2] = val2
        new_df[arr[0]] = pd.Series(values, dtype=df[arr[0]].dtype, index=df.index)

    new_df = new_df[new_df[
                        'In your own words, what would you call the part of the country you live in now?'] != 'Open-Ended Response']
    for c in new_df:
        if c != 'ResponsdentID' \
                and c != 'In your own words, what would you call the part of the country you live in now?' \
                and c != 'In what ZIP code is your home located? (enter 5-digit ZIP code; for example, 00544 or 94305)':
            new_df[c].astype('category')

    return new_df


def get_midwest_survey_df(save=True):
    data_dir = fetch(MIDWEST_SURVEY_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path, index_col='RespondentID')
    df = merge_columns(df)
    write_df(save, df, data_dir[1], MIDWEST_SURVEY_CONFIG.main_file)
    df.rename(columns={col: 'Location_Census_Region' for
              col in ['Location (Census Region)']}, inplace=True)
    return df


get_midwest_survey_df()
