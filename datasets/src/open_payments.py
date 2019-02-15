import os
from collections import namedtuple

import pandas as pd

from common.file_management import fetch, write_df

amount = ['Total_Amount_of_Payment_USDollars']
corp = ['Applicable_Manufacturer_or_Applicable_GPO_Making_' + 'Payment_Name']
dev_nm = ['Name_of_Associated_Covered_Device_or_Medical_Supply1']
dispute = ['Dispute_Status_for_Publication']
drug_nm = ['Name_of_Associated_Covered_Drug_or_Biological1']
pi_specialty = ['Physician_Specialty']

df_cols = pi_specialty + drug_nm + dev_nm + corp + dispute

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

OPEN_PAYMENTS_CONFIG = DatasetInfo(
    name='open_payments',
    urlinfos=
    (
        UrlInfo(
            url='http://download.cms.gov/openpayments/PGYR13_P062918.ZIP',
            filenames=None, uncompress=True
        ),
    ),
    main_file='open_payments.csv',
    source='https://openpaymentsdata.cms.gov'
)


def _get_file_paths(directory):
    f = {file: os.path.join(directory, file) for file in os.listdir(directory) if
         '.txt' not in file and 'REMOVED' not in file and 'OWNRSHP' not in file}
    return f


def _process_df(files):
    res_df = pd.DataFrame(columns=df_cols)

    for key in files:
        df = pd.read_csv(files[key])
        df = df[df_cols]

        if 'RSRCH' in key:
            df['status'] = 'allowed'
        elif 'GNRL' in key:
            df['status'] = 'disallowed'

        df = df.drop_duplicates(keep='first')
        res_df = pd.concat([res_df, df], ignore_index=True, sort=True)

    res_df = res_df.drop_duplicates(keep='first')
    return res_df


def get_open_payment_df(save=True):
    data_dir = fetch(OPEN_PAYMENTS_CONFIG)
    files = _get_file_paths(data_dir[0])
    df = _process_df(files)
    df['Physician_Specialty'] = df['Physician_Specialty'].astype('category')
    write_df(save, df, data_dir[1], OPEN_PAYMENTS_CONFIG.main_file)
    return df
