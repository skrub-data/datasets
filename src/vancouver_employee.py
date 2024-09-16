import os
from collections import namedtuple

import numpy as np
import pandas as pd

from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

VANCOUVER_EMPLOYEE_CONFIG = DatasetInfo(
    name='vancouver_employee',
    urlinfos=(
        UrlInfo(
            url='ftp://webftp.vancouver.ca/OpenData/csv/2017StaffRemunerationOver75KWithExpenses.csv',
            filenames=(
                "StaffRemunerationOver75KWithExpenses.csv",
            ), uncompress=False
        ),
    ),
    main_file="2017StaffRemunerationOver75KWithExpenses.csv",
    source="https://data.vancouver.ca/datacatalogue/employeeRemunerationExpensesOver75k.htm"
)


def get_vancouver_employee_df(save=True):
    # InvalidSchema: No connection adapters were found for 'ftp://webftp.vancouver.ca/OpenData/csv/2017StaffRemunerationOver75KWithExpenses.csv'
    # data_dir = fetch(VANCOUVER_EMPLOYEE_CONFIG)
    # file = os.listdir(data_dir[0])[0]
    # csv_path = os.path.join(data_dir[0], file)

    csv_path = 'data/vancouver_employee/raw/2017StaffRemunerationOver75KWithExpenses.csv'
    df = pd.read_csv(csv_path, header=3)
    df['Remuneration'] = df['Remuneration'].apply(
                    lambda x: np.log(float(''.join(str(x).split(',')))))
    df.rename(columns={col: col.lower() for
              col in df.columns}, inplace=True)
    df['title'] = df['title'].astype('category')
    # write_df(save, df, data_dir[1], VANCOUVER_EMPLOYEE_CONFIG.main_file)
    return df
