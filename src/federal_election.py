import os
import re
from collections import namedtuple

import pandas as pd
import numpy as np

from common.file_management import fetch, write_df, float_to_int

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

FEDERAL_ELECTION_CONFIG = DatasetInfo(
    name='federal_election',
    urlinfos=(
        UrlInfo(
            url='https://cg-519a459a-0ea3-42c2-b7bc-fa1143481f74.s3-us-gov-west-1.amazonaws.com/bulk-downloads/2012/indiv12.zip',
            filenames=(
                "itcont.txt",
            ), uncompress=True
        ),
    ),
    main_file="itcont.txt",
    source="https://classic.fec.gov/finance/disclosure/ftpdet.shtml"
)

FEDERAL_ELECTION_HEADER_CONFIG = DatasetInfo(
    name='federal_election',
    urlinfos=(
        UrlInfo(
            url='https://classic.fec.gov/finance/disclosure/metadata/indiv_header_file.csv',
            filenames=(
                "indiv_header_file.csv",
            ), uncompress=False
        ),
    ),
    main_file="indiv_header_file.csv",
    source="https://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml"
)


def get_federal_election_df(save=True):
    # data
    data_dir = fetch(FEDERAL_ELECTION_CONFIG)
    file = "itcont.txt"
    csv_path = os.path.join(data_dir[0], file)
    # header
    data_dir_header = fetch(FEDERAL_ELECTION_HEADER_CONFIG)
    file_header = "indiv_header_file.csv"
    csv_path_header = os.path.join(data_dir_header[0], file_header)

    df_header = pd.read_csv(csv_path_header)
    df = pd.read_csv(csv_path, sep='|', encoding='latin1',
                     header=None, names=df_header.columns)
    # Some donations are negative
    df['TRANSACTION_AMT'] = df['TRANSACTION_AMT'].abs()
    # Predicting the log of the donation
    df['TRANSACTION_AMT'] = df[
        'TRANSACTION_AMT'].apply(np.log)
    df = df[df['TRANSACTION_AMT'] > 0]
    df.rename(columns={col: col.lower() for
              col in df.columns}, inplace=True)
    df['zip_code'] = df['zip_code'].astype(str)
    df['city'].loc[1378568] = re.sub('{', '', df['city'].loc[1378568])
    df['memo_text'] = df['memo_text'].astype('category')
    write_df(save, df, data_dir[1], FEDERAL_ELECTION_CONFIG.main_file)
    return df
