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

EMPLOYEE_SALARIES_CONFIG = DatasetInfo(
    name='employee_salaries',
    urlinfos=(
        UrlInfo(
            url="https://data.montgomerycountymd.gov/api/views/"
                "xj3h-s2i7/rows.csv?accessType=DOWNLOAD",
            filenames=("rows.csv",),
            uncompress=False
        ),
    ),
    main_file="rows.csv",
    source="https://catalog.data.gov/dataset/employee-salaries-2016"
)


def get_employee_salaries_df(save=True):
    data_dir = fetch(EMPLOYEE_SALARIES_CONFIG)
    file = os.listdir(data_dir)[0]
    csv_path = os.path.join(data_dir, file)
    df = pandas.read_csv(csv_path)
    if save:
        df.to_csv('employee_salaries_df.csv')
    return df
