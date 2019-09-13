import pandas as pd
import numpy as np
import kaggle
import re

def get_building_permits_df():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('chicago/chicago-building-permits',
     path='data/building_permits/raw', unzip=True)
    # dataset update daily.

    csv_path = 'data/building_permits/raw/building-permits.csv'
    df = pd.read_csv(csv_path, low_memory=False)
    df.columns = df.columns.str.strip()
    df['PERMIT#'] = df['PERMIT#'].astype(str)
    for col in df.columns:
        if 'ZIPCODE' in col:  # zip code may contain '-'
            df[col] = df[col].astype(str)
    df['ESTIMATED_COST'] = (
        df['REPORTED_COST'].astype(float) + 1E-10).apply(np.log)
    df.rename(columns={col: col.lower() for
              col in df.columns}, inplace=True)
    for col in df:
        if 'contact_' in col:
            df[col] = df[col].astype(str)
    df['work_description'] = df['work_description'].astype('category')
    df.rename(columns={col: re.sub('@|:|#', '', col) for
              col in df.columns}, inplace=True)
    return df
