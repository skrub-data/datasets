import pandas as pd


def get_wine_reviews_df():
    # !kaggle datasets download zynicide/wine-reviews/ -p data/wine_reviews/raw --unzip
    csv_path = 'data/wine_reviews/raw/winemag-data_first150k.csv'
    df = pd.read_csv(csv_path, index_col=0)
    return df
    cat_cols = ['country', 'points', 'province', 'region_1',
                'region_2', 'variety']
    for c in cat_cols:
        df[c] = df[c].astype('category')
