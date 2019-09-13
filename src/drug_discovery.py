import os
from collections import namedtuple

import pandas as pd

from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

DRUG_DISCOVERY_CONFIG = DatasetInfo(
    name='drug_discovery',
    urlinfos=(
        UrlInfo(
            url="https://www.accessdata.fda.gov/cder/ndctext.zip",
            filenames=(
                "product.txt",
            ), uncompress=False
        ),
    ),
    main_file="product.txt",
    source="https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory"
)


def get_drug_discovery_df(save=True):
    data_dir = fetch(DRUG_DISCOVERY_CONFIG)
    file = os.listdir(data_dir[0])[1]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path, sep='\t', encoding='latin1')
    cat_cols = ['DRG Definition', 'Provider State']
    for c in cat_cols:
        df[c] = df[c].astype('category')
    df.rename(columns={col: re.sub(' ', '_', col).lower() for
              col in df.columns}, inplace=True)
    write_df(save, df, data_dir[1], DRUG_DISCOVERY_CONFIG.main_file)
    return df
