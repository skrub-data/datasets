import re

import pandas as pd
import numpy as np


def get_kickstarter_projects_df():
    # !kaggle datasets download kemical/kickstarter-projects -p data/kickstarter_projects/raw --unzip 

    # there are two. Pick the oldest one
    csv_path = 'data/kickstarter_projects/raw/ks-projects-201801.csv' 
    df = pd.read_csv(csv_path, encoding='latin1', index_col=0)
    df = df[df['state'].isin(['failed', 'successful'])]
    df['state'] = (df['state'] == 'successful')
    df['usd pledged'] = (
        df['usd pledged'].astype(float) + 1E-10).apply(np.log)
    df['name'] = ([re.sub('{', '(', str(name)) for name in df.name.values])
    df['name'] = ([re.sub('}', ')', str(name)) for name in df.name.values])
    df['category'] = df['category'].astype('category')
    return df
