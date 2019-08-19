import re
import pandas as pd


def get_cacao_flavor_df():
    # !kaggle datasets download rtatman/chocolate-bar-ratings/ -p data/cacao_flavor/raw --unzip
    csv_path = 'data/cacao_flavor/raw/flavors_of_cacao.csv'
    df = pd.read_csv(csv_path)
    df.rename(columns={col: re.sub('\xa0', ' ', col) for
              col in df.columns}, inplace=True)
    df.rename(columns={col: re.sub('\n', '_', col) for
              col in df.columns}, inplace=True)
    df.rename(columns={col: re.sub(' ', '_', col).lower() for
              col in df.columns}, inplace=True)
    df["broad_bean_origin"] = df["broad_bean_origin"].astype('category')
    return df
