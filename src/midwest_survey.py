import os
from collections import namedtuple

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


def get_midwest_survey_df(save=True):
    data_dir = fetch(MIDWEST_SURVEY_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path, index_col='RespondentID')

    write_df(save, df, data_dir[1], MIDWEST_SURVEY_CONFIG.main_file)
    return df
