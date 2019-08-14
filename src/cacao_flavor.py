import re
import pandas as pd


def get_cacao_flavor_df():
    # !kaggle datasets download rtatman/chocolate-bar-ratings/ -p data/cacao_flavor/raw --unzip
    csv_path = 'data/cacao_flavor/raw/flavors_of_cacao.csv'
    df = pd.read_csv(csv_path)
    df.rename(columns={old_col: re.sub('\n', ' ', old_col) for
              old_col in df.columns}, inplace=True)
    df["Broad Bean Origin"] = df["Broad Bean Origin"].astype('category')
    return df
