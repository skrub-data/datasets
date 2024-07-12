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

    for col in ['company__(maker-if_known)',
            'specific_bean_origin_or_bar_name',
            'broad_bean_origin']:
        if col == 'broad_bean_origin':
                df[col].fillna('\xa0', inplace=True) #replace one nan by space
        df[col] = [re.sub('&','et',s) for s in list(df[col])]
        df[col] = [re.sub('\xa0',' ',s) for s in list(df[col])]
    # drop the only row with missing label
    df.drop(index = df.index[df['bean_type'].isna()], inplace=True)       
    return df
