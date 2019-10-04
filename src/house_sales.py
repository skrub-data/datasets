import pandas as pd
import numpy as np
import kaggle


def get_house_sales_df():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('harlfoxem/housesalesprediction',
        path='data/house_sales/raw', unzip=True)

    csv_path = 'data/house_sales/raw/kc_house_data.csv'
    df = pd.read_csv(csv_path)
    df = pd.read_csv(csv_path, index_col=0)
    df.rename(columns={col: col.lower() for
              col in df.columns}, inplace=True)
    print(df.columns)
    df['zipcode'] = df['zipcode'].astype(str)
    df['zipcode'] = df['zipcode'].astype('category')
    return df
