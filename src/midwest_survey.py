import os
import pandas
from collections import namedtuple
from common.file_management import fetch

DatasetInfo = namedtuple('DatasetInfo',
                         ['name', 'urlinfos', 'main_file', 'source'])
# a DatasetInfo Object is basically a tuple of UrlInfos object
# an UrlInfo object is composed of an url and the filenames contained
# in the request content
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
    main_file="FiveThirtyEight_Midwest_Survey.csv",
    source="https://raw.githubusercontent.com/fivethirtyeight/data/master/region-survey"
)


def get_midwest_survey_df(save=True):
    data_dir = fetch(MIDWEST_SURVEY_CONFIG)
    file = os.listdir(data_dir)[0]
    csv_path = os.path.join(data_dir, file)
    df = pandas.read_csv(csv_path)
    if save:
        df.to_csv('midwest_survey_df.csv')
    return df
