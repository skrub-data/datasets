import os
import re
from collections import namedtuple

import pandas as pd
import numpy as np

from common.file_management import fetch, write_df, float_to_int

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

PUBLIC_PROCUREMENT_CONFIG = DatasetInfo(
    name='public_procurement',
    urlinfos=(
        UrlInfo(
            url='http://data.europa.eu/euodp/repository/ec/dg-grow/mapps/2019/TED_Contract_award_notices_2015.csv',
            filenames=(
                "TED_Contract_award_notices_2015.csv",
            ), uncompress=False
        ),
    ),
    main_file="TED_Contract_award_notices_2015.csv",
    source="https://data.europa.eu/euodp/en/data/dataset/ted-csv"
)


def get_public_procurement_df(save=True):

    # FIXME df.shape = (565163, 75) != from paper
    # FIXME nb category cae_name = 39623 != from paper
    # FIXME cae_name become str rather than category
    # (openml requirments)
    data_dir = fetch(PUBLIC_PROCUREMENT_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pd.read_csv(csv_path, low_memory=False)

    df.loc[df.ID_LOT == 'Zp 2130-64/15', 'ID_LOT'] = np.nan
    df.ID_LOT = df.ID_LOT.astype(float)
    df.loc[df.CRIT_PRICE_WEIGHT == '50 points',
           'CRIT_PRICE_WEIGHT'] = np.nan
    df.loc[[("%" in str(price)) for price in
           df.CRIT_PRICE_WEIGHT.values],
           'CRIT_PRICE_WEIGHT'] = np.nan
    df.CRIT_PRICE_WEIGHT = df.CRIT_PRICE_WEIGHT.astype(float)
    row_typo = []
    for row, id_lot in enumerate(df.ID_LOT_AWARDED):
        try:
            float(id_lot)
        except:
            row_typo.append(row)
    df.loc[row_typo, 'ID_LOT_AWARDED'] = np.nan  # 345 over 565163
    df.ID_LOT_AWARDED = df.ID_LOT_AWARDED.astype(float)
    df.loc[[39165, 39164], 'CONTRACT_NUMBER'] = np.nan
    df.rename(columns={col: col.lower() for
              col in df.columns}, inplace=True)
    # df['cae_name'] = df['cae_name'].astype('category')  
    df['cae_name'] = df['cae_name'].astype(str)
    tronq_cae = [str(x)[:1023] for x in df['cae_name']]
    df['cae_name'] = pd.Series(tronq_cae, dtype=df['cae_name'].dtype,
                               index=df.index)
    write_df(save, df, data_dir[1], PUBLIC_PROCUREMENT_CONFIG.main_file)
    return df
